import hashlib
import os

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from share.models import User, Image, Port, Container, Subscription


def login(request):
    if request.method == "POST":
        input_name = request.POST['username']
        input_pwd = hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest()
        try:
            user = User.objects.get(name=input_name)
        except:
            return render(request, 'share/login.html', {'error_message': 'Check the username you entered'})
        else:
            if input_pwd == user.password:
                request.session['user'] = user.id
                return HttpResponseRedirect(reverse('share:info'))
            else:
                return render(request, 'share/login.html', {'error_message': 'Incorrect password'})
    if request.session.get('user', None):
        return HttpResponseRedirect(reverse('share:info'))
    return render(request, 'share/login.html')


def register(request):
    if request.method == "POST":
        input_name = request.POST['username']
        input_pwd = request.POST['password']
        input_email = request.POST['email']
        if User.objects.filter(name=input_name).count() > 0:
            return render(request, 'share/register.html', {'error_message': 'Username has been used! Try another'})
        User.objects.create(
            name=input_name,
            password=hashlib.md5(input_pwd.encode('utf-8')).hexdigest(),
            email=input_email
        )
        request.session.flush()
        return HttpResponseRedirect(reverse('share:login'))
    return render(request, 'share/register.html')


def info(request):
    if request.session.get('user', None):
        user = User.objects.get(pk=request.session['user'])
        return render(request, 'share/info.html', {'user': user})
    else:
        return render(request, 'share/login.html')


def container(request, image_id):
    available_ports = Port.objects.filter(status=False)
    if available_ports.count() == 0:
        return render(request, 'share/container.html',
                      {'error_message': 'No port available now . Try another time .'})
    using_port = available_ports.first()
    using_port.status = True
    using_port.save()
    image = Image.objects.get(pk=image_id)
    container_num = os.popen(
        './share/scripts/run_image.sh %s %s' % (str(using_port.port_number), image.serial_number)) \
        .read() \
        .strip()
    Container.objects.create(
        image_id=image_id,
        user_id=request.session['user'],
        port_id=using_port.id,
        serial_number=container_num
    )
    return render(request, 'share/container.html', {
        'image': image,
        'container': container,
        'port_num': using_port.port_number,
        'container_num': container_num,
    })


def ajax_stop_container(request, container_id):
    os.popen('./share/scripts/stop_container.sh %s' % container_id)
    container_delete = Container.objects.get(serial_number=container_id)
    container_delete.port.status = False
    container_delete.port.save()
    container_delete.delete()
    return JsonResponse({})


def ajax_commit_stop_container(request, container_serial_num, description):
    image_rtn_num = os.popen('./share/scripts/commit_and_stop.sh %s' % container_serial_num)
    image_serial = image_rtn_num[7:].strip()
    container_delete = Container.objects.get(serial_number=container_serial_num)
    container_delete.port.status = False
    container_delete.port.save()
    container_delete.delete()
    Image.objects.create(user_id=request.session['user'], description=description, serial_number=image_serial)
    return JsonResponse({})


def configure_subscription(request):
    if request.session.get('user', None):
        user_id = request.session['user']
        return render(request, 'share/subscription.html', {
            'login_user': User.objects.get(id=request.session['user']),
            'subscripters': [subscripter.target for subscripter in
                             User.objects.get(id=user_id).subscription_user.all()],
            'users': User.objects.all(),
        })
    else:
        return render(request, 'share/login.html')


def add_user(request, user_id):
    source = User.objects.get(id=request.session['user'])
    target = User.objects.get(id=user_id)
    Subscription.objects.create(source=source, target=target)
    return HttpResponseRedirect(reverse('share:configureSubscription'))


def delete_user(request, user_id):
    target = User.objects.get(id=user_id)
    User.objects.get(id=request.session['user']).subscription_user.filter(target=target).delete()
    return HttpResponseRedirect(reverse('share:configureSubscription'))

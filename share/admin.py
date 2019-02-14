from django.contrib import admin

# Register your models here.
from share.models import User, Subscription, Image, Container, Port

admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Image)
admin.site.register(Container)
admin.site.register(Port)
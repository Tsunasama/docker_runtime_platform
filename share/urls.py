from django.urls import path

from share import views

app_name = 'share'
urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('info', views.info, name='info'),
    path('container/<image_id>', views.container, name='container'),
    path('stop_container/<container_id>', views.ajax_stop_container, name='stop_container'),
    path('commit_stop_container/<container_serial_num>/<description>',views.ajax_commit_stop_container,name='commit_stop_container'),
    path('configure_subscription',views.configure_subscription,name='configureSubscription'),
    path('add_user/<user_id>',views.add_user,name='addUser'),
    path('delete_uer/<user_id>',views.delete_user,name='deleteUser'),
]

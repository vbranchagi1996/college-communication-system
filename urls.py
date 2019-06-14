from django.conf.urls import url
from student import views
from django.contrib.auth import views as auth_views
# SET THE NAMESPACE!
app_name = 'student'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^email2/$',views.tryView, name='email2'),
    url(r'^email3/$',views.tryView2, name='email3'),
    url(r'^success/$',views.success, name='success'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^index/$', views.index, name='index'),
    url(r'^email/$',views.emailView, name='email'),
    url(r'^loginnext/$',views.loginnext, name='loginnext'),
    url(r'^sms/$', views.sms, name='sms'),
    url(r'^user_login2/$', views.user_login2, name='user_login2'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^success2/$',views.success2, name='success2'),
    url(r'^success3/$',views.success3, name='success3'),

]

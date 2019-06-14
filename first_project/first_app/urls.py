from django.conf.urls import url
from first_app import views

app_name = 'prj'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]

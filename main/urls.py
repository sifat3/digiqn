from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('what_we_do/', views.wwd, name='what we do'),
    path('contact/', views.contactus, name='contact'),
<<<<<<< HEAD
    path('request/<int:pk>', views.request_page, name='request'),
<<<<<<< HEAD
    path('admin-area', views.admin_area, name='admin_area'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
=======
    path('request/<int:pk>', views.request_page, name='request')
>>>>>>> parent of 8980747 (4th edit)
=======
    path('admin-area', views.admin_area, name='admin_area')
>>>>>>> parent of b457f18 (5th edit)
]
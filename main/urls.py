from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('what_we_do/', views.wwd, name='what we do'),
    path('contact/', views.contactus, name='contact'),
    path('request/<int:pk>', views.request_page, name='request'),
    path('admin-area', views.admin_area, name='admin_area')
]
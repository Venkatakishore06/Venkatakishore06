from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login',views.log_read,name='login'),
    path('Products',views.Products,name='Products')
]
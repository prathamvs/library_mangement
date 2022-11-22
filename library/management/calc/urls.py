from django.urls import path
from  . import views

urlpatterns = [
    path('',views.home,name='home'), #Calling for home Page
    path('login/',views.login,name='login')
]
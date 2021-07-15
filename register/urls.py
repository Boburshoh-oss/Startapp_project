from django.urls import path
from .views import *

app_name = 'register'

urlpatterns = [
    path('register/' , register , name='register'),
    path('login/',log_in , name='login')
]
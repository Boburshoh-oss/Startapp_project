from django.urls import path
from .views import *


urlpatterns = [
    path('' , home , name='home'),
    # path('strtapper' , Startappersview.as_view() , name='startapper'),
    # path('developer' , Devlopersview.as_view() , name='developer'),
]
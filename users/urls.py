from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', index , name='index'),
    path('startapper/' , startapper , name='Startapper'),
    path('developer/' , developer , name='Developer'),
    path('practitioner/', practitioner , name='Practitioner'),
    path('detail/', detail , name='detail'),
     path('ideastartapper/', ideastartapper, name='ideastartapper'),
]
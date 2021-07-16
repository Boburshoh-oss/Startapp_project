from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', index , name='index'),
    path('startapper/' , startapper , name='Startapper'),
    path('developer/' , developer , name='Developer'),
    path('practitioner/', practitioner , name='Practitioner'),
    path('profile/' , profile_page , name='profile'),
    path('update/<int:pk>' , StaffUpdateWiew.as_view() , name='update' ),
    path('application_update/<int:pk>' , AppUpdateWiew.as_view() , name='appupdate' ),
]
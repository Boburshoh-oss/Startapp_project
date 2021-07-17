from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', index , name='index'),
    path('startapper/' , startapper , name='Startapper'),
    path('developer/' , developer , name='Developer'),
    path('practitioner/', practitioner , name='Practitioner'),

    path('ideastartapper/', ideastartapper, name='ideastartapper'),
    
    path('profile/' , profile_page , name='profile'),
    
    path('staffupdate/<int:pk>' , StaffUpdateWiew.as_view() , name='staffupdate' ),
    path('startapperupdate/<int:pk>' , StartapperUpdateWiew.as_view() , name='startapperupdate' ),
    path('application_update/<int:pk>' , AppUpdateWiew.as_view() , name='appupdate' ),


]
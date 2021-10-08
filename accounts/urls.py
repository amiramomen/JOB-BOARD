
from django.urls import path , include
from .import views
app_name = 'accounts'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('logged_out',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
 
]

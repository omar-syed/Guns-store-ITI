from django.urls import path,include
from .views import profile,CreateCustomUser
urlpatterns = [
    
    path('',include('django.contrib.auth.urls')),
    path('profile/',profile,name='profile'),
    path('register',CreateCustomUser.as_view(), name='accounts.create')
]

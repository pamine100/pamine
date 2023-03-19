from django.urls import path
from . import views

urlpatterns = [
    path('pamine/',views.home, name='home'),
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('pamine/livepage/', views.livepage, name='livepage'),
    path('pamine/setuplive/', views.livesetup, name='setuplive'),
    path('setuplive/', views.livesetup, name='livesetup'),
]

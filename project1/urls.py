
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_request, name='login_request'),
    path('logout', views.logout_request, name='logout'),
    path('home', views.home, name='home'),
    path('liked', views.liker, name='like_v'),
    path('image_upload', views.upp, name='image_upload'),
    path('top', views.top_photos, name='top_photos'),
    path('search', views.search, name='search'),

    
    
]

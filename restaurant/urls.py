from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('check/', views.check, name="check server"),
    path('book/', views.book, name="book"),
    path('track/', views.track, name="track reservation"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>', views.display_menu_item, name="menu_item"),
]
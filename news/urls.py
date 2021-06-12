from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact', views.contact, name='contact'),
    path('content',views.content,name='content'),
    path('academics',views.academics,name='academics'),
    path('sports', views.sports, name='sports'),
    path('management', views.management, name='management'),
    path('culture', views.culture, name='culture'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('add_news',views.add_news,name='add_news'),
    path('admin_menu',views.admin_menu,name='admin_menu'),
    path('edit_news',views.edit_news,name="edit_news"),
    path('delete_news',views.delete_news,name='delete_news'),
    path('edit_details',views.edit_details,name="edit_details")
]
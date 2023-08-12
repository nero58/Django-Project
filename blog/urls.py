from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='blog_homie'),
    path('about/',views.about,name='blog_about'),
]
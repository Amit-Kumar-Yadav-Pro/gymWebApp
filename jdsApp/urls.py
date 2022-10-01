
from django.contrib import admin
from django.urls import path

from jdsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('About-us/', views.about),
    path('Shop/', views.shop),
    path('Contact/', views.contact),
    path('Blog/<blog_title>', views.blogDetails),
]

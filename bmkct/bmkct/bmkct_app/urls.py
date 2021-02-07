from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete_group),
    path('add/', views.add_group),
    path('add-box', views.add_box),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path('<slug:group_name>/<int:id>', views.group_list),

]

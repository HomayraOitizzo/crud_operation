"""
URL configuration for practice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views

app_name = "first_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name= 'index'  ),
    path('res_form/', views.res_form, name="res_form"),
    path('menu_form', views.menu_form, name="menu_form"),
    path('menu_list/<int:food_id>/', views.menu_list, name="menu_list"),
    path('edit_res/<int:food_id>/', views.edit_res, name='edit_res'),
    path('edit_menu/<int:food_id>/', views.edit_menu, name="edit_menu"),
    path('delete_menu/<int:food_id>/', views.delete_menu, name="delete_menu")

]

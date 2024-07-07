from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Restaurants, Menu
from first_app import forms
# Create your views here.

def index(request):
    res_list = Restaurants.objects.order_by('res_name')
    diction={'title': "Home page", 'res_list':res_list}
    return render(request, 'index.html', context=diction)
def menu_list(request, food_id):
    res_info = Restaurants.objects.get(pk=food_id)
    food_list = Menu.objects.filter(food=food_id)
    diction={'title': "List Of Foods", "res_info":res_info, "food_list":food_list}
    return render(request, 'menu_list.html', context=diction)
def res_form(request):
    form = forms.RestaurantForm()
   

    if request.method == 'POST':
        form = forms.RestaurantForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':"Add Restaurant", 'res_form':form}

    return render(request, 'restaurant_form.html', context=diction)
def menu_form(request):
    form = forms.Menuform()

    if request.method == 'POST':
        form = forms.Menuform(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title':"Add Menu", "menu_form":form}
    return render(request, 'menu_form.html', context=diction)
   
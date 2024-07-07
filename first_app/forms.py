from django import forms
from first_app import models

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurants
        fields = "__all__"
        #exlcude = ['res_name'] evabe bad deya jay field
        #fields = ('res_name', 'location') evabe jototuk chai tototuk include kora jabe
class Menuform(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = "__all__"
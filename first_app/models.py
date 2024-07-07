from django.db import models

# Create your models here.
class Restaurants(models.Model):
    res_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    cuisine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.res_name + " " + self.location
    

class Menu(models.Model):
    food = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price= models.IntegerField()


    rating = (
        (1,"Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Great")
    )    
    num_stars= models.IntegerField(choices=rating, default=0)

    def __str__(self):
        return self.name + " ,Rating: " + str(self.num_stars)




from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



PRADESH_CHOICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4 ', '4'),
    ('5 ', '5'),
    ('6 ', '6'),
    ('7 ', '7'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    Pradesh = models.CharField(choices=PRADESH_CHOICE, max_length=50)

    def __str__(self):
        return str(self.id)



PASAL_CHOICES = (

    ('M', 'MAKEUP'),
    ('F', 'FASHION_WEARS'),
    ('E', 'Electronics'),
    ('FO', 'FOODS'),   
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    Price = models.FloatField()
    Selling_Price= models.FloatField()
    Description = models.TextField()
    Manufacturer = models.CharField(max_length=100)
    category = models.CharField(choices=PASAL_CHOICES, max_length=2)
    Image = models.ImageField(upload_to='image')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)




STATUS_CHOICES = (
    ('A', 'Accepted'),
    ('P', 'Packed'),
    ('O', 'On The Way'),
    ('D', 'Delievered'),
    ('C', 'Cancel')
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    Purchased_Date = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')





from django.db import models
from django.contrib.auth.models import User



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




from django.db import models

# Create your models here.
ID_CHOICES = (
    ('Driver License', 'Driver License'),
    ('SSS ID', 'SSS ID'),
    ('Postal ID', 'Postal ID'),
    ('Student ID', 'Student ID'),
)

ACCOUNT_TYPE_CHOICES = (
    ('Buyer', 'Buyer'),
    ('Seller', 'Seller'),
)

class PersonAccount(models.Model):
    email = models.EmailField(max_length=70, null=False, blank=False)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=256,)
    id_options = models.CharField(choices=ID_CHOICES, max_length=64)
    id_image = models.ImageField()
    creationDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICES, max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
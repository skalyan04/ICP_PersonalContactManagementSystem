from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

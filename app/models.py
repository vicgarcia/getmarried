from django.db import models



class RSVP(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)
    guests = models.IntegerField()
    note = models.TextField(null=False, blank=True)


class Gift(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    note = models.TextField(null=False, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    raw = models.TextField()    # entire response from stripe


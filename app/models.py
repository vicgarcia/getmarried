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
    order = models.CharField(max_length=250)   # stripe order id
    amount = models.IntegerField()             # stripe returns amounts as cents
    raw = models.TextField()                   # save the entire stripe response


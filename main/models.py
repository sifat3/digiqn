from django.db import models


class Request(models.Model):
    sender_name = models.CharField(max_length=200, blank=False, null=False)
    receiver_name = models.CharField(max_length=200, blank=False, null=False)
    sender_email = models.EmailField(blank=False, null=False)
    receiver_email = models.EmailField(blank=False, null=False)
    ammount = models.IntegerField(blank=False, null=False)
    service_description = models.TextField()
    payment_done = models.BooleanField(default=False)
    service_done = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=500, blank=True, null=True)







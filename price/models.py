from django.db import models



class DayPrice(models.Model):
    code = models.CharField(max_length=32)
    date = models.DateField
    created_at = models.DateField(auto_now_add=True)

    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
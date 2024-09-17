from django.db import models

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    is_donated = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

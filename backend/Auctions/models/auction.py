from base.models import Base
from django.db import models
from django.conf import settings 
from django.utils import timezone

class AuctionItems(Base):
    class Status(models.TextChoices):
        DRAFT = ("Draft","draft")
        ACTIVE = ("Active" , "active")
        ENDED = ("Ended" , "ended")
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10 , decimal_places=2)
    current_high_price = models.DecimalField(max_digits=10 , decimal_places=2 , default=0)
    status = models.CharField(max_length=10 , default=Status.DRAFT)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items_for_sale')
    start_time = models.DateField()
    end_time = models.DateField()
    def __str__(self):
        return f"Item: {self.title}"

    @property
    def is_active(self):
        return self.status in (self.Status.DRAFT ,self.Status.ACTIVE) and self.end_time < timezone.now()
    
    class Meta:
        db_table = "auction"
        verbose_name = "auction"
    
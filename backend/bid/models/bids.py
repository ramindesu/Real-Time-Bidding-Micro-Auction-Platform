from base.models import Base
from django.db import models
from django.conf import settings
from Auctions.models.auction import AuctionItems

class Bid(Base):

    auction_item = models.ForeignKey(AuctionItems, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='placed_bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"user : {self.bidder.username} offered {self.amount}"
    
    class Meta:
        verbose_name = "bid"
        ordering = ['-amount'] 
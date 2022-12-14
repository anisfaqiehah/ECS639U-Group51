from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50, unique=True)
    city=models.CharField(max_length=100,null=True)
    dob=models.DateField(null=True,blank=True)
    bio=models.TextField(blank=True)
    image=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.username}"
    def to_dict(self):
        return {
            'id': self.id,
              'username':self.username,
              "email":self.email,
                  'city': self.city,
                  'dob':self.dob,
                  "bio":self.bio,
                 
                  }

"""""
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    city=models.CharField(max_length=100)
    dob=models.DateField(null=True,blank=True)
    bio=models.TextField(blank=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
            return f"{self.user}"
    def to_dict(self):
        return {
              
                  'city': self.city,
                  'dob':self.dob,
                  "bio":self.bio,
                 
                  }
                  """

class Item(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_list")
    title = models.CharField(max_length=64)
    picture=models.ImageField(null=True,blank=True)
    description = models.TextField(max_length=256, blank=True)
    starting_bid = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.CharField(max_length=24, default='No Category')
    status = models.BooleanField(default=True)
    start_date=models.DateTimeField(auto_now=True)
    end_date= models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.title}, {self.description}"
    def to_dict(self):
            return {
                  'id': self.id,
                  'title': self.title,
                  'description':self.description,
                  "starting_bid":self.starting_bid,
                  "category":self.category,
                "status":self.status,
                "start_date":self.start_date,
                "end_date":self.end_date,

                  }

class ItemCategory(models.Model):
    name = models.CharField(max_length=24, blank=False)
    item = models.ForeignKey(Item, blank=True, on_delete=models.CASCADE, related_name="category_list")
    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="user_bid_items", blank=True)
    def __str__(self):
        return f"{self.amount}"
    
class ItemComment(models.Model):
    text = models.TextField(max_length=512, blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="comments_list")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Watchlist(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist_list')

    def __str__(self):
        return f"{self.items}, {self.user}"

class Category(models.Model):
    name = models.CharField(max_length=24, blank=False)
    items = models.ManyToManyField(Item, blank=True, related_name="categories")

    def __str__(self):
        return f"{self.name}"

class AuctionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history_user")
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="items_auction_history")

    def __str__(self):
        return f"{self.user.first_name}, {self.items}"



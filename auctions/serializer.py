from rest_framework  import serializers
from .models import Item,User

class ItemSerializer(serializers.ModelSerializer):
      class Meta:
            model=Item
            fields=['id','title','description','description',"starting_bid","category","category","status","start_date","end_date"]


class ProfileSerializer(serializers.ModelSerializer):
      class Meta:
            model=User
            fields=["id","username","email","city","dob","bio"]
            
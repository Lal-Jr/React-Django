from django.db.models import fields
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause','vote_to_skip','created_at')
        
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause','votes_to_skip')

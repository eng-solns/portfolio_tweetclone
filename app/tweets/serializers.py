from rest_framework import serializers
from tweets.models import Tweet
from tweets.models import User



class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'title', 'content', 'published', 'user')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
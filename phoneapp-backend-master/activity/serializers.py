from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
#for generating token


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        fields = ('id', 'title', 'thumbnail','owner')
        


class ArticleDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        fields = ('id', 'title', 'thumbnail', 'body','owner')
        

		
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'password','groups','user_permissions','is_staff','is_active','is_superuser','date_joined','activities')
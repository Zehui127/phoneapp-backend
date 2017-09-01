from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'thumbnail')


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'thumbnail', 'body')


		
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'password','groups','user_permissions','is_staff','is_active','is_superuser','date_joined')
from rest_framework import serializers
from blog.models import Category, Post, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','title', 'description', 'category', 'tags', 'author', 'created_at', 'updated_at']




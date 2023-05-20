from rest_framework import serializers
from client.models import User
from post.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'report_count', 'ban']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    like = LikeSerializer(many=False, read_only=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    @staticmethod
    def get_category(obj):
        return CategorySerializer(obj.category.all(), many=True).data
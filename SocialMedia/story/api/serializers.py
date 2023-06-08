from rest_framework import serializers
from client.models import User
from story.models import Story


class UserSafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class StorySerializer(serializers.ModelSerializer):
    owner = UserSafeSerializer(many=False, read_only=True)
    friends = serializers.SerializerMethodField()

    class Meta:
        model = Story
        exclude = ['deleted']

    @staticmethod
    def get_friends(obj):
        return UserSafeSerializer(obj.friends.all(), many=True).data

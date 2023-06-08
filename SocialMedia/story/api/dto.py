from rest_framework import serializers


class StoryViewDto(serializers.Serializer):
    privet = serializers.BooleanField()
    title = serializers.CharField()
    story_file = serializers.FileField(required=False)


class GetFriendsStoryViewDto(serializers.Serializer):
    friends = serializers.ListField()


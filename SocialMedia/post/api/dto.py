from rest_framework import serializers


class BlogViewDto(serializers.Serializer):
    image = serializers.FileField()
    title = serializers.CharField()
    description = serializers.CharField()
    category = serializers.ListField()

from rest_framework import serializers


class BlogViewDto(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    is_comment = serializers.BooleanField()
    image = serializers.FileField(required=False)
    category = serializers.ListField(required=False)


class CategoryViewDto(serializers.Serializer):
    name = serializers.CharField()
    parent = serializers.IntegerField(required=False)


class LikeViewDto(serializers.Serializer):
    like = serializers.BooleanField()
    blog = serializers.IntegerField()

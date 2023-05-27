from rest_framework import serializers


class LoginViewDto(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ProfileViewDto(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    cellphone = serializers.CharField(required=False)
    privet = serializers.BooleanField()
    age = serializers.DateTimeField(required=False)
    bio = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)


class TokenViewDto(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class RegisterViewDto(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    re_password = serializers.CharField()


class RequestStatusViewDto(serializers.Serializer):
    status = serializers.BooleanField()

class ReportViewDto(serializers.Serializer):
    user = serializers.IntegerField()
    text = serializers.CharField()



class RequestUserViewDto(serializers.Serializer):
    user = serializers.IntegerField()


class RequestUserStatusViewDto(serializers.Serializer):
    status = serializers.BooleanField()

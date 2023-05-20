from .imports import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'report_count', 'ban']


class UserSafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'get_full_name']


class ReportSerializer(serializers.ModelSerializer):
    owner = UserSafeSerializer(many=False, read_only=True)
    user = UserSafeSerializer(many=False, read_only=True)

    class Meta:
        model = Report
        fields = '__all__'

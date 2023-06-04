from .imports import *


class UserSafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    owner = UserSafeSerializer(many=False, read_only=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    @staticmethod
    def get_category(obj):
        return CategorySerializer(obj.category.all(), many=True).data


class LikeSerializer(serializers.ModelSerializer):
    owner = UserSafeSerializer(many=False, read_only=True)
    blog = BlogSerializer(many=False, read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    owner = UserSafeSerializer(many=False, read_only=True)
    blog = BlogSerializer(many=False, read_only=True)

    class Meta:
        model = Comments
        exclude = ['deleted']

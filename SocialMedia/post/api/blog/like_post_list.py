from .imports import *


class LikePostList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: BlogViewDto(many=True)})
    def get(self, request):
        context = {}
        likes = Like.objects.filter(owner=request.user, like=True)
        posts = Blog.objects.filter(deleted=False, status=True, id__in=likes)
        context['posts'] = BlogSerializer(posts, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

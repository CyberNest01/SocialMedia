from .imports import *


class MyPostList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: BlogViewDto(many=True)})
    def get(self, request):
        context = {}
        posts = Blog.objects.filter(owner=request.user, deleted=False, status=True)
        context['posts'] = BlogSerializer(posts, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

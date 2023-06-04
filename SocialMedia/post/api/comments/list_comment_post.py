from .imports import *


class ListCommentPost(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: CommentsViewDto(many=True)})
    def get(self, request, pk):
        context = {}
        try:
            q = Q(owner_id__in=request.user.get_friends(request)) | Q(owner__privet=False) | Q(owner=request.user)
            post = Blog.objects.get(q, id=pk, deleted=False, status=True)
            comments = Comments.objects.filter(blog=post, deleted=False).order_by(request.GET.get('order_by', '-id'))
            context['comments'] = CommentsSerializer(comments, many=True).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'پست یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

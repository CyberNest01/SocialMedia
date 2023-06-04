from .imports import *


class MyCommentsList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: CommentsViewDto(many=True)})
    def get(self, request):
        context = {}
        comments = Comments.objects.filter(owner=request.user, deleted=False).order_by(request.GET.get('order_by', '-id'))
        context['comments'] = CommentsSerializer(comments, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

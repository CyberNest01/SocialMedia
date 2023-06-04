from .imports import *


class CommentSingle(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=CommentsViewDto, responses={200: CommentsViewDto(many=False)})
    def post(self, request):
        context = {}
        comment = Comments(owner=request.user)
        try:
            q = Q(owner__in=request.user.get_friends(request)) | Q(owner__privet=False) | Q(owner=request.user)
            comment.blog = Blog.objects.get(q, id=int(request.data.get('blog')), deleted=False, status=True)
        except:
            context['msg'] = 'پست یافت نشد'
            status_code = HTTP_400_BAD_REQUEST
            return Response(context, status=status_code)
        comment.message = request.data.get('message').strip()
        comment.save()
        context['comment'] = CommentsSerializer(comment, many=False).data
        context['msg'] = 'ذخیره شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: CommentsViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            comment = Comments.objects.get(id=pk, deleted=False, owner=request.user)
            context['comment'] = CommentsSerializer(comment, many=False).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: CommentsViewDto(many=False)})
    def delete(self, request, pk):
        context = {}
        try:
            comment = Comments.objects.get(id=pk, deleted=False, owner=request.user)
            comment.delete()
            context['msg'] = 'حذف شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=CommentsEditViewDto, responses={200: CommentsEditViewDto(many=False)})
    def put(self, request, pk):
        context = {}
        try:
            comment = Comments.objects.get(id=pk, deleted=False, owner=request.user)
            comment.message = request.data.get('message', comment.message).strip()
            comment.save()
            context['comment'] = CommentsSerializer(comment, many=False).data
            context['msg'] = 'تغییرات اعمال شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

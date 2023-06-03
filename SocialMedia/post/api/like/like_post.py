from .imports import *


class LikePost(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=LikeViewDto, responses={200: LikeViewDto(many=False)})
    def post(self, request):
        context = {}
        q = Q(owner=request.user, blog_id=int(request.data.get('blog')))
        if Like.objects.filter(q).exists():
            try:
                like = Like.objects.get(q)
                like.like = bool(request.data.get('like', Like.like))
            except:
                like = Like.objects.filter(q)
                like.delete()
                context['msg'] = 'دوباره امتحان کنید'
                status_code = HTTP_400_BAD_REQUEST
                return Response(context, status=status_code)
        else:
            like = Like(like=bool(request.data.get('like')))
            like.owner = request.user
            try:
                like.blog = Blog.objects.get(id=int(request.data.get('blog')), deleted=False, status=True)
            except:
                context['msg'] = 'بلاگ یافت نشد'
                status_code = HTTP_404_NOT_FOUND
                return Response(context, status=status_code)
        like.save()
        context['like'] = LikeSerializer(like, many=False).data
        if request.data.get('like'):
            context['msg'] = 'لایک شد'
        else:
            context['msg'] = 'دیس لایک شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: LikeViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            like = Like.objects.get(id=pk, owner=request.user)
            context['like'] = LikeSerializer(like, many=False).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)




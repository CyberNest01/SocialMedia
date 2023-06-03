from .imports import *


class FriendsPostList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: BlogViewDto(many=True)})
    def get(self, request):
        context = {}
        posts = Blog.objects.filter(owner__in=User.get_friends(request), deleted=False, status=True,
                                    owner__is_active=True).order_by(request.GET.get('order_by', '-id'))
        context['posts'] = BlogSerializer(posts, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

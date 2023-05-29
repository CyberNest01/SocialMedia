from django.db.models import Q

from .imports import *


class UserPostList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: BlogViewDto(many=True)})
    def get(self, request, pk):
        context = {}
        q = Q(owner__in=User.get_friends(request)) | Q(owner__privet=False) | Q(owner=request.user)
        try:
            user = User.objects.get(id=pk, is_active=True)
            if user not in User.get_friends(request) and user != request.user:
                context['msg'] = 'شما دسترسی ندارید'
                status_code = HTTP_400_BAD_REQUEST
                return Response(context, status=status_code)
            posts = Blog.objects.filter(q, owner=user, deleted=False, status=True)
            context['posts'] = BlogSerializer(posts, many=True).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

from .imports import *


class FriendsList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: FriendsViewDto(many=True)})
    def get(self, request):
        context = {}
        request_user_owner = RequestUser.objects.filter(owner=request.user, deleted=False, status=True).values('user_id')
        request_user_user = RequestUser.objects.filter(user=request.user, deleted=False, status=True).values('owner_id')
        request_user = request_user_owner.union(request_user_user, all=True)
        friends = User.objects.filter(id__in=request_user, is_active=True)
        context['friends'] = UserSafeSerializer(friends, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)


from .imports import *


class FriendsStoryList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: StoryViewDto(many=True)})
    def get(self, request):
        context = {}
        q = Q(privet=False) | Q(friends=request.user)
        stories = Story.objects.filter(q, owner__in=request.user.get_friends(request), deleted=False)
        context['stories'] = StorySerializer(stories, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

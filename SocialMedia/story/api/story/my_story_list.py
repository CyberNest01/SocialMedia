from .imports import *


class MyStoryList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: StoryViewDto(many=True)})
    def get(self, request):
        context = {}
        stories = Story.objects.filter(owner=request.user, deleted=False)
        context['stories'] = StorySerializer(stories, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

from .imports import *


class StorySingle(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=StoryViewDto, responses={200: StoryViewDto(many=False)})
    def post(self, request):
        context = {}
        story = Story(owner=request.user)
        story.privet = bool(request.data.get('privet'))
        story.title = request.data.get('title').strip()
        if 'story_file' in request.FILES:
            story.story_file = request.FILES['story_file']
        story.save()
        context['story'] = StorySerializer(story, many=False).data
        context['msg'] = 'ایجاد شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: StoryViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            q = Q(Q(owner__in=request.user.get_friends(request)) | Q(owner__privet=False) | Q(owner=request.user)) & Q(Q(
                privet=False) | Q(friends=request.user))
            story = Story.objects.get(q, id=pk, deleted=False)
            context['story'] = StorySerializer(story, many=False).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: StoryViewDto(many=False)})
    def delete(self, request, pk):
        context = {}
        try:
            story = Story.objects.get(id=pk, owner=request.user, deleted=False)
            story.delete()
            context['msg'] = 'حذف شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=GetFriendsStoryViewDto, responses={200: StoryViewDto(many=False)})
    def put(self, request, pk):
        context = {}
        try:
            story = Story.objects.get(id=pk, owner=request.user, deleted=False)
            if 'friends' in request.data:
                q = Q(id__in=list(request.data.get('friends'))) & Q(id__in=request.user.get_friends(request))
                friends = User.objects.filter(q)
                for friend in friends:
                    story.friends.add(friend)
                for friend in story.friends.all():
                    if friend not in friends:
                        story.friends.remove(friend)
                context['msg'] = 'تغیرات اعمال شد'
                status_code = HTTP_200_OK
            else:
                context['msg'] = 'دوستی انتخاب نشد'
                status_code = HTTP_400_BAD_REQUEST
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

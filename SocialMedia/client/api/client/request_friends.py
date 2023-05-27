from .imports import *


class RequestFriends(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=RequestUserViewDto, responses={200: RequestUserViewDto(many=False)})
    def post(self, request):
        context = {}
        try:
            if not request.user.id == int(request.data.get('user')):
                if RequestUser.objects.filter(owner=request.user, user_id=int(request.data.get('user')),
                                              deleted=False).exists():
                    context['msg'] = 'این درخواست قبلا ارسال شده است'
                    status_code = HTTP_400_BAD_REQUEST
                else:
                    request_user = RequestUser(owner=request.user)
                    request_user.user = User.objects.get(id=int(request.data.get('user')))
                    request_user.save()
                    request_user.friends()
                    context['request_user'] = RequestSerializer(request_user, many=False).data
                    context['msg'] = 'درخواست ارسال شد'
                    status_code = HTTP_200_OK
            else:
                context['msg'] = 'شما به خودتان نمیتوانید درخواست دهید'
                status_code = HTTP_400_BAD_REQUEST
        except:
            context['msg'] = 'کاربر یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: RequestUserViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            request_user = RequestUser.objects.get(owner=request.user, id=pk, deleted=False)
            context['request_user'] = RequestSerializer(request_user, many=False).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)




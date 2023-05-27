from .imports import *


class GetRequests(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: RequestUserViewDto(many=True)})
    def get(self, request):
        context = {}
        get_requests = RequestUser.objects.filter(user=request.user, deleted=False, status=False)
        context['get_requests'] = RequestSerializer(get_requests, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=RequestStatusViewDto, responses={200: RequestUserViewDto(many=False)})
    def put(self, request, pk):
        context = {}
        try:
            get_request = RequestUser.objects.get(id=pk, deleted=False, status=False)
            get_request.status = bool(int(request.data.get('status')))
            get_request.save()
            if get_request.status:
                get_request.set_friend()
                context['msg'] = 'تایید شد'
            else:
                get_request.delete()
                context['msg'] = 'رد شد'
            context['get_requests'] = RequestSerializer(get_request, many=False).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

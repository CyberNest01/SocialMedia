from .imports import *


class RequestsList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: RequestUserViewDto(many=True)})
    def get(self, request):
        context = {}
        request_list = RequestUser.objects.filter(owner=request.user, deleted=False, status=False)
        context['request_list'] = RequestSerializer(request_list, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

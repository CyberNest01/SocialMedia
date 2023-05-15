from .imports import *


class GetMe(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: ProfileViewDto(many=False)})
    def get(self, request):
        context = {}
        context['get_me'] = UserSerializer(request.user, many=False).data
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

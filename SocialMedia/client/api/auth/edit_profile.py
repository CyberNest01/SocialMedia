from .imports import *


class EditProfile(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=ProfileViewDto, responses={200: ProfileViewDto(many=False)})
    def put(self, request):
        context = {}
        request.user.first_name = request.data.get('first_name', request.user.first_name).strip()
        request.user.last_name = request.data.get('last_name', request.user.last_name).strip()
        request.user.email = request.data.get('email', request.user.email).strip()
        request.user.bio = request.data.get('bio', request.user.bio).strip()
        request.user.cellphone = request.data.get('cellphone', request.user.cellphone).strip()
        request.user.privet = bool(request.data.get('privet', request.user.privet))
        request.user.age = request.data.get('age', request.user.age)
        if 'image' in request.FILES:
            request.user.image = request.FILES['image']
        request.user.save()
        context['user'] = UserSerializer(request.user, many=False).data
        context['msg'] = 'با موفقیت ذخیره شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: ProfileViewDto(many=False)})
    def get(self, request):
        context = {}
        context['get_me'] = UserSerializer(request.user, many=False).data
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

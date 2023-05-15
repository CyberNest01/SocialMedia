from .imports import *


class ClientRegister(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=RegisterViewDto, responses={200: RegisterViewDto(many=False)})
    def post(self, request):
        context = {}
        if User.objects.filter(username=request.data.get('username')).exists():
            context['msg'] = 'نام کاربری وجود دارد !!!'
            status_code = HTTP_400_BAD_REQUEST
        else:
            if request.data.get('password') == request.data.get('re_password'):
                user = User(username=request.data.get('username'))
                user.set_password(request.data.get('password'))
                user.save()
                context['msg'] = 'با موفقیت انجام شد'
                status_code = HTTP_200_OK
            else:
                context['msg'] = 'تکرار رزمز اشتباه است !!!'
                status_code = HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)



from .imports import *


class ClientLogin(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=LoginViewDto, responses={200: TokenViewDto(many=False)})
    def post(self, request):
        context = {}
        try:
            user = User.objects.get(username=request.data.get('username'))
            user = authenticate(username=user.username, password=request.data.get('password'))
            if user:
                user.login(request)
                refresh = RefreshToken.for_user(user)
                context['access'] = str(refresh.access_token)
                context['refresh'] = str(refresh)
                context['msg'] = 'ورود با موفقیت انجام شد'
                status_code = HTTP_200_OK
            else:
                context['msg'] = 'رمز عبور اشتباه است'
                status_code = HTTP_404_NOT_FOUND
        except:
            context['msg'] = 'نام کاربری یافت نشد!!!'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)



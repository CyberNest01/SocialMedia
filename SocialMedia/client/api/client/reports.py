from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from .imports import *
from ..dto import ReportViewDto
from client.models import *
from ..serializers import ReportSerializer


class Reports(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=ReportViewDto, responses={200: ReportViewDto(many=False)})
    def post(self, request):
        context = {}
        if request.user.id != int(request.data.get('user')):
            try:
                report = Report(owner=request.user)
                report.user = User.objects.get(id=int(request.data.get('user')))
                report.text = request.data.get('text')
                report.save()
                report.report_user()
                context['report'] = ReportSerializer(report, many=False).data
                context['msg'] = 'ریپرت اعمال شد'
                status_code = HTTP_200_OK
            except:
                context['msg'] = 'کابر مورده نظر یافت نشد'
                status_code = HTTP_404_NOT_FOUND
        else:
            context['msg'] = 'شما خود را نمیتوانید ریپرت کنید'
            status_code = HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)

from django.db.models import Q

from .imports import *


class RemoveRequest(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: RequestUserViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            get_request = RequestUser.objects.filter(id=pk, deleted=False)
            if get_request[0].owner == request.user:
                q = Q(owner=request.user)
            elif get_request[0].user == request.user:
                q = Q(user=request.user)
            else:
                context['msg'] = 'یافت نشد'
                status_code = HTTP_404_NOT_FOUND
                return Response(context, status=status_code)
            get_request = get_request.get(q)
            context['get_request'] = RequestSerializer(get_request, many=False).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: RequestUserViewDto(many=False)})
    def delete(self, request, pk):
        context = {}
        try:
            get_request = RequestUser.objects.filter(id=pk, deleted=False)
            if get_request[0].owner == request.user:
                q = Q(owner=request.user)
            elif get_request[0].user == request.user:
                q = Q(user=request.user)
            else:
                context['msg'] = 'یافت نشد'
                status_code = HTTP_404_NOT_FOUND
                return Response(context, status=status_code)
            get_request = get_request.get(q)
            if not get_request.status:
                get_request.delete()
            else:
                get_request.remove_friend()
                get_request.delete()
            context['msg'] = 'حذف شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)




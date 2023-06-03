from .imports import *


class CategoryList(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: CategoryViewDto(many=True)})
    def get(self, request):
        context = {}
        q = Q()
        if 'name' in request.GET:
            q = q & Q(name__icontains=request.GET.get('name'))
        if 'parent' in request.GET:
            try:
                parent = Category.objects.get(id=int(request.GET.get('parent')))
                child = parent.get_children()
                q = q & Q(id__in=child)
            except:
                pass
        categories = Category.objects.filter(q).order_by(request.GET.get('order_by', '-id'))
        context['categories'] = CategorySerializer(categories, many=True).data
        context['msg'] = 'دریافت شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)


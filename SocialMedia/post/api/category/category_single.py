from .imports import *


class CategorySingle(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=CategoryViewDto, responses={200: CategoryViewDto(many=False)})
    def post(self, request):
        context = {}
        category = Category(name=request.data.get('name').strip())
        if 'parent' in request.data:
            try:
                category.parent = Category.objects.get(id=int(request.data.get('parent')))
            except:
                context['category_parent'] = 'همچین پرنتی یافت نشد'
        category.save()
        context['category'] = CategorySerializer(category, many=False).data
        context['msg'] = 'اضافه شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: CategoryViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            category = Category.objects.get(id=pk)
            context['category'] = CategorySerializer(category, many=False).data
            context['msg'] = 'دریافت شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=CategoryViewDto, responses={200: CategoryViewDto(many=False)})
    def put(self, request, pk):
        context = {}
        try:
            category = Category.objects.get(id=pk)
            category.name = request.data.get('name', category.name).strip()
            context['category'] = CategorySerializer(category, many=False).data
            context['msg'] = 'تغییرات اعمال شد'
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

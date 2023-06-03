from .imports import *


class PostSingle(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: BlogViewDto(many=False)})
    def get(self, request, pk):
        context = {}
        try:
            post = Blog.objects.get(id=pk, deleted=False, status=True)
            if not post.owner.privet or post.owner in request.user.get_friends(request) or post.owner == request.user:
                context['post'] = BlogSerializer(post, many=False).data
                context['msg'] = 'دریافت شد'
                status_code = HTTP_200_OK
            else:
                context['msg'] = 'شما دسترسی ندارید'
                status_code = HTTP_400_BAD_REQUEST
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=BlogViewDto, responses={200: BlogViewDto(many=False)})
    def post(self, request):
        context = {}
        post = Blog(owner=request.user)
        post.title = request.data.get('title').strip()
        post.description = request.data.get('description').strip()
        post.is_comment = bool(request.data.get('is_comment', True))
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        for category in request.data.get('category', []):
            post.category.add(category)
        context['post'] = BlogSerializer(post, many=False).data
        context['msg'] = 'اضافه شد'
        status_code = HTTP_200_OK
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: BlogViewDto(many=False)})
    def delete(self, request, pk):
        context = {}
        try:
            post = Blog.objects.get(id=pk, deleted=False, status=True)
            if post.owner == request.user:
                post.delete()
                context['msg'] = 'حذف شد'
                status_code = HTTP_200_OK
            else:
                context['msg'] = 'شما دسترسی ندارید'
                status_code = HTTP_400_BAD_REQUEST
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=BlogViewDto, responses={200: BlogViewDto(many=False)})
    def put(self, request, pk):
        context = {}
        try:
            post = Blog.objects.get(id=pk, status=True, deleted=False)
            if post.owner == request.user:
                post.title = request.data.get('title', post.title).strip()
                post.description = request.data.get('description', post.description).strip()
                post.is_comment = bool(request.data.get('is_comment', post.is_comment))
                if 'image' in request.FILES:
                    post.image = request.FILES['image']
                post.save()
                if 'category' in request.data:
                    categories = Category.objects.filter(id__in=list(request.data.get('category')))
                    for category in categories:
                        post.category.add(category)
                    for category in post.category.all():
                        if category not in categories:
                            post.category.remove(category)
                context['post'] = BlogSerializer(post, many=False).data
                context['msg'] = 'ذخیره شد'
                status_code = HTTP_200_OK
            else:
                context['msg'] = 'شما دسترسی ندارید'
                status_code = HTTP_400_BAD_REQUEST
        except:
            context['msg'] = 'یافت نشد'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

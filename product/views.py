from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @api_view(['GET'])
# def taskAll(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     if serializer.is_valid():
#         serializer.save()
# return Response(serializer.data)


# @api_view(['GET'])
# def taskDetail(request, pk):
#     try:
#         tasks = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return HttpResponse(status=404)
#     else:
#         serializer = TaskSerializer(tasks, many=False)
#         return Response(serializer.data)


# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         return Response({'error': 'Task don`t create because Content is empty.'})
#     return Response(serializer.data)


# @api_view(['PATCH'])
# def taskUpdate(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         context = serializer.data
#         return Response(context)
#     else:
#         context = {'error': f'{task} don`t update beacuse Content is empty.'}
#         return Response(context)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     context = {'delete': 'Succesfully deleted!'}
#     return Response(context)

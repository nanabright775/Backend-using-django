from rest_framework import viewsets
from .serielizers import ArticleSerielizers
from .models import Article
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerielizers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer()






# from rest_framework import mixins, generics
# from .serielizers import ArticleSerielizers
# from .models import Article


# class ArticleList(mixins.ListModelMixin, 
#                   mixins.CreateModelMixin, 
#                   generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerielizers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ArticleDetail(mixins.RetrieveModelMixin, 
#                     mixins.UpdateModelMixin, 
#                     mixins.DestroyModelMixin, 
#                     generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerielizers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)












# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serielizers import ArticleSerielizers
# from .models import Article
# from django.http import Http404

# #get all articles
# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerielizers(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerielizers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #get the detail for each article
# class ArticleDetail(APIView):
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             raise Http404
#             #return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
        

#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerielizers(article)
#         return Response(serializer.data)

#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerielizers(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response({'message': 'Article was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)















# from .serielizers import ArticleSerielizers
# from .models import Article
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status





# Create your views here.
# @api_view(['GET', 'POST'])
# def article_list(request):
#     #get all articles
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerielizers(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = ArticleSerielizers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# #the crud function 
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerielizers(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#        serializer = ArticleSerielizers(article, data=request.data)
#        if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response({'message': 'Article was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#     else:    
#         return Response({'message': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)     
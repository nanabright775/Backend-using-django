from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


# from django.urls import path
# from .views import ArticleList, ArticleDetail

# urlpatterns = [
#     path('articles/', ArticleList.as_view()),
#     path('articles/<int:pk>/', ArticleDetail.as_view()),
# ]


# from django.urls import path
# from .views import article_list, article_detail


# urlpatterns = [  
#     path('articles/',  article_list),
#     path('articles/<int:pk>/',  article_detail),
# ]
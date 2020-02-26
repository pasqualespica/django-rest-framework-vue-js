from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_api_view
from news.api.views import (ArticleListCreateAPIview, ArticleDetailAPIview,
                            JournalistListCreateAPIview)

# here define ENDPOINT ...
urlpatterns = [
    path('articles/', 
        ArticleListCreateAPIview.as_view(), 
        name="article-list"),

    path('articles/<int:pk>', 
        ArticleDetailAPIview.as_view(), 
        name="article-detail"),

    path('journalists/', 
        JournalistListCreateAPIview.as_view(), 
        name="journalist-list"),

    # path('articles/', article_list_create_api_view, name="article-list"),
    # path('articles/<int:pk>', article_detail_api_view, name="article-detail")
]
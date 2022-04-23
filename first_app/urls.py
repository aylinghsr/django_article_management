from . import views
from django.urls import path

app_name = 'first_app'

urlpatterns =[
    path('' , views.home , name='home'),
    path('api/' , views.api , name='api'),
    #path('article/<slug:slug>' , views.detail , name='detail'),
    path('article/<slug:slug>' , views.ArticleDetail.as_view() , name='detail'),
    #path('index/' , views.index , name='index'),
    path('index/' , views.ArticleList.as_view() , name='index'),
    #path('index/page/<int:page>' , views.index , name='index'),
    path('index/page/<int:page>' , views.ArticleList.as_view() , name='index'),
    #path('category/<slug:slug>' , views.category , name='category'),
    path('category/<slug:slug>' , views.CategoryList.as_view() , name='category'),
    #path('category/<slug:slug>/page/<int:page>' , views.category , name='category'),
    path('category/<slug:slug>/page/<int:page>' , views.CategoryList.as_view() , name='category'),
    path('author/<slug:username>' , views.AuthorList.as_view() , name='author'),
    path('author/<slug:username>/page/<int:page>' , views.AuthorList.as_view() , name='author'),
    path('preview/<int:pk>' , views.ArticlePreview.as_view() , name='preview'),
]
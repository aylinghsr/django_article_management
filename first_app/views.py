from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
#from django.contrib.auth.models import User
from account.models import User
from django.http import HttpResponse , JsonResponse
from django.views.generic import ListView , DetailView
from .models import Article , Category
from account.mixins import AuthorAccessMixin
# Create your views here.

def home(request):
    return HttpResponse('hello world!')

def api(request):
    data=({
        '1':{
            'first_name':'aylin',
            'last_name':'gheisar',
            'gender':'female',
        },
        '2': {
            'first_name': 'sara',
            'last_name': 'hofar',
            'gender': 'female',
        },
        '3': {
            'first_name': 'samira',
            'last_name': 'atashpaz',
            'gender': 'female',
        }
    })
    return JsonResponse(data)

'''
def yard(request):
    context = {
        'articles' :[
            {
            
            "title" : "The last airbender",
            "img":"https://occ-0-769-768.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABaZXpsqPMGJ3acEcZ5m6MCJaCnxq_zIwxNqRhJg6N7o2z4081gdrvluxPUaJriJEVLn7vjnjHjzFrFNlWFYfVYFQJck.jpg?r=b84",
            "description":"first cartoon",
                    },
            {
            "title": "The legend of Korra",
            "img": "https://occ-0-769-768.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABe40L8v0z2zhEWX36ZL5rIjcnHB6IiD2e0uUTMZL-lCiyk6a4aDHVAwWAZFW5fsjKlsRMqA3LdH8wUqFD_eLbKnZtnI.jpg?r=74c",
            "description": "second cartoon",
            },
            {
            "title": "Tailes of ladybug",
            "img": "https://occ-0-769-768.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABSrdAOVY1191WQgHm2B4BitRe_0uZN5jgi9GYcaKIl1ElzF2nCPZWrGFSHFmhByUvQncQQyubwu6GxIJxmcAQ1o3Tg4.jpg?r=718",
            "description": "third cartoon",
            },
            ]
        }
    return render(request, 'first_app/yard.html' , context)
    
'''


'''
def index(request , page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 4)
    #page = request.GET.get('page')    <!-- I commented this , because I made some changes in urls and add page=1 to def index -->
    articles = paginator.get_page(page)
    context = {
        'articles':articles ,
        # 'articles': Article.objects.all()
        #'articles': Article.objects.filter(status='p').order_by('-publish')[:3],
        #'articles': Article.objects.published()
        #'category': Category.objects.filter(status=True)       # I used base_tags.py and category_navbar.html
    }
    return render(request, 'first_app/base.html', context)

'''

class ArticleList(ListView):                               #context = object_list
    # model = Article   # it shows article.all
    queryset = Article.objects.published()
    template_name = 'first_app/list.html'
    #context_object_name = 'articles'
    paginate_by = 4


'''
def detail(request , slug):
    context = {
        'article': get_object_or_404(Article.objects.published() , slug=slug ,status='p')
    }
    return render(request, 'first_app/detail.html', context)
'''
class ArticleDetail(DetailView):                                    #context = object
    def get_object(self):
        slug = self.kwargs.get('slug')
        #return get_object_or_404(Article.objects.published() , slug=slug)
        article = get_object_or_404(Article.objects.published() , slug=slug)
        ip_address = self.requset.user.ip_address
        if ip_address not in article.hits.all():
            return article
    template_name = 'first_app/detail.html'

class ArticlePreview(AuthorAccessMixin , DetailView):  # context = object
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

    template_name = 'first_app/detail.html'
'''
def category(request , slug , page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 4)
    articles = paginator.get_page(page)
    context = {
    #'category': get_object_or_404(Category , slug=slug ,status=True)
    'category' : category ,
    'articles' : articles
    }
    return render(request, 'first_app/list.html', context)

'''


class CategoryList(ListView):                                  #context = object_list
    paginate_by = 3
    template_name = 'first_app/category.html'

    def get_queryset(self):
        global category                # in motaghayyer dar kharej az tabe ghabele estefade bashad
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active() , slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context



class AuthorList(ListView):                                  #context = object_list
    paginate_by = 3
    template_name = 'first_app/author_list.html'

    def get_queryset(self):
        global author                # in motaghayyer dar kharej az tabe ghabele estefade bashad
        username = self.kwargs.get('username')
        author = get_object_or_404(User , username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context



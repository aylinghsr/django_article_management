from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
#from django.contrib.auth.models import User
from account.models import User
from extensions.utils import jalali_converter

from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

# Create your models here.

# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")



class Category(models.Model):
    parent = models.ForeignKey('self' , default=None , blank=True , null=True , on_delete=models.SET_NULL , related_name='children' , verbose_name='زیردسته')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"
        ordering = ['parent__id','position']
    def __str__(self):
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES={
        ('d' , 'پیش نویس'),      # draft
        ('p' , 'منتشر شده'),     # publish
        ('i', 'در حال بررسی'),   # investigation
        ('b', 'برگشت داده شده'), # back
    }
    author = models.ForeignKey(User , null=True , on_delete=models.SET_NULL , related_name='articles' , verbose_name="نویسنده")
    title = models.CharField(max_length = 200 ,verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100 , unique=True,verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category , verbose_name='دسته بندی' , related_name='articles')
    description = models.TextField(verbose_name='موضوع مقاله')
    thumbnail = models.ImageField(upload_to="images",verbose_name='تصویر ')
    publish = models.DateTimeField(default=timezone.now,verbose_name='زمان ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name='مقاله ویژه')
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES,verbose_name='وضعیت')
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress , blank=True , related_name="hits" , verbose_name="بازدیدها")


    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"


    #def category_published(self):
        #return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 10px' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس مقاله"

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])

    category_to_str.short_description = "زمان دسته بندی"

    objects = ArticleManager()


    def get_absolute_url(self):
        return reverse('account:home')


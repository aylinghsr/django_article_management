from django.contrib import admin
from .models import Article , Category , IPAddress
# Register your models here.

# admin.site.disable_action('delete_selected')         # hazfe ghesmate hazfe maghalate montasher shode

# admin header change
admin.site.site_header = "وبلاگ"

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1 :
        message_bit = "منتشر شد."
    else :
        message_bit = "منتشر شدند."
    modeladmin.message_user(request , "{} مقاله {}".format(rows_updated , message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "پیش نویس شد."
    else:
        message_bit = "پیش نویس شدند."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_draft.short_description = "پیش نویس مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    fields = ['parent' ,'title' , 'slug' , 'status' , 'position' ]
    list_display = ('title' , 'slug' , 'status' , 'position' , 'parent')
    list_filter = (['status'])      # in models.py , status is a boolean field , so we should change it to list
    search_fields = (['title'])
    prepopulated_fields = {'slug':('title',)}   # auto fill slug

admin.site.register(Category , CategoryAdmin)




class ArticleAdmin(admin.ModelAdmin):
    fields = ['title' ,  'slug' , 'author', 'status','publish' , 'thumbnail' , 'description' , 'category']
    list_display = ('title' ,'thumbnail_tag', 'slug' , 'author' , 'jpublish', 'is_special' , 'status' , 'category_to_str')
    list_filter = ('publish' , 'status')
    search_fields = ('title' , 'description')
    prepopulated_fields = {'slug':('title',)}   # auto fill slug
    ordering = ['status' , '-publish']
    actions = [make_published , make_draft]


    '''
    def category_to_str(self , obj):
        return ", ".join([category.title for category in obj.category.active()])
    category_to_str.short_description = "زمان دسته بندی"
    '''

admin.site.register(Article , ArticleAdmin)
admin.site.register(IPAddress)
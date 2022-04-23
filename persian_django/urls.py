"""persian_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include , re_path
from account.views import Login , Register , activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('django.contrib.auth.urls')),
    path('' , include('first_app.urls')),
    path('login/' , Login.as_view() , name='login'),
    path('register/' , Register.as_view() , name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('account/' , include('account.urls')),
    path('comment/', include('comment.urls')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]

# after adding MEDIA_URL and MEDIA_ROOT to settings , add these lines to the main url.py (because we want image to be shown on website)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
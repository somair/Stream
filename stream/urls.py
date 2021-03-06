"""stream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from tube.views import (home_view, category_view, login_view,search_view, logout_handler, 
                        register_view, about_view, video_play, categories_view, increase_like, 
                        upload_video, upload_view)
import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/?$', home_view, name="home"),
    url(r'^about', about_view, name="about"),
    url(r'^categories',categories_view, name="categories"),
    url(r'^index/(?P<video_id>[0-9]+)', increase_like, name="increase_like"),
    url(r'^upload', upload_view, name="upload_video"),
    url(r'^success',upload_video, name="upload_video_handler"),
    url(r'^play-video/(?P<title>.*)', video_play, name="play-video"),
    url(r'^login/', login_view, name="login"),
    url(r'^register/',register_view, name="signup"),
    url(r'^logout/', logout_handler, name="logout"),
    url(r'^search/', search_view, name="search"),
    url(r'^category/(?P<category>.*)', category_view, name='category')




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

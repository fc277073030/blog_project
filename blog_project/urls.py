#coding:utf-8
"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from blog.upload import upload_image
from django.conf.urls import url
from blog.views import *

urlpatterns = [
    # 映射到管理界面
    url(r'^admin/', include(admin.site.urls)),
    #配置用于处理图片上传的url映射
    url(r"^uploads/(?P<path>.*)$", \
                        #django.views.static.serve专门用于处理静态文件
                        "django.views.static.serve", \
                        #这里用到了settings中配置好的路径MEDIA_ROOT
                        {"document_root": settings.MEDIA_ROOT,}),
    #用于映射富文本编辑器的图片上传
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image,\
        name='upload_image'),
    #重构urls.py，把blog相关url放到blog之下
    # url(r'^', include('blog.urls')),

    url(r'^$', index, name='index'),
    # 映射到归档页面
    url(r'^archive/', archive, name='archive'),
    # 映射到文章页面
    url(r'^article/$', article, name='article'),
    # 映射到提交评论页面
    url(r'^comment/post/$', comment_post, name='comment_post'),
    # 映射到标签页面
    url(r'^tag/', tag, name='tag'),
    # 映射到分类页面
    url(r'^category/$', category, name='category'),
    # 登录注册注销
    url(r'^logout$', do_logout, name='logout'),
    url(r'^login$', do_login, name='login'),
    url(r'^reg$', do_reg, name='reg'),
]

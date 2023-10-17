"""
URL configuration for online_intepreter_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
]


# 这是我们的 URL 入口配置，我们直接将入口配置到具体的 URL 上。

#from django.conf.urls import include  # 引入需要用到的配置函数
# include 用来引入其他的 URL 配置。参数可以是个路径字符串，也可以是个 url 对象列表

from online_intepreter_app.views import APICodeView, APIRunCodeView, home, js, css  # 引入我们的视图函数
from django.views.decorators.csrf import csrf_exempt  # 同样的，我们不需要使用 csrf 功能。

# 注意我们这里的 csrf_exempt 的用法，这和将它作为装饰器使用的效果是一样的

# 普通的集合操作 API
generic_code_view = csrf_exempt(APICodeView.as_view(method_map={'get': 'list',
                                                                'post': 'create'}))  # 传入自定义的 method_map 参数
# 针对某个对象的操作 API_
detail_code_view = csrf_exempt(APICodeView.as_view(method_map={'get': 'detail',
                                                                'put': 'update',
                                                               'delete': 'remove'}))
# 运行代码操作 API
run_code_view = csrf_exempt(APIRunCodeView.as_view())
# Code 应用 API 配置
code_api = [
    re_path(r'^$', generic_code_view, name='generic_code'),  # 集合操作
    re_path(r'^(?P<pk>\d*)/$', detail_code_view, name='detail_code'),  # 访问某个特定对象
    re_path(r'^run/$', run_code_view, name='run_code'),  # 运行代码
    re_path(r'^run/(?P<pk>\d*)/$', run_code_view, name='run_specific_code')  # 运行特定代码
]
api_v1 = [re_path('^codes/', include(code_api))]  # API 的 v1 版本
api_versions = [re_path(r'^v1/', include(api_v1))]  # API 的版本控制入口 URL
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include(api_versions)),  # API 访问 URL
    re_path(r'^$', home, name='index'),  # 主页视图
    re_path(r'^js/(?P<filename>.*\.js)$', js, name='js'),  # 访问 js 文件，记得，最后没有 /
    re_path(r'^css/(?P<filename>.*\.css)$', css, name='css')  # 访问 css 文件，记得，最后没有 /
]


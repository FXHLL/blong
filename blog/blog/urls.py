"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse



# include()函数实际上就是返回一个元组：([], None, None)

# 第一个元素可以是一个列表，列表中盛放url()子路由配置；
# 第二个元素是app_name，可以为None;
# 第三个元素是namespace，需要反向生成url时，可根据需求填写

# 在全局的urls.py中使用include方法实现url映射分发。

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('users.urls','users'),namespace='users')),
    # path('',log),

    path('',include(('home.urls','home'),namespace='home')),
]
# 图片访问路由
from  django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
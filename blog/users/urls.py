#进行users子应用的视图路由
from django.urls import path
from users.views import RegisterView,ImageCodeView
from users.views import SmsCodeView,LoginView
from users.views import LogoutView,ForgetPasswordView
from users.views import UserCenterView,WriteBlogView
urlpatterns = [
    #path第一个参数:路由,path第二个参数:视图函数名

    # 正则表达式：一个正则表达式字符串
    # views视图：一个可调用对象，通常为一个视图函数
    # 参数：可选的要传递给视图函数的默认参数（字典形式）
    # 别名：一个可选的name参数
    # django类视图as_view()方法解析
    # 使用视图函数时，django完成URL解析之后，会直接把request对象以及URL解析器捕获的参数
    # （比如re_path中正则表达捕获的位置参数或关键字参数）丢给视图函数，
    # 但是在类视图中，这些参数不能直接丢给一个类，所以就有了as_view方法
    # ，这个方法只做一件事就是返回一个闭包，这个闭包像视图函数一样接收url解析器传送过来的参数。
    #  django类视图as_view()方法详细：     https://www.cnblogs.com/olivertian/p/11072528.html
    path('register/',RegisterView.as_view(),name='register'),
    # 图片验证码路由
    path('imagecode/',ImageCodeView.as_view(),name='imagecode'),
    # 短信路由
    path('smscode/',SmsCodeView.as_view(),name='smscode'),
    #登陆路由
    path('login/',LoginView.as_view(),name='login'),
    # 退出登录
    path('logout/', LogoutView.as_view(), name='logout'),
    # 忘记密码
    path('forgetpassword/',ForgetPasswordView.as_view(),name='forgetpassword'),
    # 个人中心
    path('center/', UserCenterView.as_view(), name='center'),
    # 写博客
    path('writeblog/', WriteBlogView.as_view(), name='writeblog'),
]
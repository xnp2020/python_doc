"""定义app_blogs的URL模式"""

from  django.urls import path

from . import views

app_name = 'app_blogs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 修改post
    path('post/<int:post_id>/', views.post_edit, name='post_edit'),
    # 新增post
    path('post/add/', views.post_add, name='post_add'),
]
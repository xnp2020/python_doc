"""应用users的URL模式"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # 默认的身份验证URL
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]
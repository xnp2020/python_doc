from multiprocessing import context
from django.shortcuts import render,redirect

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """blog的主页"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'app_blogs/index.html', context)

def post_edit(request, post_id):
    """编辑post"""
    single_post = BlogPost.objects.get(id=post_id)


    if request.method != 'POST':
        # 初次请求： 使用当前条目的填充表单
        form = BlogPostForm(instance=single_post)
    else:
        # POST提交的数据： 对数据进行处理
        form = BlogPostForm(instance=single_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:index')

    context = {'single_post': single_post, 'form': form}
    return render(request, 'app_blogs/post_edit.html', context)

def post_add(request):
    """添加新post"""
    if request.method != 'POST':
        # 未提交数据： 创建一个新表单
        form = BlogPostForm()
    else:
        # POST提交的数据： 对数据进行处理
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_blogs:index')

    # 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request, 'app_blogs/post_add.html', context)
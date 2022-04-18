from django import forms

from .models import BlogPost

  
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'text': 'post_content', 'title': 'post_title'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
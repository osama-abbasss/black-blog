from django import forms
from . import models
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    content = RichTextField()
    class Meta:
        model = models.Post
        fields = ('user', 'title', 'content', 'image')


class PostEditForm(forms.ModelForm):
    content = RichTextField()
    class Meta:
        model = models.Post
        fields = ('title', 'content', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('user', 'text')
from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'posts'


urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^create/$', views.CreatePost.as_view(), name='create_post'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.UpdatePost.as_view(), name='edit_post'),
    re_path(r'(?P<pk>\d+)/delete/$', views.DeletePost.as_view(), name='delete_post'),
    re_path(r'about/$', views.About.as_view(), name='about'),
    re_path(r'(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment')

]

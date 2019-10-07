from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'posts'


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^create/$', views.CreatePost.as_view(), name='create_post'),
    url(r'^(?P<pk>\d+)/edit/$', views.UpdatePost.as_view(), name='edit_post'),
    url(r'(?P<pk>\d+)/delete/$', views.DeletePost.as_view(), name='delete_post'),
    url(r'about/$', views.About.as_view(), name='about'),
    url(r'(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment')

]
from django.urls import path

from blog_api import views

urlpatterns = [
    path('all', views.get_all_post),
    path('add', views.add_post),
    path('<int:post_id>', views.get_post),
    path('<int:post_id>/delete', views.delete_post),
    path('<int:post_id>/comment', views.add_comment),
    path('<int:post_id>/comment/all', views.get_all_comment),
]
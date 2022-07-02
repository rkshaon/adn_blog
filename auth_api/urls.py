from django.urls import path

from auth_api import views

urlpatterns = [
    path('registration', views.user_registration),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('profile', views.user_profile),
    path('all', views.get_all_user),
    path('<int:user_id>/delete', views.delete_user),
]
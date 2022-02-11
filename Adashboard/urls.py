from django.urls import path

from Adashboard import views

urlpatterns = [
    path('',views.dashboard,name='Adashboard'),
    path('users', views.show_users, name='users'),
    path('posts', views.show_post, name='posts'),
    path('deletePost/<int:p_id>', views.delete_post),

]

from django.urls import path
from blogapp import views

app_name="blog"
urlpatterns = [
    #path("", views.home, name="home")
    path("",views.PostListView.as_view(),name="home"),
    path("post/<int:pk>/", views.PostDetailView.as_view(),name="detail"),
    path("post-create/", views.PostCreateView.as_view(),name="create"),
    path("post-edit/<int:pk>",views.PostUpdateView.as_view(),name="edit"),
    path("post-delete/<int:pk>/",views.PostDeleteView.as_view(),name="delete"),
    path("post/<str:username>/",views.AuthorPostView.as_view(),name="user-posts")   
]
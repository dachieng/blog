from django.shortcuts import redirect, render
from blogapp.models import Post
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def home(request):
    posts = Post.objects.all()
    return render(request,"blogapp/home.html", {"posts":posts})


# ListView to list all the objects of the Post model
class PostListView(ListView):
    model = Post
    template_name = "blogapp/home.html"
    context_object_name = "posts"
    ordering = ['-date_created']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

class PostCreateView(CreateView):
    model=Post
    fields = ['title','content']

    def form_valid(self,form):
        #set the author of the form to current loggd in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    # set the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

   # test if the current user is the author of the post
    def test_func(self):
    # get the current post
        post = self.get_object()

        #check
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post

    # check if the current user is the one dleting the post
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

# list posts created by a specific user
class AuthorPostView(ListView):
    model = Post
    template_name = "blogapp/author_posts.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_created")
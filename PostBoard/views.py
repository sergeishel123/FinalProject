from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,TemplateView
from .models import Post,Category,Author,PostCategory,Comment
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostLists(LoginRequiredMixin,ListView):
    model = Post

    template_name = 'post_list.html'

    ordering = 'time_in'

    context_object_name = 'posts'

    paginate_by = 3

class PostDetail(DetailView):
    model = Post

    template_name = 'post_detail.html'

    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categor'] = PostCategory.objects.get(post = self.object).category
        return context


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post

    template_name = 'post_create.html'

    form_class = PostForm

    def post(self,request,*args,**kwargs):
        post = self.request.POST
        author_post,heading,text,category = request.user.id,post['heading'],post['text'],post['category']
        New = Post(author_post = Author.objects.get(user = author_post),heading = heading, text = text,)
        New.save()
        Categor = Category.objects.get(name = category)
        PostCategory.objects.create(post = New,category = Categor)
        return redirect(New.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post

    template_name = 'post_edit.html'

    form_class = PostForm

@login_required
def all_categories(request):
    context = {}
    context['categories'] = Category.objects.all()
    return render(request,'categories.html',context)


class PersonalView(TemplateView):
    template_name = 'protect/personal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(user = self.request.user.id)
        return context

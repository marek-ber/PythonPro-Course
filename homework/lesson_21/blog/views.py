from django.shortcuts import render
from .models import Post
from .forms import SearchForm
from django.db.models import Q

# Create your views here.

def category_posts(request, category_id):
    
    posts = Post.objects.filter(category=category_id)

    

    return render(request, 'blog/category_post.html', {'posts': posts})

def home(request):
    
    form = SearchForm(request.GET or None)
    posts = Post.objects.all()
    
    if form.is_valid():
        phrase = form.cleaned_data['phrase']
        posts = Post.objects.filter(Q(title__icontains=phrase)| 
                                    Q(content__icontains=phrase))
    
    # SELECT * FROM products WHERE category_id = category_id AND title = 'Zdrowie"

    
    # SELECT * FROM products WHERE title ilike '%phrase%' OR content ilike '%phrase%'
    # posts = Post.objects.order_by("-published_date")[0:5]

    return render(request, 'blog/home.html', {"posts": posts, "form": form})
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Blogs, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

def posts_by_category(request, category_id):
    # Fetch the category by its ID
    category = get_object_or_404(Category, pk=category_id)

    # Fetch all blogs that belong to the given category
    posts = Blogs.objects.filter(category=category)

    # Check if posts exist
    if not posts.exists():
        return HttpResponse(f"No posts found in category {category.category_name}")

    # Pass context to the template
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
#blogs
def blogs(request,slug):
   single_post= get_object_or_404(Blogs,slug=slug,status='published')
   context={
    'single_post':single_post
   }
   return render(request,'blogs.html',context)

   #search Functionality
def search(request):
    keyword=request.GET.get('keyword')

    blogs = Blogs.objects.filter(
    Q(title__icontains=keyword) |
    Q(short_description__icontains=keyword) |
    Q(blog_body__icontains=keyword),
    status='published'
)
    content={
        'blogs':blogs,
        'keyword':keyword
    }
  
    return render(request,'search.html',content)


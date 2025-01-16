# blogs/context_processors.py
from .models import Category

def get_category(request):
    # Fetch all categories or modify as per your need
    categories = Category.objects.all()  # Fetching all categories
    return {'categories': categories}

from django.shortcuts import render

from solemne.models import Brand, Category, Product

def category(request,category_id):

    products = Product.objects.filter(category__id=category_id, status=1)

    return render(request, 'category.html', {'products':products})
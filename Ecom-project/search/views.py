from django.shortcuts import render
from shop.models import Products
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Products.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})
from django.shortcuts import render,get_object_or_404
from store.models import Product
def homepage(request):
    product = Product.objects.all()
    return render(request,"core/homepage.html",{
        "products":product
    })
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Product,Category
from .forms import ProductForm
from userprofile.models import Userprofile,Vendor
from django.utils.text import slugify
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def isvendor(user):
    return user.userprofile.is_vendor
@user_passes_test(isvendor)
def createProduct(request):
    if not request.user.is_authenticated:
        return redirect("Login")
    try:
        if not request.user.userprofile.is_vendor:
            return redirect("homepage")
    except Userprofile.DoesNotExist:
        return redirect("homepage")
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid:
            tittle = request.POST.get("tittle")
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(tittle)
            product.save()
            return redirect("dashboard")
    else:
        form = ProductForm()
    return render(request,"store/addproduct.html",{
        "form":form,
        "tittle":"ADDPRODUCT"
    })
@user_passes_test(isvendor)
def editproduct(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid:
            form.save()
            return redirect("dashboard")
    else:
        form = ProductForm(instance=product)
    return render(request,"store/addproduct.html",{
        "form":form,
        "tittle":"EDIT-PRODUCT",
        "product":product       
    })
@user_passes_test(isvendor)
def deleteproduct(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.delete()
    return redirect("dashboard")
def product_detail(request,category_slug,slug):
    product = get_object_or_404(Product,slug=slug)
    product.video_count += 1
    product.save()
    return render(request,"store/productdetail.html",{
        "product":product,
    })
def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    product = category.products.all()
    return render(request,"store/categorydetail.html",{
        "products":product
    })
def search(request):
    query = request.GET.get("query","")
    products = Product.objects.filter(Q(tittle=query)|Q(description = query))
    return render(request,"store/search.html",{
        "query":query,
        "products":products
    })

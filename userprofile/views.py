from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Profile,Userprofile,Vendor
from .forms import CreateUserForm,ProfileForm,VendorForm
from django.contrib.auth import login
from django.contrib import messages
from store.models import Product
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.http import JsonResponse
def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            
            if Userprofile.objects.filter(user__email=email).exists():
                return render(request, "userprofile/signup.html", {"form": form, "error": "Email already used."})
            
            if Userprofile.objects.filter(user__username=username).exists():
                return render(request, "userprofile/signup.html", {"form": form, "error1": "Username already used."})
            
            user = form.save()
            userprofile = Userprofile.objects.create(user=user)
            login(request, user)
            return redirect("homepage")
    else:
        form = CreateUserForm()
    return render(request,"userprofile/signup.html",{"form":form}) 
@login_required
def account(request,id):
    profile = Profile.objects.filter(user=request.user).get(id=id)
    user = request.user
    if user.is_authenticated:
        try:
            vendor = Vendor.objects.get(user=user)
            is_vendor = True
        except Vendor.DoesNotExist:
            is_vendor = False
    else:
        is_vendor = False
    return render(request,"userprofile/account.html",{
        "profiles":profile,
        "is_vendor":is_vendor,
    })
@login_required
def edit_account(request,pk):
    profile = Profile.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request,"profile updated")
            return redirect("homepage")
    else:
        form = ProfileForm(instance=profile)
    return render(request,"userprofile/editaccount.html",{"form":form})
@login_required
def apply_vendor(request,id):
    if Vendor.objects.filter(user=request.user).exists():
        message = messages.success(request,"user under review")
        return redirect('account',id=id)
    if request.method == 'POST':
        form = VendorForm(request.POST,request.FILES)
        if form.is_valid:
            vendor_instance = form.save(commit=False)
            vendor_instance.user = request.user
            vendor_instance.status = Vendor.SUBMITTED
            vendor_instance.save()
            return redirect("homepage")
    else:
        form = VendorForm()
    return render(request,"userprofile/vendorapplication.html",{
        "form":form
    })
def is_admin(user):
    return user.is_superuser
@user_passes_test(is_admin)
def admin_reveiew_vendors(request):
    vendors_to_review = Vendor.objects.filter(status=Vendor.SUBMITTED)
    return render(request,"userprofile/admin_review.html",{
        "vendors_to_review":vendors_to_review
    })
@user_passes_test(is_admin)
def deletevendor(request,vendor_id,action):
    try:
        vendor_instance = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return HttpResponse("vendor not found")
    if action == 'delete':
        if vendor_instance.status == Vendor.ACCEPTED:
            vendor_instance.user.userprofile.is_vendor = False
            vendor_instance.user.userprofile.save()
            vendor_instance.delete()
            return redirect("vendors")
        if vendor_instance.status == Vendor.SUBMITTED:
            vendor_instance.delete()
@user_passes_test(is_admin)
def vendors(request):
    vendors = Vendor.objects.filter(status=Vendor.ACCEPTED)
    return render(request,"userprofile/vendors.html",{
        "vendors":vendors
    })
@user_passes_test(is_admin)
def acceptedvendordetails(request,vendor_id):
    vendor = get_object_or_404(Vendor,id=vendor_id)
    return render(request,"userprofile/acceptedvendor.html",{
        "vendor":vendor
    })
@user_passes_test(is_admin)
def vendordetails(request):
    vendor = get_object_or_404(Vendor)
    return render(request,"userprofile/viewdetails.html",{
        "vendor":vendor
    })
@user_passes_test(is_admin)
def viewvendordetails(request,vendor_id,action):
    try:
        vendor_instance = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return HttpResponse("vendor not found",status=404)
    if action == 'accept':
        if vendor_instance.status == Vendor.SUBMITTED:
            vendor_instance.status = Vendor.ACCEPTED
            vendor_instance.user.userprofile.is_vendor = True
            vendor_instance.user.userprofile.save()
            vendor_instance.save()
        else:
            return HttpResponse("invalid action for current status")
    elif action == 'decline':
        if vendor_instance.status == Vendor.SUBMITTED:
            vendor_instance.status = Vendor.DECLINED
            vendor_instance.delete()
        else:
            return HttpResponse("invalid action for current user")
    else:
        return HttpResponse("invalid action",status=404)
    
    return redirect("reviewvendors")
def isvendor(user):
    return user.userprofile.is_vendor
@user_passes_test(isvendor)
def vendor_dashboard(request):
    products = request.user.products.all()
    return render(request,"userprofile/dashboard.html",{
        "products":products
    })
def vendor_detail(request,pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    return render(request,"userprofile/vendorsprofile.html",{
        "products":products
    })
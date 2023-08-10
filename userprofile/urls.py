from django.urls import path
from . import views
from django.contrib.auth import views as login
urlpatterns=[
    path("signup/",views.signup,name = "signup"),
    path("login/",login.LoginView.as_view(template_name="userprofile/login.html"),name="login"),
    path("logout/",login.LogoutView.as_view(),name="logout"),
    path("account/<int:id>/",views.account,name="account"),
    path("editprofile/<int:pk>/",views.edit_account,name='editaccount'),
    path("register_shop/<int:id>/",views.apply_vendor,name='apply'),
    path("admin_review_vendors/",views.admin_reveiew_vendors,name='reviewvendors'),
    path("view_reviewed_vendors/",views.vendordetails,name="vendordetails"),
    path("view_vendor_information/<int:vendor_id>/<str:action>/",views.viewvendordetails,name='acceptvendor'),
    path("delete_vendor/<int:vendor_id>/<str:action>/",views.deletevendor,name='deletevendor'),
    path("accepted_vendor_information/<int:vendor_id>/",views.acceptedvendordetails,name="acceptedvendor"),
    path("vendors/",views.vendors,name='vendors'),
    path("vendor_dashboard",views.vendor_dashboard,name="dashboard"),
    path("<int:pk>/",views.vendor_detail,name = 'vendordetail')
]
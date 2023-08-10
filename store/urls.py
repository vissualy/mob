from django.urls import path
from . import views
urlpatterns = [
    path('search/',views.search,name = 'search'),
    path("add-product/",views.createProduct,name='createproduct'),
    path("edit_product/<int:pk>/",views.editproduct,name='editproduct'),
    path("delete_product/<int:pk>/",views.deleteproduct,name='deleteproduct'),
    path("<str:category_slug>/<str:slug>",views.product_detail,name='productdetail'),
    path("<slug:slug>/",views.category_detail,name='categorydetail'),
]
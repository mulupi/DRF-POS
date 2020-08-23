from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.Brand, name="manages_brands"),
    path('body/', views.Body_type, name="manages_bodies"),
    path('models/', views.Bike_models, name="manages_bike_models"),
    path('partscategories/', views.Parts_cat, name="manages_partscats"),
    path('products/', views.Products, name="manages_products"),
    path('subcat/', views.Subcategory, name="manages_subcategories"),
    path('suppliers/', views.Suppliers, name="manages_suppliers"),
    path('supplies/', views.Supplies, name="manages_supplies"),
]
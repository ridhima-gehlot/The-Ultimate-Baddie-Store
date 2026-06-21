from django.urls import path
from products import views

urlpatterns=[
    path('', views.home_page, name='home_page'),
    path('western_outfits/', views.western_outfits, name='western_outfits'),
    path('traditional_outfits/', views.traditional_outfits, name='traditional_outfits'),
    path('accessories/', views.accessories, name='accessories'),
    path('daily_products/', views.daily_products, name='daily_products'),
    path('product/<int:id>/', views.product_details, name='product_details'),
]
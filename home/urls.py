from .views import *
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name = 'category'),
    path('brand/<slug>', BrandView.as_view(), name = 'brand'),
    path('search', SearchView.as_view(), name = 'search'),
    path('details/<slug>', ProductDetailView.as_view(),name = 'details'),
    path('signup', signup, name = "signup"),
    path('product_review/<slug>', product_review, name ='product_review'),
    path('cart/<slug>', cart, name = 'cart'),
    path('my_cart', CartView.as_view(), name = 'my_cart'),
    path('reduce_quantity/<slug>', decrease_quantity, name = 'reduce_cart'),
    path('delete_cart/<slug>', delete_cart, name = 'delete_cart'),



    # path('', home, name = 'home'),
    # path('contact', contact, name = 'contact'),
    # path('cart', cart, name = 'cart'),
    # path('checkout', checkout, name = 'checkout'),
    # path('login', login, name = 'login'),
    # path('my-account', my_account, name = 'my-account'),
    # path('product-detail', product_detail, name = 'product-detail'),
    # path('product-list', product_list, name = 'product-list'),
    # path('wishlist', wishlist, name = 'wishlist'),

]
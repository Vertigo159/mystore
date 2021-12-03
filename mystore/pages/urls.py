from django.urls import path
from pages.views import *


urlpatterns = [
    path("", home_page, name="home_page"),
    path("shop", shop_page, name="shop_page"),
    path("about", about_page, name="about_page"),
    path("shopping_cart", shopping_cart_page, name="shopping_cart_page"),
    path("checkout", checkout_page, name="checkout_page"),
    path("blog_details", blog_details_page, name="blog_details_page"),
    path("blog", blog_page, name="blog_page"),
    path("contacts", contacts_page, name="contacts_page"),
    path("category/<str:category_slug>/", get_category, name="get_category"),
    path("/<str:product_slug>/", product_details, name="product_details"),
]
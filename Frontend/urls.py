from django.urls import path
from Frontend import views

urlpatterns = [
    path('homepage/',views.homepage, name="homepage"),
    path('products/',views.products, name="products"),
    path('cat_product/<cat_name>',views.cat_product, name="cat_product"),
    path('single_product/<int:proid>/',views.single_product, name="single_product"),
    path('about_us_page/',views.about_us_page, name="about_us_page"),
    path('contact_us_page/',views.contact_us_page, name="contact_us_page"),
    path('service_page/',views.service_page, name="service_page"),
    path('save_contact/',views.save_contact, name="save_contact"),
    path('sign_page/',views.sign_page, name="sign_page"),
    path('register_page/',views.register_page, name="register_page"),
    path('userlogin/',views.userlogin, name="userlogin"),
    path('Userlogout/',views.Userlogout, name="Userlogout"),
    path('cart_page/',views.cart_page, name="cart_page"),
    path('save_cart/',views.save_cart, name="save_cart"),
    path('delete_cart_product/<int:dataid>/',views.delete_cart_product, name="delete_cart_product"),
    path('checkout/',views.checkout, name="checkout"),
]
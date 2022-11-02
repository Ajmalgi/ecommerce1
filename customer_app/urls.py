from django.urls import path
from . import views
app_name='customer'
urlpatterns = [
    path('home',views.home_page,name='home'),
    path('product',views.product_details,name='product'),
    path('cart',views.cart,name='cart'),
    path('orders',views.my_orders,name='orders'),
    path('password',views.password,name='password'),
    path('profile',views.profile,name='profile')


    
]

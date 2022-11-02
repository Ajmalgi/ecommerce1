from django.urls import path
from . import views
app_name='seller'
urlpatterns = [
    path('home2',views.seller_home,name='home2'),
    path('product',views.add_product,name='product'),
    path('catalogus',views.productcatalog,name='catalogus'),
    path('orders',views.my_orders,name='orders'),
    path('stock',views.update_stock,name='stock'),
    path('changepswd',views.change_password,name='changepswd'),
    path('profile',views.seller_profile,name='profile')
    
    
]

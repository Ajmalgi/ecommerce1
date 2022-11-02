from django.urls import path
from . import views
app_name='eadmin'
urlpatterns = [
    path('home3',views.eadmin,name='home3'),
    path('approve',views.approve_sellers,name='approve'),
    path('view',views.view_sellers,name='view'),
    path('viewcustomers',views.view_customers,name='viewcustomers'),
    path('changepassword',views.change_password,name='changepassword')
]
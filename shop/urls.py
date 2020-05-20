from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    url(r'^shopnow/',views.shop_now, name='shop_now'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]
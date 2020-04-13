from django.urls import path

from . import views

urlpatterns = [
    # path('product-list', views.ProductListAPIView.as_view(), name='product-list'),
    # path('user-list', views.UserListAPIView.as_view(), name='user-list'),
    path("invoice", views.InvoiceListAPIView.as_view(), name="invoice")
]

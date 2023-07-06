from django.urls import path
from .views import Base,ProductDetail
from .views import ProductList, ProductEdit, ProductDelete, ProductCreate,ProductSavat
urlpatterns = [
    path('create/', ProductCreate.as_view(), name = 'create'),
    path('', Base.as_view(), name='base'),
    path('<str:title>', ProductList.as_view(), name='product'),
    path('detail/<int:pk>', ProductDetail.as_view(), name = 'detail'),
    path('detail/<int:pk>/edit', ProductEdit.as_view(), name = 'edit'),
    path('detail/<int:pk>/delete', ProductDelete.as_view(), name = 'delete'),
    path('savat/', ProductSavat, name = 'savat'),
]
from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('addcategory/',views.addCategoryView,name='addcategory'),
    path('showcategory/',views.showCategoryView,name='showcategory'),
    path('deletecategory/<int:id>/',views.deleteCategoryView,name='deletecategory'),
    path('addproduct/',views.addProductView,name='addproduct'),
    path('showproduct/',views.showProductView,name='showproduct'),
    path('deleteproduct/<int:id>/',views.deleteProductView,name='deleteproduct'),
    path('updateproduct/<int:id>/',views.updateProductView,name='updateproduct'),
    path('storehome/',views.StoreHomeView.as_view(),name='storehome'),
    path('cart/',views.cartView,name='cart'),
    path('order/',views.orderView,name='order'),
    path('success/',views.successView,name='success'),

]

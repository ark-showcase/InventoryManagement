from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('yourDashboard/', views.yourDashboard, name="yourDashboard"),
    path('addSaleProduct/', views.addSaleProduct, name="addSaleProduct"),
    path('viewProduct/', views.viewProduct, name="viewProduct"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('deleteUpdate/<int:id>', views.deleteUpdate, name="deleteUpdate"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('excel/', views.excel, name="excel"),
    path('updateStock/', views.updateStock, name="updateStock"),
    path('selectSale/', views.selectSale, name="selectSale"),
    path('saleThis/<int:id>', views.saleThis, name="saleThis"),
    path('viewPurchase/', views.viewPurchase, name="viewPurchase"),
    path('shareCertificate/', views.shareCertificate, name="shareCertificate"),
    path('viewSaleReport/', views.viewSaleReport, name="viewSaleReport"),
    path('addMember/', views.addMember, name="addMember"),
    path('viewMember/', views.viewMember, name="viewMember"),
    path('addPurchase/', views.addPurchase, name="addPurchase"),
    path('addShareCertificate/', views.addShareCertificate, name="addShareCertificate"),
]

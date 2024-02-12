from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from production.views import ProductionInvoicePdfView, ProductionListView, SuppliesListView
from inventory.views import InventoryInvoicePdfView, ProductListView
from sales.views import SaleInvoicePdfView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('home/', views.home, name='home'),   
    path('ventas/', views.ventas, name='ventas'),
    path('rrhh/', views.rrhh, name='rrhh'),
    path('Postulacion/', views.Postulacion, name='Postulacion'),
    path('sugerencias/', views.sugerencias, name='sugerencias'),        
    path('sales/', views.sales, name='sales'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_jas'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),          
       
    path('sales/sale_invoice/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
    
    path('producto/', ProductListView.as_view(), name='producto'),
    path('inventory/inventory_invoice/', InventoryInvoicePdfView.as_view(), name='inventory_invoice_pdf'),   
    
    path('insumo/', SuppliesListView.as_view() ,name='insumo'),
    path('supplies/create_supplies/', views.createsupplies, name='create_supplies'),
    path('supplies/editar/<int:id>', views.editsupplies, name='edits_upplies'),
    path('supplies/eliminar/<id>/', views.deleteSupplies, name='eliminar_orden_pedido'),

    path('ordenpedido/', ProductionListView.as_view(), name='ordenpedido'),
    path('production/product_invoice/', ProductionInvoicePdfView.as_view(), name='production_invoice_pdf'),
    path('production/create_production_order/', views.create_production_order, name='create_production_order'),
    path('production/editar/<int:id>', views.editProductionOrder, name='editar_orden_pedido'),
    path('production/eliminar/<id>/', views.deleteProductionOrder, name='eliminar_orden_pedido')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

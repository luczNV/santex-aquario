from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='inicio'),
    path('productos/',views.producto,name='producto'),
    path('productos/<int:producto_id>/', views.producto_views, name='producto_views'),
    path('checkout/',views.checkout, name='checkout'),
    path('logout/',views.logout_view, name='logout'),
    path('carrito/', views.Carrito, name='carrito'),
    path('agregar-carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('cantidad-carrito/', views.global_carrito_cantidad, name='global_carrito_cantidad'),
    path('carrito/bajar/<int:item_id>/', views.bajar_cantidad, name='bajar_cantidad'),
    path('carrito/aumentar/<int:item_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('gracias/', views.gracias, name='gracias'),
]

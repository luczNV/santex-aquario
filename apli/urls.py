from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='inicio'),
    path('productos/',views.producto,name='producto'),
    path('carrito/', views.carrito, name='carrito'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
]

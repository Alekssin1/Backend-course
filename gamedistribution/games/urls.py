from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from games import views

urlpatterns = [
    path('contact/', views.app_render, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('search/', views.search_view, name='search'),
    path('', views.home, name= "home"),
    path('shop/<int:game_id>/', views.product, name= "product-details"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
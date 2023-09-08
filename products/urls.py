from django.urls import path

# /api/products/
from . import views
urlpatterns = [
    path('', views.product_mixin_view),
    path('<int:pk>/', views.product_mixin_view),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view())
]
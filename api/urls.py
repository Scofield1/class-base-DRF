from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>', views.ProductDetailApiView.as_view(), name='home')
]
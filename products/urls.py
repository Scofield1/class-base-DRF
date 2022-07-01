from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='name'),
    path('<str:pk>', views.BlogDetails.as_view())
]
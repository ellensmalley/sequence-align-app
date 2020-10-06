from django.urls import path
from . import views

urlpatterns = [
    path('api/protein/', views.ProteinListCreate.as_view() ),
]
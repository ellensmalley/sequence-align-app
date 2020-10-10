from django.urls import path
from . import views

urlpatterns = [
	path('api/requests/', views.RequestList.as_view()),
	path('api/requests/<int:pk>/', views.RequestDetail.as_view()),
	path('api/requests/<str:user>/', views.UserRequestList.as_view())
]
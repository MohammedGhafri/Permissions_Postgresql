from django.urls import path
from .views import DataList,DataDetails



urlpatterns = [
    path('', DataList.as_view(), name='data'), 
    path('<int:pk>/', DataDetails.as_view(), name='data_details') 
]
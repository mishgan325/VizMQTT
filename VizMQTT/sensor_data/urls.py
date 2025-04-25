# sensor_data/urls.py
from django.urls import path
from .views import SensorDataList, SensorDataDetail

urlpatterns = [
    path('sensor_data/', SensorDataList.as_view(), name='sensor_data_list'),
    path('sensor_data/<int:pk>/', SensorDataDetail.as_view(), name='sensor_data_detail'),
]

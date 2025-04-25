# sensor_data/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SensorDataList(APIView):
    def get(self, request):
        return Response({"message": "Получить все показания датчиков."}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "Добавить показание датчика."}, status=status.HTTP_201_CREATED)

class SensorDataDetail(APIView):
    def get(self, request, pk):
        return Response({"message": f"Получить показание датчика с ID {pk}."}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"message": f"Обновить показание датчика с ID {pk}."}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        return Response({"message": f"Удалить показание датчика с ID {pk}."}, status=status.HTTP_204_NO_CONTENT)

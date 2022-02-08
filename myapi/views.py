from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Track
from .serializers import Trackserializers
from rest_framework.decorators import api_view
from rest_framework import viewsets,status
from rest_framework.response import Response

class Tracklist(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class= Trackserializers
# class Trackviewset(viewsets.ModelViewSet):
#     queryset = Track.objects.all()
#     serializer_class= Trackserializers
@api_view(['GET', 'PUT', 'DELETE'])
def trackDetail(request, id):
    try:
        student = Track.objects.get(id=id)
    except Track.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Trackserializers(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Trackserializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
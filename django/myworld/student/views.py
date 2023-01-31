from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets , mixins , generics

# Create your views here.

class viewsets_techer(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserialzer


class MixsinsTracher(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserialzer


    def get(self , request ):
        return self.list(request)
    def post(self , request )    :
        return self.create(request)

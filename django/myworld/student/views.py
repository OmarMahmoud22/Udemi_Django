from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets , mixins , generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
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

class viewsets_Student(viewsets.ModelViewSet):
    queryset = StudintInfo.objects.all()
    serializer_class = StudentSerializerInfo


    


class viewsets_courses(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursSerializer

class viewsets_Categury(viewsets.ModelViewSet):
    queryset = CateguryOfCourse.objects.all()
    serializer_class = CatSerializer   

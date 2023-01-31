from rest_framework import serializers
from .models import *


class Teacherserialzer(serializers.ModelSerializer):
    class Meta:
     model = Teacher
     fields = '__all__'
    


class CatSerializer(serializers.ModelSerializer):
    class Meta:
     model = CateguryOfCourse
     fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
     model = StudintInfo
     fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
     model = Courses
     fields = ( 'id' , 'statue')


    
    
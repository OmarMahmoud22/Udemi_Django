from rest_framework import serializers
from .models import *


class Teacherserialzer(serializers.ModelSerializer):
    model = Teacher
    fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    model = CateguryOfCourse
    fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    model = StudintInfo
    fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    model = Courses
    fields = '__all__'


    
    
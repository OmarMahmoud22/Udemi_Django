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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    
  
class StudentSerializerInfo(serializers.ModelSerializer):
    his_course = serializers.StringRelatedField()

    class Meta:
        model = StudintInfo
        fields = ['his_course' , 'user' , 'age']    

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
     model = Courses
     fields = ( 'id' , 'statue' , 'nameofcours' ,'cat' , 'price' , 'rate' , 'slug', 'active' , 'language', 'what' )


    
    
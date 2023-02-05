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
     fields = ('id' , 'how_muchethis_course_have_this_student' , 'user' , 'age' , 'what' )

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
     model = Courses
     fields = ( 'id' , 'statue' , 'nameofcours' ,'cat' , 'price' , 'rate' , 'slug', 'active' , 'language' )


    
    
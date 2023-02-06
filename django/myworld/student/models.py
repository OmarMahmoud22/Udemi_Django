from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
from django.template.defaultfilters import slugify  
from django.conf.global_settings import LANGUAGES
from rest_framework import serializers

# Create your models here.

class StudintInfo(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    age = models.PositiveIntegerField()
    his_course = models.ManyToManyField("Courses" )


    def how_muchethis_course_have_this_student(self)     :
        return  self.his_course.count()

    def __str__(self):
        return str(self.user)


    #def what(self):
    #    his_course = serializers.StringRelatedField()
    #    return his_course
     

    
      


  
        
class CateguryOfCourse(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name

class Courses(models.Model):
    nameofcours =models.CharField(max_length=50)
    cat = models.ForeignKey( CateguryOfCourse , on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    rate = models.IntegerField(validators=[MaxValueValidator(5) , MinValueValidator(1)])
    slug = models.SlugField(null=True , blank=True)
    active = models.BooleanField()
    language = models.CharField(max_length=7, choices=LANGUAGES)
    #date = models.DateTimeField()
    

    def statue(self):
        if self.active == False:
            return "its not avilabel"
        elif self.active == True:
            return "avilabel"    
        return True    

    def __str__(self):
        return self.nameofcours

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.nameofcours)
        return super(Courses ,self).save(*args, **kwargs)    


    def what(self):
     stu = StudintInfo.objects.select_related('his_course').order_by('user')
     for x in stu:
        print(x.his_course)
        return str(x.his_course)


class Teacher(models.Model):
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    age = models.PositiveIntegerField()
    his_course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname



 







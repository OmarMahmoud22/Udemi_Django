from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
from django.template.defaultfilters import slugify  

# Create your models here.

class StudintInfo(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    age = models.PositiveIntegerField()
    his_course = models.ForeignKey("Courses", on_delete=models.CASCADE)

    

    def __str__(self):
        return str(self.user)


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
    
    def __str__(self):
        return self.nameofcours

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.nameofcours)
        return super(Courses ,self).save(*args, **kwargs)    

class Teacher(models.Model):
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    age = models.PositiveIntegerField()
    his_course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname





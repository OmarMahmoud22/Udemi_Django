# Generated by Django 4.1.5 on 2023-02-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_studintinfo_his_course_studintinfo_his_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studintinfo',
            name='his_course',
        ),
        migrations.AddField(
            model_name='studintinfo',
            name='his_course',
            field=models.ManyToManyField(to='student.courses'),
        ),
    ]

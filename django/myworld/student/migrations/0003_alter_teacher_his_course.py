# Generated by Django 4.1.5 on 2023-01-31 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_courses_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='his_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.courses'),
        ),
    ]

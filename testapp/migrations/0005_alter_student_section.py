# Generated by Django 4.2.1 on 2024-01-30 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_student_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='testapp.studentsection'),
        ),
    ]

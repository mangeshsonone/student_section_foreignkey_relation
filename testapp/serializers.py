from rest_framework import serializers
from .models import studentsection,student

class studentsection_serializer(serializers.ModelSerializer):
    students=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=studentsection
        fields=['id','section','students']
        
class student_serializer(serializers.ModelSerializer):
    section=serializers.StringRelatedField( read_only=True)
    class Meta:
        model=student
        fields=['id','name','section','rollno','address']
        


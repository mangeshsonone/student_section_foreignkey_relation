from django.shortcuts import render
from rest_framework.views import APIView
from .models import studentsection,student
from .serializers import studentsection_serializer,student_serializer
from rest_framework.response import Response



class student_secAPI(APIView):
    def get(self,request,id=None,format=None):
        id=id
        if id is not None:
            stusec=studentsection.objects.get(id=id)
            serializer=studentsection_serializer(stusec)
            print(serializer.data)
            return Response(serializer.data)
        
        stusec=studentsection.objects.all()
        serializer=studentsection_serializer(stusec,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=studentsection_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'data saved'})
        
        return Response(serializer.errors)
    
    def put(self,request,id=None,format=None):
        id=id
        stu=studentsection.objects.get(id=id)
        serializer=studentsection_serializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'data saved'})
        
        return Response(serializer.errors)
    
    def delete(self,request,id,format=None):
        id=id
        stu=studentsection.objects.get(id=id)
        stu.delete()
        return Response({'data':'data deleted'})
            
            
            
            
            
class student_API(APIView):
    def get(self,request,id=None,format=None):
        id=id
        if id is not None:
            stusec=student.objects.get(id=id)
            serializer=student_serializer(stusec)
            return Response(serializer.data)
        
        stusec=student.objects.all()
        serializer=student_serializer(stusec,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'data saved'})
        
        return Response(serializer.errors)
    
    def put(self,request,id=None,format=None):
        id=id
        stu=student.objects.get(id=id)
        serializer=student_serializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'data saved'})
        
        return Response(serializer.errors)
    
    def delete(self,request,id,format=None):
        id=id
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'data':'data deleted'})
            
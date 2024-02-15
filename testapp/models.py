from django.db import models

class studentsection(models.Model):
    section=models.CharField(max_length=100)
    
    def __str__(self):
        return self.section
    
    
class student(models.Model):
    name=models.CharField(max_length=70)
    section=models.ForeignKey(studentsection,on_delete=models.CASCADE,related_name='students')
    rollno=models.IntegerField()
    address=models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.name
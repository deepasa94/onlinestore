from django.db import models

# Create your models here.
books=[
   {"id": 100,"book_name":"randamoozham","author":"mt","price":480,"copies":250},
    {"id":101,"book_name": "aarachar", "author": "meera", "price": 580, "copies": 250},
    {"id":102,"book_name": "the alchemist", "author": "paulo", "price": 780, "copies": 250},
    {"id":103,"book_name": "rainrising", "author": "nirupama", "price": 1000, "copies": 250},
    {"id":104,"book_name": "indhuleka", "author": "chandhu menon", "price": 280, "copies": 250},
    {"id":105,"book_name": "pazhassy", "author": "mt", "price": 580, "copies": 350},

]
class Books(models.Model):
 book_name=models.CharField(max_length=120,unique=True)
 author=models.CharField(max_length=120)
 price=models.PositiveIntegerField()
 copies=models.PositiveIntegerField()
 published_date=models.DateField(null=True)
 image=models.ImageField(upload_to="images",null=True)
 def __str__(self):
   return self.book_name
class Employee(models.Model):
 employee_name=models.CharField(max_length=120)
 employee_desig=models.CharField(max_length=120)
 employee_exp=models.PositiveIntegerField()
 employee_salary=models.PositiveIntegerField()

 def __str__(self):
  return self.employee_name


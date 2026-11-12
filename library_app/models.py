# library_app/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField(default=5) # YE LINE ADD KARO
    
    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {self.student.name}"
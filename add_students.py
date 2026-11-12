import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
django.setup()
from django.contrib.auth.models import User
from library_app.models import Student
User.objects.filter(username__startswith='student').delete()
Student.objects.all().delete()
first_names = ["Aman","Nishant","Rahul","Priya","Anjali","Vikash","Sneha","Arjun","Pooja","Rohit","Karan","Neha","Amit","Simran","Deepak","Riya","Saurabh","Kavya","Mohit","Ishika"]
last_names = ["Singh","Sharma","Verma","Yadav","Gupta","Patel","Kumar","Barhela","Chaudhary","Mishra"]
courses = ["BCA","MCA","BTech","BSc CS","MSc"]
for i in range(1, 501):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    username = f"student{i:03d}"
    password = f"pass{i:03d}@123"
    User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
    Student.objects.create(name=f"{fname} {lname}", course=random.choice(courses))
print("500 Done! ex: student001 / pass001@123")

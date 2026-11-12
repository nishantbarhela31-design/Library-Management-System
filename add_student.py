import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
django.setup()

from django.contrib.auth.models import User
from library_app.models import Student

# Purana data delete
User.objects.filter(username__startswith='student').delete()
Student.objects.all().delete()

first_names = ["Aman","Nishant","Rahul","Priya","Anjali","Vikash","Sneha","Arjun","Pooja","Rohit","Karan","Neha","Amit","Simran","Deepak","Riya","Saurabh","Kavya","Mohit","Ishika","Yash","Tanya","Harsh","Muskan","Aditya","Shreya","Sumit","Divya","Sachin","Komal"]
last_names = ["Singh","Sharma","Verma","Yadav","Gupta","Patel","Kumar","Barhela","Chaudhary","Mishra","Jain","Saini","Thakur","Rathore","Meena","Khan"]
courses = ["BCA","MCA","BTech","BSc CS","MSc","BBA","MBA"]

for i in range(1, 501):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    full_name = f"{fname} {lname}"
    username = f"student{i:03d}"
    password = f"pass{i:03d}@123"  # ex: pass001@123
    course = random.choice(courses)

    # 1. Django User banao
    user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
    
    # 2. Student profile banao
    Student.objects.create(name=full_name, course=course)

    if i % 100 == 0:
        print(f"{i} created...")

print("Done! 500 Students + Users Created!")
print("Example Login -> username: student001 / password: pass001@123")
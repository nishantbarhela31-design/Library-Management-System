import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
django.setup()
from library_app.models import Book
Book.objects.all().delete()
books = [
    ("Python Programming", "Guido van Rossum", 10),
    ("Machine Learning", "Andrew Ng", 5),
    ("Data Science Handbook", "Jake VanderPlas", 7),
    ("Deep Learning", "Ian Goodfellow", 3),
    ("Java Complete", "Herbert Schildt", 12),
    ("C Programming", "Dennis Ritchie", 8),
    ("Django", "William Vincent", 6),
    ("AI", "Stuart Russell", 4),
    ("Computer Networks", "Tanenbaum", 9),
    ("DBMS", "Korth", 10),
]
for t,a,q in books:
    Book.objects.create(title=t, author=a, quantity=q)
print("10 Books Added!")
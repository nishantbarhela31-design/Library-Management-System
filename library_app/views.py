from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Student, Issue

def home(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    issues = Issue.objects.filter(is_returned=False)
    return render(request, 'home.html', {'books': books, 'issues': issues})

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            quantity=request.POST['quantity']
        )
        return redirect('/')
    return render(request, 'add_book.html')

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], course=request.POST['course'])
        return redirect('/')
    return render(request, 'add_student.html')

def issue_book(request):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=request.POST['book'])
        if book.quantity > 0:
            Issue.objects.create(book=book, student_id=request.POST['student'])
            book.quantity -= 1
            book.save()
        return redirect('/')
    return render(request, 'issue_book.html', {'books': Book.objects.all(), 'students': Student.objects.all()})

def return_book(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    issue.book.quantity += 1
    issue.book.save()
    issue.is_returned = True
    issue.save()
    return redirect('/')
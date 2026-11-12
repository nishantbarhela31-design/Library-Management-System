from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-student/', views.add_student, name='add_student'),
    path('issue-book/', views.issue_book, name='issue_book'),
    path('return/<int:issue_id>/', views.return_book, name='return_book'),
]
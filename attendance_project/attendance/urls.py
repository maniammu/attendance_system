from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
path(
    'attendance-report/',
    views.attendance_report,
    name='attendance_report'
),
path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path(
    'attendance-percentage/',
    views.attendance_percentage,
    name='attendance_percentage'
),
path(
    'monthly-report/',
    views.monthly_report,
    name='monthly_report'
),
path(
    'export-csv/',
    views.export_csv,
    name='export_csv'
),
path(
    'student-history/<int:id>/',
    views.student_history,
    name='student_history'
),
path(
    'teacher-list/',
    views.teacher_list,
    name='teacher_list'
),
]
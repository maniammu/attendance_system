from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from .forms import StudentForm, AttendanceForm
from .models import Student, Attendance
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from datetime import date
from .models import Student, Attendance

from datetime import date

def dashboard(request):

    total_students = Student.objects.count()

    present_today = Attendance.objects.filter(
        date=date.today(),
        status='Present'
    ).count()

    absent_today = Attendance.objects.filter(
        date=date.today(),
        status='Absent'
    ).count()

    context = {
        'total_students': total_students,
        'present_today': present_today,
        'absent_today': absent_today,
    }

    return render(
        request,
        'dashboard.html',
        context
    )
def student_list(request):

    search = request.GET.get('search')

    students = Student.objects.all()

    if search:
        students = students.filter(
            name__icontains=search
        )

    return render(
        request,
        'student_list.html',
        {'students': students}
    )


def add_student(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/students/')

    return render(request, 'add_student.html', {
        'form': form
    })
def mark_attendance(request):

    form = AttendanceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/attendance-report/')

    return render(request,
                  'mark_attendance.html',
                  {'form': form})
def attendance_report(request):

    records = Attendance.objects.all().order_by('-date')

    return render(
        request,
        'attendance_report.html',
        {'records': records}
    )
from django.shortcuts import render, redirect, get_object_or_404

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    form = StudentForm(
        request.POST or None,
        instance=student
    )

    if form.is_valid():
        form.save()
        return redirect('/students/')

    return render(
        request,
        'edit_student.html',
        {'form': form}
    )


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/students/')
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login/')
from .models import Student, Attendance

@login_required
def attendance_percentage(request):

    students = Student.objects.all()

    data = []

    for student in students:

        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status='Present'
        ).count()

        percentage = 0

        if total > 0:
            percentage = round(
                (present / total) * 100,
                2
            )

        data.append({
            'student': student,
            'total': total,
            'present': present,
            'percentage': percentage
        })

    return render(
        request,
        'attendance_percentage.html',
        {'data': data}
    )
from django.db.models import Q

@login_required
def monthly_report(request):

    month = request.GET.get('month')

    records = Attendance.objects.all()

    if month:
        records = records.filter(date__month=month)

    return render(
        request,
        'monthly_report.html',
        {
            'records': records,
            'selected_month': month
        }
    )
import csv
from django.http import HttpResponse

@login_required
def export_csv(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="attendance.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Student',
        'Date',
        'Status'
    ])

    records = Attendance.objects.all()

    for record in records:

        writer.writerow([
            record.student.name,
            record.date,
            record.status
        ])

    return response
@login_required
def student_history(request, id):

    student = Student.objects.get(id=id)

    records = Attendance.objects.filter(
        student=student
    )

    return render(
        request,
        'student_history.html',
        {
            'student': student,
            'records': records
        }
    )
from .models import Teacher

from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()

    return render(
        request,
        'teacher_list.html',
        {'teachers': teachers}
    )
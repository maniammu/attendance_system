from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent')
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"
photo = models.ImageField(
    upload_to='students/',
    blank=True,
    null=True
)
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Classroom(models.Model):
    name = models.CharField(max_length=50)

classroom = models.ForeignKey(
    Classroom,
    on_delete=models.CASCADE
)
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
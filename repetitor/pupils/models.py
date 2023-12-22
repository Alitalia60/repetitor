from django.db import models


# Create your models here.

class School(models.Model):
    school_number = models.IntegerField()


class SchoolClass(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True)
    class_number = models.IntegerField()
    class_letter = models.CharField(max_length=1)


class Pupil(models.Model):
    name = models.CharField(max_length=50)
    school_number = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.name} СШ № {self.school_number} класс {self.school_class} '
        # return f'{self.name}  '


class Lesson(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    date = models.DateTimeField()
    lesson_title = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    lesson_comment = models.TextField(blank=True)

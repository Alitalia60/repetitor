from django.contrib import admin

from .models import Pupil, Lesson, School, SchoolClass

# Register your models here.
admin.site.register(Pupil)
admin.site.register(Lesson)
admin.site.register(School)
admin.site.register(SchoolClass)
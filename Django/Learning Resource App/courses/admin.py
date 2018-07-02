from django.contrib import admin
from .models import Courses, Step
# Register your models here.

class StepInline(admin.StackedInline):
    model = Step


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Courses, CourseAdmin)
admin.site.register(Step)
from django.contrib import admin
from .models import Project, ProjectFile
# Register your models here.

admin.site.register(ProjectFile)
admin.site.register(Project)
from django.contrib import admin
from .models import Project
from .models import TODO


admin.site.register(Project)
admin.site.register(TODO)

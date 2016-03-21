from django.contrib import admin

# Register your models here.
from .models import Question,Temperature

admin.site.register(Question)
admin.site.register(Temperature)

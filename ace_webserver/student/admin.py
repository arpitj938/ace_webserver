from django.contrib import admin
from .models import *

class student_dataAdmin(admin.ModelAdmin):
	list_display=["enroll_no","name","sem","mobile","email","linkedin_url","github_url","photo",]
	search_fields=["enroll_no","name","sem",]

admin.site.register(student_data,student_dataAdmin)

class skill_dataAdmin(admin.ModelAdmin):
	list_display=["enroll_no","skill"]

admin.site.register(skill_data,skill_dataAdmin)



# Register your models here.

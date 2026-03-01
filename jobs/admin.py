from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("job_title", "company_name", "application_deadline", "created_at")
    search_fields = ("job_title", "company_name", "company_email")
    list_filter = ("application_deadline", "created_at")

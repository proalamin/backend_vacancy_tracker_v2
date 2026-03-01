from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    application_deadline = models.DateField()
    application_link = models.URLField(blank=True, null=True)
    company_website_url = models.URLField(blank=True, null=True)
    company_facebook_url = models.URLField(blank=True, null=True)
    company_linkedin_url = models.URLField(blank=True, null=True)
    company_phone_no = models.CharField(max_length=30, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["application_deadline", "-created_at"]

    def __str__(self):
        return f"{self.job_title} - {self.company_name}"

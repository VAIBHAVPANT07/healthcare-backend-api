from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctors'
    )
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

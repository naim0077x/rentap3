from django.db import models
import os

class Promoter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tracking_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class RentalApplication(models.Model):
    APPLYING_AS_CHOICES = [
        ('Tenant', 'Tenant'),
        ('Guarantor', 'Guarantor'),
    ]

    move_in_date = models.DateField()
    applying_as = models.CharField(max_length=20, choices=APPLYING_AS_CHOICES)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    phone_number = models.CharField(max_length=15)
    email = models.EmailField() 

    current_address = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    zip_postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    employer_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    monthly_income = models.IntegerField(blank=True, null=True)
    social_security_number = models.CharField(max_length=255, blank=True, null=True)

    id_proof_front = models.FileField(upload_to='ids/', blank=True, null=True)
    id_proof_back = models.FileField(upload_to='ids/', blank=True, null=True)
    photo_selfie = models.FileField(upload_to='photos/', blank=True, null=True)

    references = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)

    submitted_at = models.DateTimeField(auto_now_add=True)
    promoter = models.ForeignKey('Promoter', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def delete(self, *args, **kwargs):
        # Delete associated files before deleting the model
        for field in ['id_proof_front', 'id_proof_back', 'photo_selfie']:
            file_field = getattr(self, field)
            if file_field:
                if os.path.isfile(file_field.path):
                    os.remove(file_field.path)
        super().delete(*args, **kwargs)
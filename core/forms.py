from django import forms
from .models import RentalApplication

class RentalApplicationForm(forms.ModelForm):
    class Meta:
        model = RentalApplication
        fields = [
            'move_in_date', 'applying_as', 'first_name', 'last_name', 'date_of_birth',
            'phone_number', 'email', 'current_address', 'city', 'state_province',
            'zip_postal_code', 'country', 'employer_name', 'job_title',
            'monthly_income', 'social_security_number', 'id_proof_front', 'id_proof_back',
            'photo_selfie', 'references', 'additional_comments'
        ]
        widgets = {
            'move_in_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'applying_as': forms.Select(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'phone_number': forms.TextInput(attrs={'id': 'phone-input'}),
            'email': forms.EmailInput(),
            'current_address': forms.TextInput(),
            'city': forms.TextInput(),
            'state_province': forms.TextInput(),
            'zip_postal_code': forms.TextInput(),
            'country': forms.TextInput(attrs={'value': 'United States'}),
            'employer_name': forms.TextInput(),
            'job_title': forms.TextInput(),
            'monthly_income': forms.NumberInput(),
            'id_proof_front': forms.ClearableFileInput(),
            'id_proof_back': forms.ClearableFileInput(),
            'photo_selfie': forms.ClearableFileInput(),
            'references': forms.Textarea(attrs={'rows': 2}),
            'additional_comments': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        spam_domains = [
            'mailinator.com', 'tempmail.com', '10minutemail.com', 'disposable.com',
            'fakeemail.com', 'spammail.com', 'yopmail.com', 'sharklasers.com'
        ]
        domain = email.split('@')[-1]

        if domain in spam_domains:
            raise forms.ValidationError("Disposable email addresses are not allowed.")

        return email

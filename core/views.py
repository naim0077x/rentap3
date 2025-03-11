from django.shortcuts import render
from .models import RentalApplication, Promoter
from .forms import RentalApplicationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    tracking_code = request.session.get('tracking_code')
    return render(request, 'index.html', {'tracking_code': tracking_code})

def apply(request):
    tracking_code = request.GET.get('ref', '')  # Get tracking code from query params

    # ✅ Step 1: Store tracking code in session if available
    if tracking_code:
        request.session['tracking_code'] = tracking_code  # Store in session

    # ✅ Step 2: Retrieve tracking code from session if previously set
    stored_tracking_code = request.session.get('tracking_code', None)
    promoter = Promoter.objects.filter(tracking_code=stored_tracking_code).first() if stored_tracking_code else None

    if request.method == 'POST':
        form = RentalApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            rental_application = RentalApplication(
                move_in_date=form.cleaned_data['move_in_date'],
                applying_as=form.cleaned_data['applying_as'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                current_address=form.cleaned_data['current_address'],
                city=form.cleaned_data['city'],
                state_province=form.cleaned_data['state_province'],
                zip_postal_code=form.cleaned_data['zip_postal_code'],
                country=form.cleaned_data['country'],
                employer_name=form.cleaned_data.get('employer_name', ''),
                job_title=form.cleaned_data.get('job_title', ''),
                monthly_income=form.cleaned_data.get('monthly_income', None),
                social_security_number=form.cleaned_data.get('social_security_number', None),
                id_proof_front=request.FILES.get('id_proof_front', None),
                id_proof_back=request.FILES.get('id_proof_back', None),
                photo_selfie=request.FILES.get('photo_selfie', None),
                references=form.cleaned_data.get('references', ''),
                additional_comments=form.cleaned_data.get('additional_comments', ''),
                promoter=promoter
            )
            rental_application.save()

            # Store the application in the session
            request.session['submitted_application'] = True
            messages.success(request, "Your rental application has been submitted successfully!")
            return redirect('apply')

    else:
        form = RentalApplicationForm()
    
    return render(request, 'rental_form.html', {
        'form': form,
        'tracking_code': stored_tracking_code  # ✅ Pass tracking code to template
    })

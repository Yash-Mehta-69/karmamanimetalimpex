from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string



def index(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validate required fields
        if not all([name, mobile, email, message]):
            messages.error(request, 'Please fill in all required fields.')
            return HttpResponseRedirect(request.path)
        
        # Compose email content
        subject = f"New Contact Form Submission from {name}"
        email_message = f"""
        Name: {name}
        Mobile: {mobile}
        Email: {email}
        
        Message:
        {message}
        """
        
        try:
            # Send email using SMTP
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Use your configured email
                recipient_list=['karmamani432@gmail.com'],  # Send to yourself karmamani432
                fail_silently=False,
            )
            
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return HttpResponseRedirect(request.path)
        
        except Exception as e:
            # Log the error for debugging
            print(f"Error sending email: {str(e)}")
            messages.error(request, 'There was an error sending your message. Please try again later.')
            return HttpResponseRedirect(request.path)
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def applications(request):
    return render(request, 'pages/applications.html')

def weight_calculation_formula(request):
    return render(request, 'pages/weight_calculation_formula.html')

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validate required fields
        if not all([name, mobile, email, message]):
            messages.error(request, 'Please fill in all required fields.')
            return HttpResponseRedirect(request.path)
        
        # Compose email content
        subject = f"New Contact Form Submission from {name}"
        email_message = f"""
        Name: {name}
        Mobile: {mobile}
        Email: {email}
        
        Message:
        {message}
        """
        
        try:
            # Send email using SMTP
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Use your configured email
                recipient_list=['karmamani432@gmail.com'],  # Send to yourself
                fail_silently=False,
            )
            
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return HttpResponseRedirect(request.path)
        
        except Exception as e:
            # Log the error for debugging
            print(f"Error sending email: {str(e)}")
            messages.error(request, 'There was an error sending your message. Please try again later.')
            return HttpResponseRedirect(request.path)
    return render(request, 'pages/contact.html')

# custom 404 view
def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)

def stainless_steel_sheets_plates_coils(request):
    return render(request, 'products/stainless_steel_sheets_plates_coils.html')

def stainless_steel_pipes_tubes(request):
    return render(request, 'products/stainless_steel_pipes_tubes.html')

def stainless_steel_bars(request):
    return render(request, 'products/stainless_steel_bars.html')

def stainless_steel_flanges(request):
    return render(request, 'products/stainless_steel_flanges.html')


def stainless_steel_pipe_fittings(request):
    return render(request, 'products/stainless_steel_pipe_fittings.html')

def stainless_steel_angles(request):
    return render(request, 'products/stainless_steel_angles.html')

    
def stainless_steel_channels(request):
    return render(request, 'products/stainless_steel_channels.html')

def stainless_steel_flats(request):
    return render(request, 'products/stainless_steel_flats.html')

def stainless_steel_wires(request):
    return render(request, 'products/stainless_steel_wires.html')



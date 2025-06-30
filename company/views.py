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

def vcard(request):
    # return render(request, 'pages/vcard_chatgpt.html')
    # return render(request, 'pages/vcard_deepseek.html')
    # return render(request, 'pages/vcard_grok.html')
    return render(request, 'pages/vcard.html')
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
    product_name = 'stainless_steel_sheets_plates_coils'
    return render(request, 'products/stainless_steel_sheets_plates_coils.html', {'product_name': product_name})

def stainless_steel_pipes_tubes(request):
    product_name = 'Stainless Steel Pipes Tubes'
    return render(request, 'products/stainless_steel_pipes_tubes.html', {'product_name': product_name})

def stainless_steel_bars(request):
    product_name = 'stainless_steel_bars'
    return render(request, 'products/stainless_steel_bars.html', {'product_name': product_name})

def stainless_steel_flanges(request):
    product_name = 'stainless_steel_flanges'
    return render(request, 'products/stainless_steel_flanges.html', {'product_name': product_name})


def stainless_steel_pipe_fittings(request):
    product_name = 'stainless_steel_pipe_fittings'
    return render(request, 'products/stainless_steel_pipe_fittings.html', {'product_name': product_name})

def stainless_steel_angles(request):
    product_name = 'stainless_steel_angles'
    return render(request, 'products/stainless_steel_angles.html', {'product_name': product_name})

    
def stainless_steel_channels(request):
    product_name = 'stainless_steel_channels'
    return render(request, 'products/stainless_steel_channels.html', {'product_name': product_name})

def stainless_steel_flats(request):
    product_name = 'stainless_steel_flats'
    return render(request, 'products/stainless_steel_flats.html', {'product_name': product_name})

def stainless_steel_wires(request):
    product_name = 'stainless_steel_wires'
    return render(request, 'products/stainless_steel_wires.html', {'product_name': product_name})



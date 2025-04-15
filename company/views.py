from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string



def index(request):
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
                recipient_list=[settings.EMAIL_HOST_USER],  # Send to yourself
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


import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

def generate_product_pdf(request, product_name):
    valid_products = [
        'stainless-steel-sheets-plates-coils',
        'stainless-steel-pipes-tubes',
        'stainless-steel-bars',
        'stainless-steel-flanges',
        'stainless-steel-pipe-fittings',
        'stainless-steel-angles',
        'stainless-steel-channels',
        'stainless-steel-flats',
        'stainless-steel-wires'
    ]
    
    if product_name not in valid_products:
        return HttpResponse("Product not found", status=404)
    
    # Convert slug to corresponding template name.
    # Assumes that your product templates are in 'products/' and named with underscores.
    template_name = product_name.replace('-', '_') + '.html'
    template_path = f'products/{template_name}'
    
    # Context for the template; pdf_mode can be used to adjust CSS in the template.
    context = {
        'pdf_mode': True,
        'product_slug': product_name,
        'STATIC_URL': settings.STATIC_URL,
        'request': request,
    }
    
    # Render the HTML string from the template.
    try:
        html_string = render_to_string(template_path, context)
    except Exception as e:
        return HttpResponse("Template not found", status=404)
    
    # Optional: pdfkit configuration options. Adjust if needed.
    options = {
        'encoding': 'UTF-8',
        'enable-local-file-access': None,  # Uncomment if needed for local static files
    }
    
    try:
        # Generate PDF from the HTML string.
        pdf = pdfkit.from_string(html_string, False, options=options)
    except Exception as e:
        return HttpResponse(f"Error generating PDF: {e}", status=500)
    
    # Return the PDF file as an attachment.
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product_name}-specifications.pdf"'
    return response

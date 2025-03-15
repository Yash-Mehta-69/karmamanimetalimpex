from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def applications(request):
    return render(request, 'pages/applications.html')

def weight_calculation_formula(request):
    return render(request, 'pages/weight_calculation_formula.html')

def contact(request):
    return render(request, 'pages/contact.html')

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
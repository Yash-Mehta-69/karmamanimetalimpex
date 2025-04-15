from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('applications/', views.applications, name='applications'),    
    path('weight-calculation-formula/', views.weight_calculation_formula, name='weight-calculation-formula'),
    path('contact-us/', views.contact, name='contact-us'),
    path('stainless-steel-sheets-plates-coils/', views.stainless_steel_sheets_plates_coils, name='stainless-steel-sheets-plates-coils'),
    path('stainless-steel-pipes-tubes/', views.stainless_steel_pipes_tubes, name='stainless-steel-pipes-tubes'),
    path('stainless-steel-bars/', views.stainless_steel_bars, name='stainless-steel-bars'),
    path('stainless-steel-flanges/', views.stainless_steel_flanges, name='stainless-steel-flanges'),
    path('stainless-steel-pipe-fittings/', views.stainless_steel_pipe_fittings, name='stainless-steel-pipe-fittings'),
    path('stainless-steel-angles/', views.stainless_steel_angles, name='stainless-steel-angles'),
    path('stainless-steel-channels/', views.stainless_steel_channels, name='stainless-steel-channels'),
    path('stainless-steel-flats/', views.stainless_steel_flats, name='stainless-steel-flats'), 
    path('stainless-steel-wires/', views.stainless_steel_wires, name='stainless-steel-wires'),
     # Updated PDF generation URL (uses product_name slug)
    # path('product/<str:product_name>/download-pdf/', views.generate_product_pdf, name='generate_product_pdf'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
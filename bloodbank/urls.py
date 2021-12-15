"""bloodbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bbank_admin import views




urlpatterns=[
    path('admin/', admin.site.urls),
    path('show_area/', views.show_area),
    path('show_bgrp/', views.show_bgrp),
    path('show_donor/',views.show_donor),
    path('show_receiver/', views.show_receiver),
    path('show_bbank/', views.show_bbank),
    path('show_hospital/', views.show_hospital),
    path('show_stock/',views.show_stock),
    path('show_appoinment/', views.show_appoinment),
    path('show_requestblood/', views.show_requestblood),
    path('show_events/', views.show_events),
    path('show_van/', views.show_van),
    path('show_gallery/', views.show_gallery),
    path('show_feedback/', views.show_feedback),
    path('area_form/', views.area_form),
    path('appointment_form/', views.appointment_form),
    path('bbank_form/',views.bbank_form),
    path('bgrp_form/', views.bgrp_form),
    path('donor_form/', views.donor_form),
    path('events_form/', views.events_form),
    path('feedback_form/', views.feedback_form),
    path('gallery_form/', views.gallery_form),
    path('hospital_form/', views.hospital_form),
    path('receiver_form/', views.receiver_form),
    path('requestblood_form/', views.requestblood_form),
    path('stock_form/', views.stock_form),
    path('van_form/', views.van_form)

  ]



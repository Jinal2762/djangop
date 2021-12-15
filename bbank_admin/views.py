from django.shortcuts import render
#from bbank_admin.models import User
#from bbank_admin.forms import AreaForm
#from bbank_admin.models import Area
from bbank_admin.models import Blood_grp
from bbank_admin.forms import Blood_grpForm
from bbank_admin.models import Donor
from bbank_admin.forms import DonorForm
from bbank_admin.models import Receiver
from bbank_admin.forms import ReceiverForm
from bbank_admin.models import Bloodbank
from bbank_admin.forms import BloodbankForm
from bbank_admin.models import Hospitals
from bbank_admin.forms import HospitalsForm
from bbank_admin.models import Blood_stock
from bbank_admin.forms import Blood_stockForm
from bbank_admin.models import Appointment
from bbank_admin.forms import AppointmentForm
from bbank_admin.models import Request_blood
from bbank_admin.forms import Request_bloodForm
from bbank_admin.models import Event
from bbank_admin.forms import EventForm
from bbank_admin.models import Van
from bbank_admin.forms import VanForm
from bbank_admin.models import Gallery
from bbank_admin.forms import GalleryForm
from bbank_admin.models import Feedback
from bbank_admin.forms import FeedbackForm

def show_area(request):
    area = Area.objects.all()
    return render(request, "show_area.html", {'areas': area})

def show_bgrp(request):
    bgrp = Blood_grp.objects.all()
    return render(request, "show_bgrp.html", {'bgrps': bgrp})

def show_donor(request):
    donor=Donor.objects.all()
    return render(request, "show_donor.html", {'donors': donor})


def show_receiver(request):
    receiver=Receiver.objects.all()
    return render(request, "show_receiver.html", {'receivers': receiver})


def show_bbank(request):
    bbank=Bloodbank.objects.all()
    return render(request, "show_bbank.html", {'bbanks': bbank})


def show_hospital(request):
    hosp=Hospitals.objects.all()
    return render(request, "show_hospital.html", {'hospp': hosp})


def show_stock(request):
    stock=Blood_stock.objects.all()
    return render(request, "show_stock.html", {'stocks': stock})

def show_appoinment(request):
    appoinment = Appointment.objects.all()
    return render(request, "show_appoinment.html", {'appoinments ': appoinment})


def show_requestblood(request):
     request_blood= Request_blood.objects.all()
     return render(request, "show_requestblood.html", {'request_bloods': request_blood})

def show_events(request):
    event= Event.objects.all()
    return render(request, "show_events.html", {'events': event})


def show_van(request):
    van=Van.objects.all()
    return render(request, "show_van.html", {'vans': van})

def show_gallery(request):
    gallery= Gallery.objects.all()
    return render(request, "show_gallery.html", {"gallerys": gallery})

def show_feedback(request):
    feedback= Feedback.objects.all()
    return render(request, "show_feedback.html", {"feedbacks": feedback})


def area_form(request):
    return render(request, "area_form.html")

def appointment_form(request):
    return render(request, "appointment_form.html")

def bbank_form(request):
    return render(request, "bbank_form.html")

def bgrp_form(request):
    return render(request, "bgrp_form.html")

def donor_form(request):
    return render(request, "donor_form.html")

def events_form(request):
    return render(request, "events_form.html")

def feedback_form(request):
    return render(request, "feedback_form.html")

def gallery_form(request):
    return render(request, "gallery_form.html")

def hospital_form(request):
    return render(request, "hospital_form.html")

def receiver_form(request):
    return render(request, "receiver_form.html")

def requestblood_form(request):
    return render(request, "requestblood_form.html")

def stock_form(request):
    return render(request, "stock_form.html")

def van_form(request):
    return render(request, "van_form.html")



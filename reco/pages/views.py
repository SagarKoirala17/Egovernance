from django.shortcuts import render
from .models import Citizen
from address.models import Address

# Create your views here.
def index(request):
    if request.method==POST:
          dob =request.POST["dob"]
          phone =request.POST["Phone"]
          age =  request.POST["Age"]
          gender =request.POST["gender"]
          father_name =request.POST["fathername"]
          grandfather_name =request.POST["Grandfathername"]
          father_citizen_number =request.POST["fathercitizennumber"]
          birth_certificate_photo =request.POST[""]
          applicant_photo =request.POST["applicantphoto"]
          father_citizenship_photo =request.POST["fathercitizenship"]


return render(request,'pages/index.html')
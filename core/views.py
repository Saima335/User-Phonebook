from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.form import AddContactForm
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
import re

# Create your views here.
def Home(request):
    # return HttpResponse("Contact Added Successfully")
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

def TestAPI(request):
    your_json = [{"firstName": "Saima", "lastName": "Kausar"}]
    return HttpResponse(your_json, 'application/json')

def AddContact(request):
    if request.POST:
        form = AddContactForm(request.POST, request.FILES)
        valid = True
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        mobile = request.POST.get("mobile", "")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        if not(first_name.isalpha()):
            messages.error(request, 'Invalid First Name')
            valid = False
        if last_name != "" and not(last_name.isalpha()):
            messages.error(request, 'Invalid Last Name')
            valid = False
        if mobile != "" and not (mobile.isdigit() and len(mobile)==11):
            messages.error(request, 'Invalid Mobile Number')
            valid = False
        if phone != "" and not(phone.isdigit() and len(phone)==10):
            messages.error(request, 'Invalid Phone Number')
            valid = False
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if email != "" and not(re.match(email_pattern, email)):
            messages.error(request, 'Invalid Email Address')
            valid = False
        if valid == False:
            return redirect(AddContact)
            # return HttpResponse(message)
        elif form.is_valid():
            form.save()
            return redirect(Home)
    return render(request, 'contact.html', {'form': AddContactForm})

def DeleteContact(request, id):
    try:
        Contact.objects.get(id=id).delete()
        messages.success(request, 'Contact deleted!')
        return redirect(Home)
    except Contact.DoesNotExist:
        messages.warning(request, 'Invalid operation')
        return redirect(to=Home)
    # return render(request, 'contacts.html', {'contacts': contacts})


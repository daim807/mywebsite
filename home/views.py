from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('message')

        Contact.objects.create(name=name, email=email, description=description)

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, "contact.html")

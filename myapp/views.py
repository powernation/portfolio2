from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Message from {name}"
        full_message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],  # your receiving address
            )
            messages.success(request, '✅ Your message has been sent successfully!')
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, '❌ Something went wrong. Please try again later.')

        return redirect('contact')  # Change this to your URL name

    return render(request, 'contact.html')

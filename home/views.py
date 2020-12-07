from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


def index(request):  # view to return the index page
    return render(request, 'home/index.html')


def email_page(request):  # view to return the index page
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
        )
        messages.success(request, f"Thank you for your query we'll get back \
        to you on {email}.")
    return render(request, 'home/email_submission.html')

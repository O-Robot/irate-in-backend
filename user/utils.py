from django.core.mail import send_mail
from decouple import config

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        config('EMAIL_HOST'),  # Sender's email address
        recipient_list,             # List of recipient email addresses
        fail_silently=False,        # Set to True to suppress exceptions if email sending fails
    )

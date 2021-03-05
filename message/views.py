import os
from django.shortcuts import render, redirect

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
client = Client()

def get_sent_messages():
    messages = client.messages.list(from_=TWILIO_PHONE_NUMBER)
    return messages

def send_message(to, body):
    client.messages.create(
        to=to,
        from_=TWILIO_PHONE_NUMBER,
        body=body,
    )

def index(request):
    messages = get_sent_messages()
    return render(request, 'message/index.html', {'messages': messages})

def add_compliment(request):
    sender = request.POST['sender']
    receiver = request.POST['receiver']
    compliment = request.POST['compliment']
    to = request.POST['to']
    body = f'{sender} says: {receiver} is {compliment}'
    send_message(to, body)
    return redirect('index')

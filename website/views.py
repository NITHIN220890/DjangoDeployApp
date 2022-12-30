from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings


def home(request) :
	return render(request,'home.html',{})

def contact(request) :
	if request.method =="POST" :
		message_name =request.POST['message-name']
		message_email =request.POST['message-email']
		message =request.POST['message']
		phone_number=request.POST['phone-number']
		host_email='sahanadamotharan@gmail.com'
		
		email=EmailMessage('From Dr Sahana',
		f' Hi {message_name}! \n  Thanks for  contacting me Will be glad to assist you on the query raised..\n Your mobile no {phone_number} \n\nYour Query :{message}',settings.EMAIL_HOST_USER,[message_email,host_email])
		email.fail_silently=True
		email.send()
		return render(request,'contact.html',{'message_name':message_name})
	else :
		return render(request,'contact.html',{})



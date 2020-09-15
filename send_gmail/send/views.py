from django.shortcuts import render
from django.core.mail import send_mail


def App(request):
    return render(request, 'App.tsx',{})

def Form(request):
    if request.method == "POST":
        message_fullname = request.POST['message_fullname']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']

        send_mail(
            message_fullname,
            message_email,
            message_subject,
            message,
            ['bro68207@gmail.com'],
        )

        
        return render(request,'Form.tsx',{'message_fullname':message_fullname})
    else:
        return render(request,'Form.tsx',{}) 
           

# Create your views here.

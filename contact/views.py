from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

# Create your views here.


def index (request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        data = Contact(name=name,email=email,message=message)
        data.save()

        

        return render(request,'index.html',{'name':name})
    else:
        return render(request,'index.html')
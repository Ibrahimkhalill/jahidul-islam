
from django.shortcuts import render, redirect

from mainapp.models import Image
from . models import *
# Create your views here.


def home(request):
    image = Image.objects.all()
    context = {
        "image": image
    }
    print(image)
    return render(request, 'index.html', context)


def message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        text = request.POST.get("message")
        print(name,email,subject,text)
        model = Mesaage(name=name,email=email,subject=subject,text=text)
        model.save()

        return redirect('/')
    
     

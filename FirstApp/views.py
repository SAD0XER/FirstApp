from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from FirstApp.models import Contact

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)
        # check if user entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
    # return render(request, 'index.html')


def about(request):
    # return HttpResponse("This is About page.")
    return render(request, 'about.html')


def services(request):
    # return HttpResponse("This is service page.")
    return render(request, 'services.html')


def contact(request):
    # Here is the logic of post method of Contact Form.
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')
    # return HttpResponse("This is Contact Page.")

    def __str__(self):
        # change thee object name which you want to see in the Contact Object (Header) in DB.
        return self.name

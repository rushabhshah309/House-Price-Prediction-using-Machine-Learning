from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import *
from accounts.models import *
from django.core.mail import send_mail
import random
from django.conf import settings


def login(request):
    #if request.session.get('first_name'):
        #return redirect("/")
    if request.method == "POST":
        usrname = request.POST.get('username')
        password1 = request.POST.get('password')
        email = request.POST.get('email')

        try:
            use = user.objects.get(usrname=usrname, password1=password1)
            if use.status == "active":
                request.session['first_name'] = use.first_name
                request.session['userpk'] = use.pk
                return redirect('/')
            else:
                email = email
                rec = [email, ]
                subject = "Successful OTP conformation"
                randotp = random.randint(1000, 9999)
                message = "Your otp for successful registration is " + str(randotp)
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject, message, email_from, rec)
                return render(request, 'accounts/otp.html', {'randotp': randotp, 'email': email, })
        except:
            messages.info(request, 'Enter correct username and password')
            return redirect('/accounts/login')

    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        usrname = request.POST.get('usern')
        password1 = request.POST.get('password')
        password2 = request.POST.get('cpassword')
        email = request.POST.get('email')

        try:
            # use = user.objects.get(email=email)
            if user.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('/accounts/signup')
            use = user.objects.get(usrname=usrname)
            if use:
                messages.info(request, 'Username already exists')
                return redirect('/accounts/signup')

        except:
            user.objects.create(first_name=first_name, last_name=last_name,
                                email=email, usrname=usrname, password1=password1,
                                password2=password2)
            rec = [email, ]
            subject = "Successful OTP conformation"
            randotp = random.randint(1000, 9999)
            message = "Your otp for successful registration is " + str(randotp)
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, rec)
            return render(request, 'accounts/otp.html', {'randotp': randotp, 'email': email, })
    else:
        return render(request, 'accounts/signup.html')


def logout(request):
    try:
        del request.session['first_name']
        return redirect('/')
    except:
        pass


def validateotp(request):
    error = ""
    if request.method == "POST":
        r_otp = request.POST['r_otp']
        u_otp = request.POST['u_otp']
        email = request.POST['email']
        if r_otp == u_otp:
            use = user.objects.get(email=email)
            use.status = "active"
            use.save()
            return redirect('/accounts/login')

        else:
            error = "incorrect otp"

            email = request.POST['email']
            rec = [email, ]
            subject = "succesfull otp registration"
            randotp = random.randint(1000, 9999)
            message = "your otp for succesfull registration is" + str(randotp)
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, rec)
            return render(request, 'accounts/otp.html', {'randotp': randotp, 'email': email})

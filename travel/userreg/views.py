from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        psw = request.POST['psw']
        user = auth.authenticate(username=uname, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('login')


    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def registration(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        psw = request.POST['psw']
        rpsw = request.POST['rpsw']
        if psw == rpsw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"This username is already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                            password=psw)
                user.save()
                messages.info(request, "Registered Successfully")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('registration')
        return redirect('/')

    return render(request, "register.html")

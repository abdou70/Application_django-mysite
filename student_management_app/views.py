from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from student_management_app.EmailBackEnd import EmailBackEnd


def showview(request):
    return render(request,'demo.html')

def Login(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method!= "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!= None:
            login(request,user)
            print("je suis de la postefinance")
            return HttpResponse("Email "+request.POST.get("email")+"Password"+request.POST.get("password"))
        else:
            return HttpResponse("<h2>Invalid Login</h2>")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("user "+request.user.email+" usertype "+request.user.user_type)
    else:
        return HttpResponse("please Login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
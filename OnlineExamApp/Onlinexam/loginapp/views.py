from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if(request.method=='GET'):
        return render(request, 'loginapp/login.html')
    username = request.POST['username']
    password = request.POST['password']
    userobj = auth.authenticate(username=username, password=password)
    if userobj == None:
        return render(request, 'loginapp/login.html', {"message": "Invalid Credentials"})
    else:
        auth.login(request, userobj) #starts session for the user
        request.session["username"]=userobj.username
        request.session["score"]=0
        request.session["qindex"]=0
        request.session["answers"]={}
        return render(request, 'Examapp/subjects.html')




def register(request):
    if(request.method == 'GET'):
        return render(request, 'loginapp/register.html')
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    userobj = User.objects.create_user(username=username, password=password, email=email)
    userobj.save()
    return render(request, 'loginapp/login.html', {'message':'Registeration successfull. Now you can login'})
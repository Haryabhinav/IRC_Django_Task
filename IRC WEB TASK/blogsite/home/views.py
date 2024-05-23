from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth import logout,login,authenticate
# Create your views here.
def index(request):
     
 
     if(request.method=="POST"):
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(username=email, password=password)#Checking the users credential
        
        if user is not None:
           #To login User
           login(request, user)
           return redirect('/Userlogin')
        else:
             return render(request,'base.html')

 
     return render(request,'base.html')
def UserLogin(request):
   return HttpResponse("Logged In")


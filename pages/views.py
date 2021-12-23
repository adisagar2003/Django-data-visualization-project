from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
import matplotlib.pyplot as pb

# Create your views here.
def index(request):
    return render(request,'index.html')

def sign_in(request):

    if request.method=='POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)


            
            return render(request,'index.html')



        

        else:
            return HttpResponse('bb')
    return render(request,'signin.html')

def sign_out(request):
    logout(request)

    return render(request,'signout.html')





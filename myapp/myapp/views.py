from django.http import HttpResponse
from django.shortcuts import render
def test(request):

    print("this is test finction")

    return HttpResponse("<h1> hello this is index page </h1>")
def about(request):

 print("this is test finction")
 return render(request,"about.html",{})


def home(request):
    return render(request,"home.html",{}) 
 

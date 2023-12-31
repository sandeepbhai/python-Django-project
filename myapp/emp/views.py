from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp
# Create your views here.
def emp_home(request):

    return render(request,"emp/home.html",{ 
        
    })

def add_emp(request):
         
    if request.method=="POST":
       
       emp_name = request.POST.get("emp_name")
       emp_id = request.POST.get("emp_id")
       emp_phone = request.POST.get("emp_phone")
       emp_add = request.POST.get("address")
       emp_working = request.POST.get("working")
       emp_dept= request.POST.get("dept") 
       
       e=Emp()
       e.name=emp_name
       e.emp_id=emp_id
       e.phone=emp_phone
       e.address= emp_add
       e.department=emp_dept
       e.working=emp_working
       if emp_working is None:
            e.working=False  
       else:
            e.working=True

       e.save()
       return  redirect("/emp/home/")
        
    return render(request,"emp/add_emp.html",{})

def view_emp(request):
          
    emps = Emp.objects.all()      
    return render(request,"emp/view.html",{
           

        'emps':emps
    })


def delete_emp(request,emp_id):

    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/view_emp/")  


def update_emp(request,emp_id):

    emp=Emp.objects.get(pk=emp_id)
    
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def about(request):

    return render(request,"emp/about.html",{})


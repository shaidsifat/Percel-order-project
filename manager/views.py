from django.shortcuts import render
from . import models
from django import forms
from django.forms import Form
from .models import createnewpercel
from .models import createorder
from manager.forms import createnewpercelForm,createorderForm,createcheckorderForm
from .models import createcheckorder
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages


def  createnewpercels(request):

    if request.method == 'POST':
       form = createnewpercelForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('createneworder/')
    else:
        form = createnewpercelForm()
    return render(request,'createnewpercel.html',{'form':form})           
    
  

def new_page(request): 

  sifat_list = createcheckorder.objects.all()
  return render(request, 'newpage.html', context = {'data':sifat_list})   



def checkorders(request):

    if request.method == 'POST':
        form =  createcheckorderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newpage/')
    else:
        form =  createcheckorderForm()

 
    return render(request,'chargebox.html',{'form':form})            
 

def createorders(request):
    
    if request.method == 'POST':
        form = createorderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createorder/')
    else:
        form = createorderForm()   
    return render(request,'createorder.html',{'form':form}) 




def index(request):  
    student = StudentForm()  
    return render(request,"index.html",{'form':student})  

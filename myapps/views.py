
from django.shortcuts import render,redirect,get_object_or_404
from .models import Details
from django.urls import reverse
from .forms import detailsform
from django.contrib import messages
import os
# Create your views here.

def member(request):
    return render(request,"index.html")

def registration(request):
    if request.method=="POST":
        city_name=request.POST['city_name']
        state_name=request.POST['state_name']
        country_name=request.POST['country_name']
        if len(request.FILES)!=0:
            image=request.FILES['image']
        obj=Details.objects.create(city_name=city_name,state_name=state_name,country_name=country_name,image=image)   
        obj.save()
        messages.success(request,"Product Added Successfully")
        return  redirect('/member/')
    return render(request,'index.html')

def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html' ,{'details':details})

def edit(request,id):
    object=Details.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
          if len(object.image)>0:
            os.remove(object.image.path)
          object.image=request.FILES['image']
        object.save()
        messages.success(request,"product ADDED successfully")
        return redirect('/member/retieve/')
    return render(request,"edit.html", {"object":object})

def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Details.objects.all()
        instance = get_object_or_404(Details, id=id)
        if request.method == 'POST':
                  form = detailsform(request.POST, request.FILES, instance=instance)
                  if form.is_valid():
                        form.save()
                        return redirect('/member/retrieve/')  # Redirect to detail view or another page
                  else:
                        form = detailsform(instance=instance)
    return render(request,"retrieve.html")

def delete(request,id):   
        obj=Details.objects.filter(id=id).delete()
        return render(request,'retrieve.html')  

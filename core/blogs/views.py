from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .form import BLogForm
 
# Create your views here.
def list_view(request):
    context={
        'blogs': Blog.objects.all()
    }
    return render(request,"list_view.html",context)


def create_view(request):
    form=BLogForm()
    if request.method=="POST":
        print(request.POST)
        form=BLogForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(list_view)
    context={
        'blogs': Blog.objects.all(),
        'form':form
    }
    return render(request,"create_view.html",context)


def update_view(request,id):
    blog=get_object_or_404(Blog,id=id)
    form=BLogForm(instance=blog)    
    if request.method=="POST":
        print(request.POST)
        form=BLogForm(request.POST, instance=blog)
    if form.is_valid():
        form.save()
        return redirect(list_view)
    context={
        'form':form
    }
    return render(request,'update.html',context)

def delete_view(request,id):
    blog=get_object_or_404(Blog,id=id)
    form=BLogForm(instance=blog)    
    if request.method=="POST":
        print(request.POST)
        form=BLogForm(request.POST, instance=blog.delete())
    if form.is_valid():
        form.save()
        return redirect(list_view)
    context={
        'form':form
    }
    return render(request,'delete.html',context)
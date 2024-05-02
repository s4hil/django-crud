from django.shortcuts import render, redirect
from .models import users

# Create your views here.

def index(request):
    data = users.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def insertData(request):
    data = users.objects.all()
    context = {"data": data}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = users(name=name, email=email, phone=phone)
        query.save()
    return render(request, "index.html", context)
    
def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        e = users.objects.get(id=id)
        e.name = name
        e.email = email
        e.phone = phone
        e.save()
        return redirect("/")
    data = users.objects.get(id=id)
    context = {"d": data}
    
    return render(request, "update.html", context)
    

def deleteData(request, id):
        query = users.objects.get(id=id)
        query.delete()
        return redirect("/")

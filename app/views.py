from django.shortcuts import render
from .models import Crud
from django.shortcuts import redirect

def index(request):
    data = Crud.objects.all()
    context ={"data": data}
    return render(request, "index.html",context)

def insertData(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('textarea')
        query = Crud(title=title, description=description)
        query.save()  # Fixed missing parentheses
        return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('textarea')
        edit = Crud.objects.get(id=id)
        edit.title =title
        edit.description = description
        edit.save()
        return redirect("/")

        query = Crud(title=title, description=description)
        query.save()  # Fixed missing parentheses
        return redirect("/")    
    d = Crud.objects.get(id=id)
    context ={"d": d}

    return render(request, "edit.html",context)

def deleteData(request, id):
    d= Crud.objects.get(id=id)
    d.delete()
    return redirect("/")


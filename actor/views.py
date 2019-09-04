from django.shortcuts import render, redirect  
from actor.forms import ActorForm  
from actor.models import Actor  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = ActorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    actors = Actors.objects.all()  
    return render(request,"show.html",{'actors':actors})  
def edit(request, id):  
    actor = Actor.objects.get(id=id)  
    return render(request,'edit.html', {'actor':actor})  
def update(request, id):  
    actor = Actor.objects.get(id=id)  
    form = ActorForm(request.POST, instance = actor)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'actor': actor})  
def destroy(request, id):  
    actor = Actor.objects.get(id=id)  
    actor.delete()  
    return redirect("/show")  

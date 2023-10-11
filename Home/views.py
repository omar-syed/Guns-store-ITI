from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Gun
from . forms import GunForm 

# Create your views here.
def home(request):
    guns = Gun.objects.all()
    context = {
        'guns': guns}
    return render(request,'Home\home.html',context )


def contact(request):
    return render(request,'Home\contact.html')


def about (request):
    return render(request,"Home\\about.html")
    
    

# def listt(request):
#     return HttpResponse(guns)


def detail(request, id):
    gun = Gun.objects.filter(id = id)

    gun = list(gun)
    if gun:
        print(gun[0])
        return render(request,"Home\detail.html",{'gun':gun[0]})

    return HttpResponse("Sorry target gun profile not found ")
    

def delete(request,id):
    gun = Gun.objects.filter(id =id)
    if gun:
        gun[0].delete()
        return redirect('home')
    else:
        return HttpResponse("Sorry, gun not found")
    
    

def search(request):
    query = request.GET.get('query')
    guns = Gun.objects.filter(name__icontains=query)
    context = {
        'guns': guns,
        'query': query
    }
    return render(request, 'Home/search.html', context)    

def add_gun(request):
    if request.method == 'POST':
        form = GunForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GunForm()
    return render(request, 'Home/add_gun.html', {'form': form})    

def edit_gun(request,id):
    gun = Gun.objects.get(id=id) 
    form = GunForm(instance=gun)
    
def edit_gun(request, id):
    gun = Gun.objects.get(id=id)
    if request.method == 'POST':
        form = GunForm(request.POST, request.FILES, instance=gun)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GunForm(instance=gun)
    return render(request, 'Home/edit_gun.html', {'form': form, 'gun': gun})
        
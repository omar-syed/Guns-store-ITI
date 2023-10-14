import os
from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import Gun,Category
from .forms import GunForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

def detail(request, id):
    gun = Gun.objects.filter(id = id)

    gun = list(gun)
    if gun:
        print(gun[0])
        return render(request,"Home\detail.html",{'gun':gun[0]})

    return HttpResponse("Sorry target gun profile not found ")
    

# def delete(request,id):
#     gun = Gun.objects.filter(id =id)
#     if gun:
#         gun[0].delete()
#         return redirect('home')
#     else:
#         return HttpResponse("Sorry, gun not found")



@login_required
def delete(request, id):
    gun = Gun.objects.filter(id=id)
    if gun:
        gun_instance = gun[0]
        image_path = gun_instance.image.path
        
        # Delete the image file
        if os.path.exists(image_path):
            os.remove(image_path)

        gun_instance.delete()
        print(request.user,'I am delete function in views.py')
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
@login_required
def add_gun(request):
    if request.method == 'POST':
        form = GunForm(request.POST, request.FILES)
        if form.is_valid():
            if Gun.objects.filter(name=form.cleaned_data['name']).exists():
                form.add_error('name', 'A gun with this name already exists.')
            else:
            # Save the form data to create a new Gun object
                gun = Gun(
                    name=form.cleaned_data['name'],
                    image=form.cleaned_data['image'],
                    price=form.cleaned_data['price'],
                    description=form.cleaned_data['description'],
                    in_stock=form.cleaned_data['in_stock'],
                    category=form.cleaned_data['category'],
                    owner=request.user
                )
                gun.save()
                return redirect('home')
    else:
        form = GunForm()

    context = {
        'form': form
    }
    return render(request, 'Home/add_gun.html', context)

@login_required
def edit_gun(request, id):
    gun = get_object_or_404(Gun, id=id)
    
    # Check if the current user is the owner of the gun
    if gun.owner != request.user:
        return HttpResponse("You are not authorized to edit this gun.")

    if request.method == 'POST':
        form = GunForm(request.POST, request.FILES)
        if form.is_valid():
            gun.name = form.cleaned_data['name']
            gun.price = form.cleaned_data['price']
            gun.description = form.cleaned_data['description']
            gun.in_stock = form.cleaned_data['in_stock']
            gun.category = form.cleaned_data['category']

            # Check if a new image is provided
            if 'image' in request.FILES:
                gun.image = form.cleaned_data['image']
            

            gun.save()
            return redirect('home')
    else:
        form = GunForm({
            'name': gun.name,
            'price': gun.price,
            'description': gun.description,
            'in_stock': gun.in_stock,
            'category': gun.category,
            }
        )

    context = {
        'form': form
    }
    return render(request, 'Home/edit_gun.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories}
    return render(request,'Home\category.html',context )

def category_detail(request, category):
    guns = Gun.objects.filter(category__name=category)
    context = {
        'guns': guns,
        'category': category
    }
    return render(request, 'Home/category_detail.html', context)
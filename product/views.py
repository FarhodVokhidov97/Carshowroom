from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category,TypeCar,Services

# Create your views here.


def product(request, slug):

    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product/product.html', {'product': product})


def addProd(request):
    cat = Category.objects.all()
    type = TypeCar.objects.all()
    context = {
        'category': cat,
        'types':type
    }

    pro = Product()
    if request.method == 'POST':
        pro.typecar = TypeCar.objects.get(id=request.POST.get('types'))
        pro.name = request.POST.get('name')
        pro.slug = request.POST.get('slug')
        pro.description = request.POST.get('description')
        pro.price = request.POST.get('price')
        pro.year = request.POST.get('year')
        pro.category = Category.objects.get(id=request.POST.get('category'))
       

        if len(request.FILES) != 0:
            pro.image = request.FILES['image']
            pro.thumbnail = request.FILES['image']

        pro.save()
        return redirect('shop')

    return render(request, 'addpro.html', context)

def deletePro(request,id):
    Product.objects.get(id=id).delete()
    return redirect('shop')


def servises(request):
    servis = Services.objects.all()
    context = {
        'serv':servis
    }
    return render(request,'servises.html',context)

def add_servises(request):
    serv = Services()
    if request.method == 'POST':
        serv.code = request.POST.get('code')
        serv.name = request.POST.get('name')
        serv.sedanPrice = request.POST.get('price1')
        serv.UniversalPrice = request.POST.get('price2')
        serv.PicapPrice = request.POST.get('price3')

        serv.save()
        return redirect('serv')
    
    return render(request, 'addsevis.html')

def edit_serv(request,id):
    serv = Services.objects.get(id=id)
    context = {
        'serv':serv
    }

    if request.method == 'POST':
        serv.name = request.POST.get('name')
        serv.code = request.POST.get('code')
        serv.sedanPrice = request.POST.get('price1')
        serv.UniversalPrice = request.POST.get('price2')
        serv.PicapPrice = request.POST.get('price3')
        serv.save()
        return redirect('serv')
    
    return render(request, 'editserv.html',context)

def deleteServ(request,id):
    serv = Services.objects.get(id=id).delete()
    return redirect('serv')


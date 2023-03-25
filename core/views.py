from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from product.models import Product, Category
from .forms import SingUpForm
from django.contrib.auth import login


def frontpage(request):
    product = Product.objects.all()[0:8]
    context = {
        'products': product
    }

    return render(request, 'front.html', context)


def singup(request):

    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SingUpForm()

    return render(request, 'core/singup.html', {'form': form})


@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        f = request.POST.get('first_name')
        print(f)
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        print(user)
        user.save()
        return redirect('myaccount')

    return render(request, 'core/edit_myaccount.html')


def shop(request):
    categories = Category.objects.all()
    product = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        product = product.filter(category__slug=active_category)

    query = request.GET.get('query', '')
    price = request.GET.get('price','')
    year = request.GET.get('year','')

    if query:
        product = product.filter(
            Q(name__icontains=query) | Q(description__icontains=query)) 
    if price:
        product = product.filter(
            Q(price__icontains=price))
    if year:
        product = product.filter(
            Q(year__icontains=year))

    sort_by = request.GET.get("sort", "l2h") 
    if sort_by == "l2h":
           product = product.order_by("price")
    elif sort_by == "h2l":
        product = product.order_by("-price")

    context = {
        'products': product,
        'categories': categories,
        'active_category': active_category
    }

    return render(request, 'shop.html', context)

def editCategory(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        category.save()
        return redirect('shop')

    return render(request,'editCategory.html',{'category':category})

def CategoryAdd(request):
    cate = Category()
    if request.method == 'POST':
        cate.name = request.POST.get('name')
        cate.slug = request.POST.get('slug')
        cate.save()
        return redirect('shop')
    return render(request,'addCategory.html')

def CategoryDel(request,id):
    Category.objects.get(id=id).delete()
    
    return redirect('shop')


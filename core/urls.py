from django.urls import path
from core.views import frontpage
from core.views import shop 
from core.views import singup
from core.views import myaccount
from core.views import edit_myaccount
from core.views import editCategory 
from core.views import CategoryAdd
from core.views import CategoryDel
from product.views import addProd, product,deletePro,servises,add_servises,edit_serv,deleteServ
from django.contrib.auth import views

urlpatterns = [

    path('', frontpage, name='frontpage'),
    path('singup/', singup, name='singup'),
    path('shop/', shop, name='shop'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit', edit_myaccount, name='edit_acc'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/<slug:slug>/', product, name='product'),
    path('shop/category/edit/<int:id>',editCategory,name='editCat'),
    path('shop/addCategory',CategoryAdd,name='addCat'),
    path('shop/deliteCat/<int:id>',CategoryDel,name='deliteCat'), 
    path('shop/addProduct',addProd, name='addpro'),
    path('shop/delteproduct/<int:id>',deletePro,name='deletePro'),
    path('shop/servises',servises,name='serv'),
    path('shop/servises/add',add_servises,name='addserv'),
    path('shop/servises/edit/<int:id>',edit_serv,name='editserv'),
    path('shop/servises/delete/<int:id>',deleteServ,name='deleteserv'),
]

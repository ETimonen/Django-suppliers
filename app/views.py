from django.shortcuts import render, redirect
from .models import Supplier, Product
from django.contrib.auth import authenticate, login, logout


# LANDING AFTER LOGIN
'''
def landingview(request):
    return render(request, 'landingpage.html')
'''

# LOGIN AND LOGOUT
def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        context = {'name': user}
        return render(request,'landingpage.html',context)
    else:
        return render(request,'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request,'loginpage.html')

# PRODUCT VIEWS
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist,'suppliers': supplierlist}
        return render (request, "productlist.html", context)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']

        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)

def deleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Product.objects.get(id = id).delete()
        return redirect(productlistview)

def edit_product_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)

def edit_product_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        filteredproducts = productlist.filter(supplier = id)
        context = {'products': filteredproducts}
        return render (request,"productlist.html",context)


# SUPPLIER VIEWS
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request, "supplierlist.html", context)

def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)

def deletesupplier(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Supplier.objects.get(id = id).delete()
        return redirect(supplierlistview)

def edit_supplier_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"edit_supplier.html",context)

def edit_supplier_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supp = Supplier.objects.get(id = id)
        supp.companyname = request.POST['companyname']
        supp.contactname = request.POST['contactname']
        supp.address = request.POST['address']
        supp.phone = request.POST['phone']
        supp.email = request.POST['email']
        supp.country = request.POST['country']
        supp.save()
        return redirect(supplierlistview)

def searchsuppliers(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Supplier.objects.filter(companyname__icontains=search)
        context = {'suppliers': filtered}
        return render (request,"supplierlist.html",context)
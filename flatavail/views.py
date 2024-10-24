from django.shortcuts import render,redirect
from flatavail.models import category_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Frontend.models import contact_db
from django.contrib import messages
# Create your views here.
def index(req):
    return render(req,"index.html")

def category(req):
    return render(req,"Addcategory.html")

def save_category(req):
    if req.method=="POST":
        na = req.POST.get('name')
        det = req.POST.get('details')
        img = req.FILES['img']
        obj = category_db(Name=na,Description=det,Image=img)
        obj.save()
        messages.success(req,"Data Saved Successfully")
        return redirect(category)

def dis_category(req):
    category = category_db.objects.all()
    return render(req,"display_category.html",{'category':category})

def edit_category(req,dataid):
    category = category_db.objects.get(id=dataid)
    return render(req,"edit_category.html",{'category':category})

def update_category(req,dataid):
    if req.method=="POST":
        na = req.POST.get('name')
        det = req.POST.get('details')
        try:
            img = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = category_db.objects.get(id=dataid).Image
        category_db.objects.filter(id=dataid).update(Name=na,Description=det,Image=file)
        messages.success(req, "Data Edited Successfully")

        return redirect(dis_category)

def delete_category(req,dataid):
    category = category_db.objects.filter(id=dataid)
    category.delete()
    messages.success(req, "Data Deleted Successfully")
    return redirect(dis_category)

def product(req):
    category = category_db.objects.all()
    return render(req,"Addproduct.html",{'category':category})

def save_product(req):
    if req.method=="POST":
        cat = req.POST.get('cat')
        na = req.POST.get('name')
        des = req.POST.get('details')
        pri = req.POST.get('price')
        img = req.FILES['img']
        obj = product_db(Category_Name=cat,Product_Name=na,Product_Description=des,Product_Price=pri,Product_Image=img)
        obj.save()
        messages.success(req,"Data Saved Successfully")
        return redirect(product)

def display_product(req):
    product = product_db.objects.all()
    return render(req,"display_product.html",{'product':product})

def edit_product(req,dataid):
    category = category_db.objects.all()
    product = product_db.objects.get(id=dataid)
    return render(req,"edit_product.html",{ 'category':category,'product':product})

def update_product(req,dataid):
    if req.method=="POST":
        na = req.POST.get('cat')
        pa = req.POST.get('name')
        det = req.POST.get('details')
        pp = req.POST.get('price')
        try:
            img = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = product_db.objects.get(id=dataid).Product_Image
        product_db.objects.filter(id=dataid).update(Category_Name=na,Product_Name=pa,Product_Description=det,Product_Price=pp,Product_Image=file)
        messages.success(req, "Data Edited Successfully")

        return redirect(display_product)

def delete_product(req,dataid):
    product = product_db.objects.filter(id=dataid)
    product.delete()
    messages.success(req, "Data Deleted Successfully")

    return redirect(display_product)

def adminlogin(req):
    return render(req,"Adminlogin.html")

def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('user_name')
        psw = request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=psw)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=psw
                messages.success(request, "Login Successfully")
                return redirect(index)

            else:
                messages.error(request, "Login Failed")

                return redirect(adminlogin)
        else:
            messages.error(request, "Login Failed")

            return redirect(adminlogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)


def dis_contact_frontend(req):
    contact = contact_db.objects.all()
    return render(req,"display_contact_page.html",{'contact':contact})

def delete_contact(req,dataid):
    contact = contact_db.objects.filter(id=dataid)
    contact.delete()
    return redirect(dis_contact_frontend)

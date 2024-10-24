from django.shortcuts import render,redirect
from flatavail.models import category_db,product_db
from Frontend.models import contact_db,register_db,cart_db
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat = category_db.objects.all()
    return render(request,"Home.html",{'cat':cat})

def products(request):
    cat = category_db.objects.all()
    pro = product_db.objects.all()
    return render(request,"products.html",{'pro':pro,'cat':cat})

def cat_product(request,cat_name):

    data = product_db.objects.filter(Category_Name=cat_name)
    return render(request,"cat_product.html",{'data':data})

def single_product(req,proid):
    cat = category_db.objects.all()
    data = product_db.objects.get(id=proid)
    return render(req,"single_product.html",{'data':data,'cat':cat})


def about_us_page(request):
    cat = category_db.objects.all()
    return render(request,"aboutus.html",{'cat':cat})

def contact_us_page(request):
    cat = category_db.objects.all()
    return render(request,"contact_us.html",{'cat':cat})

def service_page(request):
    cat = category_db.objects.all()
    return render(request,"service.html",{'cat':cat})

def save_contact(request):
    if request.method=="POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        loc = request.POST.get('city')
        cou = request.POST.get('country')
        zi = request.POST.get('zipcode')
        tel = request.POST.get('tel')
        obj = contact_db(First_name=fn,Last_name=ln,Email_id=em,Address=ad,City=loc,Country=cou,Zip_code=zi,Telephone=tel)
        obj.save()
        return redirect(contact_us_page)

def sign_page(req):
    return render(req,"sign_in_up_page.html")

def register_page(req):
    if req.method=="POST":
        na = req.POST.get('name')
        no = req.POST.get('number')
        em = req.POST.get('email')
        un = req.POST.get('username')
        psd = req.POST.get('password')
        obj = register_db(Name=na,Mobile=no,Email=em,Username=un,Password=psd)
        obj.save()
        return redirect(sign_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        psw = request.POST.get('password')
        if register_db.objects.filter(Username=un,Password=psw).exists():
            request.session['Username'] = un
            request.session['Password'] = psw
            messages.success(request, "Login Successfully")
            return redirect(homepage)
        else:
            messages.error(request, "Login Failed")
            return redirect(sign_page)
    return redirect(sign_page)

def Userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(sign_page)

def cart_page(request):
    data = cart_db.objects.filter(username=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"cart.html",{'data':data,'total_price':total_price})

def save_cart(req):
    if req.method=="POST":
        un = req.POST.get('username')
        pn = req.POST.get('pname')
        qn = req.POST.get('quantity')
        tp = req.POST.get('tprice')
        des = req.POST.get('pdes')
        obj = cart_db(username=un,Product=pn,quantity=qn,TotalPrice=tp,Description=des)
        obj.save()
        messages.success(req, "Item is added to cart Successfully")
        return redirect(homepage)

def delete_cart_product(req,dataid):
    data = cart_db.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Item removed Successfully")
    return redirect(cart_page)

def checkout(request):
    data = cart_db.objects.filter(username=request.session['Username'])

    return render(request,"checkout.html",{'data':data})
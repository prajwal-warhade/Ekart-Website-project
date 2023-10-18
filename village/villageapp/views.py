from django.shortcuts import render,redirect,HttpResponse
from django.views import View 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from villageapp.models import Product,Cart,Order
from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail
# Create your views here.

def products(request):
    uid=request.user.id     #to find who logged user
    p=Product.objects.filter(is_active=True)           #data fetch here from models.py file
    dictionary={}
    dictionary['data']=p 
    
    ''' dictionary is a dictionary=>this dictionary have key named 'data' and
        =>that key have vlaue of 'p' and
        => iside of p there is list of products
        => and that list contains obj1,obj2,obj3'''
        
    return render(request,'index.html',dictionary)  

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    context={}
    if request.method == 'GET': 
        return render(request,'register.html')
    else:
        n=request.POST['uname']
        p=request.POST['upass']
        c=request.POST['ucpass']
        if n=='' or p=='' or c=='': # any filed is blank
            context['Error']='filed cannot be Blank'
            return render(request,'register.html',context)
        elif p!=c:# if passwords dosent match 
            context['Error']='Password Dosent matched'
            return render(request,'register.html',context)
        elif len(p)<8:
            context['Error']='password should contains 8 characters'
            return render(request,'register.html',context)
        else:
            try:   #for mssg already user found 
                u=User.objects.create(username=n,)
                u.set_password(p)#password will be in encripted format
                u.save()
                context['Success']='User Registration Successful'
                   
            except Exception:
                context['Error']='Already Exist'
                return render(request,'register.html',context)

def Product_DE(request,pid):
    p=Product.objects.filter(id=pid)
    context={}
    context['data']=p
    return render(request,'product_D.html',context)

def user_login(request): 
    
    if request.method=="GET":
        return render(request,'login.html')
    else:
        n=request.POST['uname']
        p=request.POST['upass']
        u=authenticate(username=n,password=p)#for authentication of user.
       #print(u)
        if u is not None:
            login(request,u)
            return redirect('/products')
        else: 
            context={}#if login credentials wrong
            context['Error']='Invalid Username or Password'
            return render(request,'login.html',context)
        
def user_logout(request):
    logout(request)#distroy the session id
    return redirect('/products')  

def catfilter(request,cp):
    q1=Q(cat=cp)
    q2=Q(is_active=True)
    
    p=Product.objects.filter(q1&q2)#if both conditions true q1 and q2 data fetch in p object.
    dictionary={}
    dictionary['data']=p
    return render(request,'products.html', dictionary)

def cart(request,pid):
    if request.user.is_authenticated:
        
        a=User.objects.filter(id=request.user.id)#request.user.id:- returns sessions userid whos loggedin
        p=Product.objects.filter(id=pid)
        
        q1=Q(userid=a[0])
        q2=Q(pid=p[0])
        b=Cart.objects.filter(q1 & q2)
        L=len(b)
        print(L)
        context={}

        context['data']=p 
        #shows product details in pop up message
        
        if L==1:
            context['message']="Product Already in cart..."# this is sends message views to templates file.
        else:
            b=Cart.objects.create (userid=a[0],pid=p[0])
            b.save()
            context['message']="Product Added Successfully..."
                
        return render(request,'Product_D.html',context)
        
            
    else:
        return redirect('/login')
    
def viewcart(request):
    
    c=Cart.objects.filter(userid=request.user.id)#request.user.id:- returns sessions userid whos loggedin
    print(c)
    print(c[0].userid)
    sum=0
    for x in c:
        sum=sum + x.pid.price*x.qty
    context={}
    context['data']=c
    context['total']=sum
    
    context['n']=len(c)
    
    return render(request,'cart.html',context)

def updateqty(request,x,cid):
    c=Cart.objects.filter(id=cid)
    q=c[0].qty
    if x=='1':
        q=q+1
    elif q>1:
        q=q-1
    
    c.update(qty=q)
    return redirect('/viewcart')

def removecart(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/products')
def placeorder(request):
    '''this function use for when 
    user placed order this function remove data from cart and add to order table,'''
    c=Cart.objects.filter(userid=request.user.id )
    #request.user.id:- returns data from sessions userid whos logged in
    orderid=random.randrange(1000,9999)
    for x in c:
        amount=x.qty*x.pid.price
        o=Order.objects.create(orderid=orderid,qty=x.qty,pid=x.pid,userid=x.userid,amt=amount)
        o.save()# records added in order table
        x.delete()# after that data will be removed whe payment successful.
        #create method used for inserting Data
    return redirect('/fetchorder')

def fetchorder(request):
    orders=Order.objects.filter(userid=request.user.id)
    #to send msg to html file make dictionary
    context={}
    context['data']=orders
    return render(request,"placeorder.html",context)

def makepayment(request):
    client = razorpay.Client(auth=("rzp_test_aOpdJJYWcJjPan","TjlzhCU8PPBW7Cu59HC8KaZq"))
    order=Order.objects.filter(userid=request.user.id)
    sum=0
    for x in order:
        sum=sum+x.amt
        oid=x.orderid
    data = { "amount":sum*100, "currency": "INR", "receipt":"oid" }
    payment = client.order.create(data=data)
    context={}
    context['payment']=payment
    return render(request,'pay.html',context)

def paysuccess(request):
    sub='Ekart-Order Stutus'
    msg='Thanks FOr Shoping'
    frm='prajwalwarhade07@gmail.com'
    u=User.objects.filter(id=request.user.id)
    to=u[0].email
    
    send_mail(
        sub,
        msg,
        frm,
        [to],
        fail_silently=False
    )
    return render(request,'paysuccess.html')




'''def seedfilter(request,sd):
    q1=Q(seed=sd)
    q2=Q(is_active=True)
    
    s=Product.objects.filter(q1&q2)
    print(s)
    dictionary={}
    dictionary['data']=s
    return render(request,'products.html', dictionary)'''
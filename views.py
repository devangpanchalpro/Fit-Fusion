from django.shortcuts import render,redirect
from .models import *
import random
from django.core.mail import send_mail
from django.conf import settings
import razorpay
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        context = {
            'uid' : uid
        }
        return render(request, "myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")

def about(request):
    return render(request, "myapp/about.html")

def course(request):
    return render(request,"myapp/courses.html")

def price(request):
    return render(request,"myapp/price.html")

def gallery(request):
    return render(request,"myapp/gallery.html")

def blog(request):
    return render(request,"myapp/blog.html")

def contact(request):
    if request.POST:
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        uid = Contact_Us.objects.create(message=message,name=name,email=email,subject=subject)
        context = {
            'uid' : uid
        }

        return render(request,"myapp/contact.html",context)
    
    else:

        return render(request,"myapp/contact.html")

def login(request):
    if "email" in request.session:

        uid = User.objects.get(email=request.session['email'])
        context = {
            'uid' : uid
        }
        return render(request, "myapp/index.html",context)
    else:
        if request.POST:
            email = request.POST['email']
            password  = request.POST['password']

            uid = User.objects.get(email=email)

            if uid.password == password:

                request.session['email'] = uid.email

                context = {
                    'uid' : uid
                }
                return render(request, 'myapp/index.html',context)
            else:
                
                n_msg = "invalid password"

                context = {
                    'n_msg' : n_msg
                }

                return render(request,"myapp/login.html",context)
                
            
        else:
            return render(request,"myapp/login.html")
                

       
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def register(request):
    
       if request.POST:
           username = request.POST['username']
           email = request.POST['email']
           password = request.POST['password']

           uid = User.objects.create(username=username,
                                     email=email,
                                     password=password,

                                     )
           context = {
               'uid' : uid,

           }

           return render(request,"myapp/login.html",context)
       
       else:
           return render(request,"myapp/register.html")
       

def blog_details(request):
    if request.POST:
        comment = request.POST['comment']
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
    
        uid = leave_reply.objects.create(comment=comment,name=name,email=email,website=website)
        context = {
            'uid' : uid
        }

        return render(request,"myapp/blog_details.html",context)
    else:
        return render(request,"myapp/blog_details.html")


def elements(request):
    
  return render(request,"myapp/elements.html")

def supplement(request):
    uid = Add_product.objects.all()
    context ={
        'uid' : uid
    }
    return render(request,"myapp/supplement.html",context)

def forget_password(request): 
    if request.POST:
        email = request.POST['email']
        otp = random.randint(1111,9999)
        try:
            uid = User.objects.get(email=email)
            if uid.email == email:
                uid.otp = otp
                uid.save()
                send_mail("forgot password","your otp is"+str(otp),"gohiljayb10@gmail.com",[email] )
                context ={
                    'email' : email
                }
                return render(request, "myapp/confirm_password.html",context)
            else:

                context={
                    'e_msg' :"INVALID PASSWORD"
                }
                return render(request,"myapp/forget_password",context)


        except:

            e_msg = "INVALID PASSWORD"

            context={
                'e_msg' : e_msg

            }
            return render(request,"myapp/forget_password",context)
        
    else:
        return render(request,"myapp/forget_password.html")
            

        
             

def confirm_password(request):
    if request.POST:
        
        otp = request.POST['otp']
        email = request.POST['email']
        new_passwpord = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        uid = User.objects.get(email=email)
        if str(uid.otp) == otp:
            if new_passwpord == confirm_password:
                uid.password = new_passwpord
                uid.save()
                context ={
                    'email' :  email,
                    'uid' : uid
                }

                return render(request,"myapp/login.html",context)
            else:
                context={
                    'p_msg' : "INVALID PASSWORD"
                }
                return render(request,"myapp/confirm_password.html",context)
            
        else:

            context={

                'e_msg' : " INVALID OTP "

            }
            return render(request,"myapp/confirm_password.html",context)
        
    else:
       
        return render(request,"myapp/confirm_password.html")
            


def home(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        context = {
            'uid' : uid
        }
        return render(request, "myapp/index.html",context)
    else:
        return render(request,"myapp/home.html")
    

def shop(request):
    pid=product.objects.all()
    bid=branding.objects.all()    
    cid=prize.objects.all()    

    b_id=request.GET.get("b_id")
    print(b_id)

    c_id=request.GET.get("c_id")
    print(c_id)
    
    if b_id:
        pid=product.objects.filter(branding_id=b_id) 
    elif c_id:
        pid=product.objects.filter(prize_id=c_id)
    else:
        pid=product.objects.all()

    
    paginator=Paginator(pid,6)
    page_number=request.GET.get("page")
    pid = paginator.get_page(page_number)

    contaxt={
        "pid":pid,
        "bid":bid,
        "cid":cid,
    }
    return render(request,"myapp/shop.html",contaxt)  


    

          


def detail(request):
    uid=User.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(user_id=uid)
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)  
    total=sub_total  
   
    contaxt={
        "aid":aid,
        "sub_total":sub_total,
        "total":total,
        "uid":uid,
    }
    return render(request,"myapp/detail.html",contaxt)

def add_to_cart(request,id):
    pid=product.objects.get(id=id)
    print(pid)
    uid=User.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(product_id=pid,user_id=uid).exists()
    if aid:
        aid=add_cart.objects.get(product_id=pid,user_id=uid)
        aid.qty+=1  
        aid.total=aid.qty*aid.price
        aid.save()
        return redirect("detail")
    else:
        add_cart.objects.create(user_id=uid,product_id=pid,img=pid.img,name=pid.name,price=pid.price,qty=1,total=pid.price)
        return redirect("detail")

def cart_delete(request,id):
    aid=add_cart.objects.get(id=id)
    aid.delete()
    return redirect("detail")

def cart_plus(request,id):
    aid=add_cart.objects.get(id=id)
    aid.qty+=1
    aid.total=aid.qty*aid.price
    aid.save()
    return redirect("detail")

def cart_minus(request,id):
    aid=add_cart.objects.get(id=id)
    aid.qty-=1
    aid.total=aid.qty*aid.price
    aid.save()
    if aid.qty==0:
        aid.delete()
    return redirect("detail")

    

def checkout(request):
    uid=User.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(user_id=uid)
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)  
    total=sub_total  
    amount = total*100 #100 here means 1 dollar,1 rupree if currency INR
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    print(response,"")

    contaxt={
        "aid":aid,
        "total":total,
        "sub_total":sub_total,
        "response":response,

    }


    return render(request,"myapp/checkout.html",contaxt)
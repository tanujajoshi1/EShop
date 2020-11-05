from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import View
############## hashing your password ###############
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

class Index(View):
    def get(self,request):
        # request.session.get('cart').clear()
        items= None
        categories=Category.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
            items=Product.get_all_products_by_id(categoryID)
        else:
            items=Product.get_all_products()
        return render(request,'index.html',{'data':items,'category':categories})

    def post(self,request):
        products= request.POST.get('products')
        cart= request.session.get('cart')
        if cart:
            quantity= cart.get(products)
            if quantity:
                cart[products]=1+quantity
            else:
                cart[products]=1
        else:
            cart={}
            cart[products]=1
        request.session['cart']=cart
        return redirect('/')





def signUp(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        fname= request.POST['firstname']
        lname= request.POST['lastname']
        phone= request.POST['phone']
        email= request.POST['email']
        password= request.POST['password']
        confirmation=request.POST['confirmation']

        ##### Validation #####
        error_message= None
        if not fname:
            error_message= "First Name Required !"
        elif not lname:
            error_message= "Last Name Required !"
        elif not email:
            error_message= "Email field required !"
        elif not phone or len(phone)<10:
            error_message= "Phone number should not be less than 10 digits !"        
        elif not password or len(password)<6:
            error_message= "Password should be atleast 6 characters long"
        elif password !=confirmation:
            error_message= "Password must match"
        #3333333333333 checks if the email is already registered #3333333333
        elif Customer.objects.filter(email=email):
            error_message= "This email is already registered"

        if not error_message:
        
            customer=Customer(fname=fname,lname=lname,phone=phone,email=email,password=password)

            ############## hashing your password and replacing the password field with hased password ###############
            customer.password= make_password(customer.password)
            ############## hashing your password and replacing the password field with hased password ###############

            customer.save()
            return render(request,'login.html',{'message':"Sign up is done successfully. You may login now"})
        else:
            return render(request,'signup.html',{'message':error_message,'fname':fname,'lname':lname,'email':email,'phone':phone})
       

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email= request.POST['email']
        password= request.POST['password']

        error_message=None
        customer=Customer.objects.get(email=email)

        if check_password(password,customer.password):
            request.session['customer_id']=customer.id  ##saving to session
            request.session['email']=customer.email
            user=request.session.get('email')
            return render(request,'index.html',{user:'user'})
        else:
            error_message="Email / Password invalid"
            return render(request,'login.html',{'error_message':error_message})



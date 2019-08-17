from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm,RegisterForms
from .models import Register
from products.models import Product
from cart.models import Cart
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
User=get_user_model()
def shakes(request):
    return render(request,'aj.html')
def fruit(request):
    return render(request,'fruit.html')
def about(request):
    return render(request,'abouts.html')
def review(request):
    return render(request,'intro.html')
def register(request):
    context={"form":RegisterForms}
    return render(request,'register.html',context)
def adduser(request):
    form=RegisterForms(request.POST)
    if form.is_valid():
        register=Register(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                              email=form.cleaned_data['email'])
        register.save()
        messages.add_message(request, )
    return redirect('contact')
def contact(request):
    return render(request,'contact.html')
def signup(request):
    context={"form":RegisterForms}
    return render(request,'signup.html',context)
def login_view(request):
    next=request.GET.get('next')
    art=Register.objects.all()
    form=UserLoginForm(request.POST or None)
    context={'form':form} 
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        #for i in art:
           # if i.username==username:
          #      p=i
         #       break
        #context['username']=p
        p=Product.objects.all()
        z=p[:20]
        q=p[20:31]
        u=p[31:39]
        k=p[39:]
        c=Cart()
        c.save()
        m=Register.objects.get(username=username)
        m.prof.add(c)
        if request.user.is_authenticated:
            context={'username': request.user, 'product': z, 'juice': q, 'shake': u, 'cake': k}    
        return render(request,'test.html',context)   
    return render(request,'contact.html',context)   
def register_view(request):
    next=request.GET.get('next')
    form=RegisterForms(request.POST or None)
    
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(request,new_user)
        register=Register(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                              email=form.cleaned_data['email'])
        register.save()
        messages.add_message(request,messages.INFO,"You have registered successfully,now login")
        p=1
        if next:
            return redirect(next)
        return redirect('contact')
    
    context={'form':form}    
    return render(request,'signup.html',context)
def menu(request):
    return render(request,'menu.html')
def test(request):
    p=Product.objects.all()
    z=p[:20]
    q=p[20:31]
    u=p[31:39]
    k=p[39:]
    cart=Cart.objects.all()
    l=len(cart)
    carts=cart[l-1]
    c=carts.products.all()
    l=len(c)
    if request.user.is_authenticated:
        context={'product': z,'juice': q,'shake': u,'cake': k,'username': request.user,'num': l}
    return render(request,'test.html',context)
def single(request,slug):
    p=Product.objects.get(slug=slug)
    cart=Cart.objects.all()
    l=len(cart)
    carts=cart[l-1]
    c=carts.products.all()
    if p not in c:
        carts.products.add(p)
    else:
        carts.products.remove(p)
        new_total=0.00
        for item in carts.products.all():
            new_total+=float(item.price)
        carts.total=new_total
        carts.save()
        context={"cart": carts, 'username': request.user}
        return render(request,'cart.html',context)
    new_total=0.00
    for item in carts.products.all():
        new_total+=float(item.price)
    carts.total=new_total
    carts.save()     
    if request.user.is_authenticated:
        context={'toy': p,'username': request.user}
    return render(request,'menu.html',context)
def carts(request):
    carts=Cart.objects.all()
    l=len(carts)
    cart=carts[l-1]
    context={"cart": cart, 'username': request.user}
    return render(request,'cart.html',context)
def cart_update(request):
    cart=Cart.objects.all()[0]
    new_total=0.00
    for item in cart.products.all():
        new_total+=item.price
    cart.total=new_total
    cart.save()
    context={"cart": cart}
    return render(request,'cart.html',context)
def delete(request,slug):
    carts=Cart.objects.all()
    l=len(carts)
    cart=carts[l-1]
    p=Product.objects.get(slug=slug)
    cart.products.remove(p)
    cart.save()
    context={"cart": cart}
    return render(request,'cart.html',context)
def reward(request):
    return render(request,'reward.html')
def profile(request):
    if request.user.is_authenticated:
        p=request.user
        username=request.user.username
    m=Register.objects.get(username=username)
    q=m.prof.all()
    l=len(q)
    if l>=2:
        z=q[l-2]
    context={'data':q,'username':p,'last': z}
    return render(request,'profile.html',context)
def ship(request):
    return render(request,'ship.html')
def branch(request):
    return render(request,'branch.html')
def cont(request):
    return render(request,'cont.html')
def test2(request):
    p=Product.objects.all()
    z=p[:20]
    q=p[20:31]
    u=p[31:39]
    k=p[39:]
    context={'product': z,'juice': q,'shake': u,'cake': k}
    return render(request,'test2.html',context)
def logout_view(request):
    logout(request)
    return render(request,'fruit.html')
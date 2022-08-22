from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from Eshop.models import E_Shop

def home(request):
    return render(request,'index.html')

def log_read(request):
    if request.method == 'POST':
        user_name = request.POST['txtemail']
        user_pswd = request.POST['txtpswd']
        user = authenticate(request,username=user_name,password=user_pswd)
        resp = ''
        if user is not None:
             if user.is_superuser:
                login(request, user)
                return render(request,"Home.html")
        else:
            return redirect('home')

    else:
        resp=HttpResponse('Credintials are not correct')
    return resp

def Products(request):
    p1 = E_Shop.objects.all()
    return render(request, 'show_products.html', {'products':p1})

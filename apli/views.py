from django.shortcuts import render
from .models import Producto
from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import FormUser
from .models import User
# Create your views here.
def home(request):
    return render (request, 'home.html')
def logout_view(request):
    logout(request)
    return redirect('/')
def producto(request):
    productos=Producto.objects.all()
    return render (request, 'producto.html',{'productos':productos})

def carrito(request):
    return render(request,'carrito.html')

def register(request):
    data={'form':CustomUser()}
    if request.method=='POST':
        user_creation_form= CustomUser(data=request.POST)
        if user_creation_form.is_valid():
            print ('se creo')
            user_creation_form.save()
            return redirect('/')
        else:
            print ('no se creo')
            print(user_creation_form.errors)
    else:
        user_creation_form = CustomUser()
    return render(request, 'registration/register.html',data)
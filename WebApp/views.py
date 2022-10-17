from django.shortcuts import render, redirect
from django.http import HttpResponse
from WebApp.models import *
from WebApp.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request,'home.html',{'avatar' : avatar})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username=user, password=pwd)
            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'home.html', {'avatar' : avatar})
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})
def register(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)       
        #print(form)# debugeee
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect("/login")
        else:#decidi regresar el formulario con error
            return render(request, "register.html", {'form': form})
    #form = UserCreationForm()

    form = UserRegisterForm()
    return render(request, "register.html", {'form': form})

@login_required
def perfil(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "perfil.html",{'avatar' : avatar})

def blogs(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "blogs.html",{'avatar' : avatar})

def about(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "about.html",{'avatar' : avatar})

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'home.html')
        else:
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request,'home.html',{'avatar' : avatar})
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
    return render(request, 'editarPerfil.html', {'form': form, 'usuario': usuario})

@login_required
def changepass(request):
    usuario= request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request,'home.html',{'avatar' : avatar})
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_pass.html', {'form': form, 'usuario': usuario})

def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request,'home.html',{'avatar' : avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})

def cuidado(request):
    return render(request, 'blogs/cuidados.html')

def estilo1(request):
    return render(request, 'blogs/estilo1.html')
def estilo2(request):
    return render(request, 'blogs/estilo2.html')
def estilo3(request):
    return render(request, 'blogs/estilo3.html')
def estilo4(request):
    return render(request, 'blogs/estilo4.html')
def estilo5(request):
    return render(request, 'blogs/estilo5.html')
def estilo6(request):
    return render(request, 'blogs/estilo6.html')
def estilo7(request):
    return render(request, 'blogs/estilo7.html')
def estilo8(request):
    return render(request, 'blogs/estilo8.html')
def estilo9(request):
    return render(request, 'blogs/estilo9.html')
def estilo10(request):
    return render(request, 'blogs/estilo10.html')
def estilo11(request):
    return render(request, 'blogs/estilo11.html')
def estilo12(request):
    return render(request, 'blogs/estilo12.html')
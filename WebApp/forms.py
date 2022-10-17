from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = "Usuario", widget = forms.TextInput())
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre", widget = forms.TextInput())
    last_name = forms.CharField(label = "Apellido", widget = forms.TextInput())
    password1 = forms.CharField(label = "Ingresa una contraseña", widget = forms.PasswordInput())
    password2 = forms.CharField(label = "Repite la contraseña", widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        help_texts: {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Usuario'}))
    Email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Correo'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Apellido'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Insertar Contraseña'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']
        help_texts = {k: "" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Antigua Contraseña", }))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Nueva Contraseña"}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirmar Contraseña"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()

class PostsForm(forms.Form):

    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=1000)
    autor = forms.CharField(max_length=40)
    fecha = forms.DateField()

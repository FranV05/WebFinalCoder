"""WebFinalCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from WebApp.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login_request),
    path('register/', register),
    path('logout/', LogoutView.as_view(template_name = 'home.html'),name="Logout"),
    path('about/', about),
    path('blogs/', blogs),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changepass),
    path('perfil/', perfil),
    path('perfil/changeAvatar', agregarAvatar),
    path('blogs/cuidados', cuidado),
    path('blogs/estilo1', estilo1),
    path('blogs/estilo2', estilo2),
    path('blogs/estilo3', estilo3),
    path('blogs/estilo4', estilo4),
    path('blogs/estilo5', estilo5),
    path('blogs/estilo6', estilo6),
    path('blogs/estilo7', estilo7),
    path('blogs/estilo8', estilo8),
    path('blogs/estilo9', estilo9),
    path('blogs/estilo10', estilo10),
    path('blogs/estilo11', estilo11),
    path('blogs/estilo12', estilo12),
    path('posts/', PostsList.as_view(), name="Posts"),
    path('new/', PostCreate.as_view(), name="Create"),
    path('<pk>/', PostDetail.as_view(), name="Detail"),
    path('update/<pk>', PostUpdate.as_view(), name="Update"),
    path('delete/<pk>', PostDelete.as_view(), name="Delete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
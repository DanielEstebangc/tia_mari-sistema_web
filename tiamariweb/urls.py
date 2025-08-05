

"""
URL configuration for tiamariweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import RedirectView
from inventario import views as inventario_views  # o cambia el nombre según tu app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),  # aquí se enlazan las rutas del app
    path('', inventario_views.inicio, name='inicio'),

    # path('', RedirectView.as_view(url='/inventario/', permanent=False)),  # <-- redirección aquí


    
]

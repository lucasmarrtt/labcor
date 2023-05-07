"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from home import views 

# Media config
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authenticated
    path('', views.index, name='index'),
    path('logout/', views.logoutU, name='logout'),

    # Pages
    path('google/', views.google, name='google'),
    #path('instagram/', views.instagram, name='instagram'),

  
    
    path('busca-avancada/', views.advanced_search, name='busca-avancada'),

    path('global/', views.global_view, name='global'),


  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Admin 
admin.AdminSite.site_header = 'System'
admin.AdminSite.site_title = 'System'
admin.AdminSite.index_title = 'System'
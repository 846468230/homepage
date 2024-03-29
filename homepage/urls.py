"""homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import xadmin
from django.conf import settings
from django.urls import path,include,reverse,reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
urlpatterns = [
    path('dashboard/',include('dashboard.urls')),
    path('',RedirectView.as_view(url=reverse_lazy('dashboard:homepage',args=[1]))),
    path('admin/', xadmin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

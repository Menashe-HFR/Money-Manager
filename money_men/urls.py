"""
URL configuration for money_men project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path


def my_web(request):
    return HttpResponse("Hello, This is the HomePage of MoneyMen!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}")


def hello_name_repeat(request, name, times=1):
    return HttpResponse(f"Hello, {name * times}")


urlpatterns = [
    path("", my_web),
    path("hello/<name>/", hello_name),
    path("hello/<name>/", hello_name),
    path("hello/<name>/<int:times>/", hello_name_repeat),
    path("admin/", admin.site.urls),
]

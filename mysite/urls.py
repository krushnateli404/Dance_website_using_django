"""mysite URL Configuration

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
from django.urls import path
from . import views
from . import views1

#This for file views.py
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name = 'index'),
#     path('about',views.about,name = 'about')
# ]

#This is for views1.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views1.index,name = 'index'),
    path('analyze',views1.analyze,name= 'analyze'),
    path('about/',views1.about,name= 'about'),
    path('contaact/',views1.contaact,name= 'contaact'),
    # path('ex1',views1.ex1,name = 'ex1'),
    # path('newlineremove', views1.newlineremove, name='newlineremove'),
    # path('spaceremove', views1.spaceremove, name='spaceremove'),
    # path('charcount', views1.charcount, name='charcount'),



]

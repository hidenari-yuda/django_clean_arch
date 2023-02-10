from django.urls import path
from gadget_app.controllers.router import mgadget_handler, mgadget_id_handler


urlpatterns = [
    path('<str:id>', mgadget_id_handler),
    path('', mgadget_handler),
    path('mgadget/<str:id>', mgadget_id_handler),
]

# """django_clean_arch URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import include, path


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('gadgets/', include('gadget_app.urls')),
# ]

"""
URL configuration for rentify_car project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rentify_car_app import views
from rentify_car_app.views import Signup
from rentify_car_app.views import Login,logout
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout',logout,name='logout'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.disp_service,name='service'),
    path('add_service/',views.add_service,name='add_service'),
    path('book_service/',views.book_services,name='book_service'),
    path('cars/',views.disp_car,name='cars'),
    path('add_car/',views.add_car,name='add_car'),
    path('team/',views.disp_team,name='team'),
    path('add_team/',views.add_team_member,name='add_team'),
    path('review/',views.disp_review,name='review'),
    path('add_review/',views.add_review,name='add_review'),
    path('update_service/<int:service_id>',views.edit_service,name='update_service'),
    path('delete_service/<int:service_id>',views.delete_service,name='delete_service'),
    path('update_team/<int:team_id>',views.edit_team,name='update_team'),
    path('delete_team/<int:team_id>',views.delete_team,name='delete_team'),
    path('update_car/<int:car_id>',views.edit_car,name='update_car'),
    path('delete_car/<int:car_id>',views.delete_car,name='delete_car'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
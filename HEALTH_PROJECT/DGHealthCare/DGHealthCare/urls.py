"""DGHealthCare URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from healthify import views
urlpatterns = [
    path('healthify/',include('healthify.urls')),
    path('admin/', admin.site.urls),
    path('',views.homeView,name='home'),
    path('account/',include('Accountsapp.urls')),
    path('admindata/',views.adminView,name='admindata'),
    path('appoint/',views.addAppointmentView,name='appoint'),
    path('delete/<int:id>/',views.deleteAppointmentView,name='delete'),
    path('showappoint/',views.showAppointmentView,name='show'),
    path('addambulance/',views.addAmbulanceView,name='addambulance'),
    path('deleteambulance/<int:id>/',views.deleteAmbulanceView,name='deleteambulance'),
    path('showambulance/',views.showAmbulanceView,name='showambulance'),
    path('adddoctor/',views.addDoctorView,name='adddoctor'),
    path('showdoctor/',views.showDoctorView,name='showdoctor'),
    path('updatedoctor/<int:id>/',views.updateDoctorView,name='updatedoctor'),
    path('deletedoctor/<int:id>/',views.deleteDoctorView,name='deletedoctor'),
    path('addnursingstaff/',views.addNursingStaffView,name='addnursingstaff'),
    path('shownursingstaff/',views.showNursingStaffView,name='shownursingstaff'),
    path('updatenursingstaff/<int:id>/',views.updateNursingStaffView,name='updatenursingstaff'),
    path('deletenursingstaff/<int:id>/',views.deleteNursingStaffView,name='deletenursingstaff'),
    path('addroomservicestaff/',views.addRoomServiceStaffView,name='addroomservicestaff'),
    path('showroomservicestaff/',views.showRoomServiceStaffView,name='showroomservicestaff'),
    path('updateroomservice/<int:id>/',views.updateRoomServiceStaffView,name='updateroomservice'),
    path('deleteroomservice/<int:id>/',views.deleteRoomServiceStaffView,name="deleteroomservice"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
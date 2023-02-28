
from django.contrib import admin
from django.urls import path


from django_kibrudashboard.views import(
    kibru_Admin_Site_View
)
app_name="django_kibrudashboard"
urlpatterns = [
    path("dashboard/", kibru_Admin_Site_View,name="dashboard"),
    
]

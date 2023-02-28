from django.http import JsonResponse
from django.shortcuts import redirect,render

# Admin View
def kibru_Admin_Site_View(request ,*args, **kwargs): 
    return redirect("admin:index")
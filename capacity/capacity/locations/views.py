from django.shortcuts import render
from django.views.generic.list import ListView
from locations.models import Location
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

# from django.contrib.auth import get_user_model
# User = get_user_model()
# from django.contrib.auth.models import User

# user = User.objects.get(username=User111)

# Create your views here.

class LocationsListView(ListView):
    model = Location

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print ("-----------------------------------------------------")
    #     print (context)
    #     print ("-----------------------------------------------------")
    #     # print(str(User.last_login))
    #     return context  
    
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     print (str(qs))      
    #     return qs



    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     search = self.request.GET.get("search", 0)
    #     if search != 0:
    #         return qs.filter(name__icontains=search)
    #     return qs
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     f = SearchForm()
    #     context["form"] = f       
    #     return context
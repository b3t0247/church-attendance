from django.shortcuts import render
from django.urls import path

def root(request):
    return render(request, "home.html")

urlpatterns = [
    path("", root),
]

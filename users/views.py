# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def registration(request):
#     return HttpResponse("<h1>Registration</h1>")
#
# def login(request):
#     return HttpResponse("<h1>Welcome to login</h1>")

from django.shortcuts import render
def login(request):
    return render(request,"myusers/login.html")
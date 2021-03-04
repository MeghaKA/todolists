from django.shortcuts import render

# Create your views here.
def get_addition(request):
    return render(request,"mymath/addition.html")
def calculate(request):
    num1=int(request.POST.get("num1"))
    num2=int(request.POST.get("num2"))
    res=num1+num2
    context={}
    context["reslt"]=res
    return render(request,"mymath/addition.html",context)

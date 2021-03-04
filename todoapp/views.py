from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def get_taskpage(request):

def create_task(request):
    # return HttpResponse("<h1>createTask</h1>")
    # print("inside create_task")
    # my_task=request.POST.get("task")
    # # print(my_task)
    # context={}
    # context["result"]=my_task
    return render(request,"todoapp/createTask.html",)

def addTask(request):
    # print("inside add task view")
    my_task=request.POST.get("task")
    print(my_task)
    return HttpResponse("<h1>add your task</td>")

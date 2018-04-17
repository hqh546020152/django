from django.shortcuts import render
from cmdb import models
from django.http import HttpResponseRedirect

from django.shortcuts import HttpResponse
# Create your views here.

user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]
def index(request):
    if request.method== "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username,pwd=password)
        #print(username,password)
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)
    user_list = models.UserInfo.objects.all()
    #request.POST
    #request.GET
    #return HttpResponse("hello world!")
    return render(request, "index.html",{"data":user_list})

def hello(request):
    #return HttpResponse("hello world!")
    return render(request, "hello.html")

def online(request):
    #print(models.get_messages())
    context = {'messages': models.get_messages()}
    return render(request, "online/index.html",context)

def create(request):
    return render(request, "online/create.html")

def save(request):
    usrname = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    #print(username,title,content)
    #models.save_message(username, title, content)
    models.save_message(usrname, title, content)
    return HttpResponseRedirect('/online')

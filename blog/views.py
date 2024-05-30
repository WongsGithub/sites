from django.http import JsonResponse

from django.shortcuts import get_object_or_404, render
from .models import Blog,User

def index(request):
    return render(request, "blog/login.html")

def blog(request):
    return render(request, "blog/index.html")

def sign(request):
    uname = request.POST["username"]
    pass1 = request.POST["password"]
    pass2 = request.POST["password1"]
    users = User.objects.all()
    if pass1 != pass2:
        return JsonResponse("The password and confirmation password are inconsistent.",safe=False)
    elif len(User.objects.filter(username=uname)) > 0:
        return JsonResponse("The email is exists.",safe=False)
    else:
        u = User(username=uname,password=pass1)
        u.save()
        return JsonResponse("0",safe=False)

def login(request):
    uname = request.POST["username"]
    passd = request.POST["password"]
    if len(User.objects.filter(username=uname,password=passd)) > 0:
        return JsonResponse("0",safe=False)
    else:
        return JsonResponse("Wrong email address or password.",safe=False)
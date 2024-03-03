from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse


def hello(request):
    return HttpResponse(f'Hello,{request.user}!')


def sign(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            return HttpResponse(f'Hello,{request.POST.get("email")}!')
        else:
            raise Exception()
    return render(request, template_name="link.html")





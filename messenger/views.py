from django.shortcuts import render, HttpResponse


def hello(request):
    return HttpResponse(f'Hello,{request.user}!')


def sign(request):
    return render(request, template_name="link.html")




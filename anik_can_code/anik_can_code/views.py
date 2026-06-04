from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("i will be the best programmer in the world")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("i am anik and i am a software developer")

def contact(request):
    return HttpResponse("you can contact me nowhere")
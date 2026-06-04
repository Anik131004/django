from django.shortcuts import render

# Create your views here.
def ironman(request):
    return render(request, 'ironman/one.html')
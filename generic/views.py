from django.shortcuts import render

# Create your views here.


def muni(request):
    return render(request,'muni.html')

def gaanu(request):
    return render(request,'gaanu.html')

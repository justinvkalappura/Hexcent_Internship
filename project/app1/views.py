from django.shortcuts import render
from .models import class1

# Create your views here.
def front(request):
    return render(request,'front.html')

def home(request):
    var=class1.objects.all()
    return render(request,'home.html',{'key1':var})
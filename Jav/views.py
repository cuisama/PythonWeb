from django.shortcuts import render

# Create your views here.
from Jav import models


def main(request):
    data = models.Video.objects.all()
    return render(request,"main.html",{"videos":data})
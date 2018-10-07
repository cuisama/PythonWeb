from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from Jav import models


def main(request):
    data = models.Video.objects.all()[0:100]
    return render(request,"main.html",{"videos":data})

def search(request):
    para = {
        "number":request.POST.get("number",""),
        "title":request.POST.get("title",""),
        "cast":request.POST.get("cast",""),
        "maker":request.POST.get("maker","")
    }

    # data = models.Video.objects.filter(Q(number_icontains=para['number']) | Q(title_icontains=para['title']) | Q(cast_icontains=para['cast']) | Q(maker_icontains=para['maker']))
    data = models.Video.objects.filter(number__icontains=para['number']).filter(title__icontains=para['title']).filter(cast__icontains=para['cast']).filter(maker__icontains=para['maker'])[0:100]
    return render(request,"main.html",{"videos":data,"para":para})
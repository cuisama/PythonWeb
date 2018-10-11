from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from Jav import models

PAGE_PRE_NUM = 2

def main(request):
    data = models.Video.objects.all().order_by('-date')
    data = Paginator(data,PAGE_PRE_NUM).page(1)
    return render(request,"main.html",{"videos":data,"para":{"current":2}})

def search(request):
    para = {
        "number":request.POST.get("number",""),
        "title":request.POST.get("title",""),
        "cast":request.POST.get("cast",""),
        "genres":request.POST.get("genres",""),
        "director":request.POST.get("director",""),
        "maker":request.POST.get("maker",""),
        "current":request.POST.get("current",1)
    }
    p = []
    for col in ["number","title","cast","genres","director","maker"]:
        tmp = None
        if para[col]:
            tmp = para[col].split(' ')
        if tmp is not None:
            for t in tmp:
                if col == "number":
                    p.append(Q(number__icontains=t))
                elif col == "title":
                    p.append(Q(title__icontains=t))
                elif col == "cast":
                    p.append(Q(cast__icontains=t))
                elif col == "genres":
                    p.append(Q(genres__icontains=t))
                elif col == "director":
                    p.append(Q(director__icontains=t))
                elif col == "maker":
                    p.append(Q(maker__icontains=t))

    query = models.Video.objects
    for i in p:
        query = query.filter(i)

    data = query.order_by("-date")
    data = Paginator(data,PAGE_PRE_NUM).page(para["current"])
    para["current"] = int(para["current"]) + 1

    # data = models.Video.objects.filter(Q(number__icontains=para['number'])
    #                                    , Q(title__icontains=para['title'])
    #                                    , Q(cast__icontains=para['cast'])
    #                                    , Q(genres__icontains=para['genres'])
    #                                    , Q(director__icontains=para['director'])
    #                                    , Q(maker__icontains=para['maker'])).order_by("-date")[0:100]
    #data = models.Video.objects.filter(number__icontains=para['number']).filter(title__icontains=para['title']).filter(cast__icontains=para['cast']).filter(maker__icontains=para['maker'])[0:100]
    return render(request,"main.html",{"videos":data,"para":para})
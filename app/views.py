from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('topic created')

    return render(request,'create_topic.html')

def create_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST.get('n')
        u=request.POST.get('u')
        e=request.POST.get('e')
        toa=Topic.objects.get_or_create(topic_name=tn)[0]
        to=Webpage.objects.get_or_create(topic_name=toa,name=n,url=u,email=e)[0]
        to.save()
        return HttpResponse('webpage created')

    return render(request,'create_webpage.html')

def create_access_record(request):
    if request.method=='POST':
        n=request.POST.get('n')
        d=request.POST.get('d')
        a=request.POST.get('a')
        woa=Webpage.objects.get_or_create(name=n)[0]
        to=AccessRecord.objects.get_or_create(name=woa,date=d,author=a)[0]
        to.save()
        return HttpResponse('access_record created')

    return render(request,'create_access_record.html')
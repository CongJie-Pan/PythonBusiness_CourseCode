from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse
from bs4 import BeautifulSoup
import requests
import datetime


def home(request):
    return render(request, 'home/home.html')


def simple_crawl(request):
    url = "https://www.cnn.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.select('title')
    return render(request, 'home/home.html', locals())

def hello(request):
    name=request.GET['name']
    gender=request.GET['gender']
    c={'g':gender}
    c['who']=name
    return render(request,'home/hello.html',c)

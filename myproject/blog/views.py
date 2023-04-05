from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Index(request):
    template = loader.get_template('index.html')
    context = {
        'title':'Belajar Web Developer Menggunakan Django Framework | EdiKartono.com',
        'content_body':'Ini adalah toturial bagian pertama belajar cara membuat website menggunakan django framework bersama edikartono.com ',
    }
    return HttpResponse(template.render(context, request))

def new(request):
    template = loader.get_template('new.html')
    context = {
        'title':'Belajar Web Developer Menggunakan Django Framework | EdiKartono.com',
        'content_body':'Ini halaman new data ',
    }
    return HttpResponse(template.render(context, request))

def welcome(request):
    template = loader.get_template('home/index.html')
    context = {
        'title':'Welcome Django Framework',
        'content_body':'Hello World By Saepulfariz',
    }
    return HttpResponse(template.render(context, request))

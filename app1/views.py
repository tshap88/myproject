from django.shortcuts import render
from django.core.files import File
from django.views import generic

# Create your views here.
from app1.models import App1,Choice

def index(request):
	app1 = App1.objects.all().order_by('action')
	context = {'app1':app1}
	return render(request, 'app1/index.html', context)

def detail(request, appaction):
	app1 = App1.objects.get(action=appaction)
	context = {'app1': app1}
        return render(request, 'app1/detail.html', context)
#def end(request,):
#	f = open('/home/tania/myproject/sample.txt', 'r')
#	r = f.read()
#	context = {'r':r}
#	f.close()
#	return render(request, 'app1/end.html', context)
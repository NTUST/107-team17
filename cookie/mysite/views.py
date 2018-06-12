from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import About_us,Products,ProductDetail,News,Contact,QA,Banner
from . import models
from django.template import RequestContext
# Create your views here.

def aboutus(request):
	a = About_us.objects.all()
	return render_to_response('site/about.html',locals())

def products(request):
	products = Products.objects.all()
	return render_to_response('site/products.html',locals())

def products_detail(request):
	products = Products.objects.all()


	n = request.GET["name"]
	pd = ProductDetail.objects.filter(name=n)
	return render_to_response('site/products_detail.html',locals())

def contact(request):

	return render_to_response('site/contact.html')

def send(request):

	name = request.POST.get("name")
	email = request.POST.get("email")
	text = request.POST.get("article")
	po = models.Contact(name=name,email=email,text=text)
	po.save()
	return HttpResponseRedirect('/')

def qa(request):

	q = QA.objects.all()
	return render_to_response('site/qa.html',locals())

def index(request):
	banners =Banner.objects.all()
	return render_to_response('site/index.html',locals())

def english(request):

	return render_to_response('site/english_ver.html')

def news(request):
	banners =Banner.objects.all()
	news =News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render_to_response('site/news.html',locals())

def noproblem(request):
	return render_to_response('site/noproblem.html')

def question(request):
	return render_to_response('site/question.html')

def tictactoe(request):
	return render_to_response('site/tictactoe.html')

def newsgraduate(request):
	return render_to_response('site/newsgraduate.html')





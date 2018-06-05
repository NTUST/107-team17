from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import About_us,Products,ProductDetail,News,Contact,QA
from . import models
# Create your views here.

def aboutus(request):
	a = About_us.objects.all()
	return render_to_response('site/about.html',locals())

def products(request):
	products = Products.objects.all()
	return render_to_response('site/products.html',locals())

def products_detail(request):

	n = request.GET["name"]
	pd = ProductDetail.objects.filter(name=n)
	return render_to_response('site/products_detail.html',locals())

def contact(request):

	return render_to_response('site/contact.html')

def send(request):

	name = request.GET["name"]
	email = request.GET["email"]
	text = request.GET["article"]
	po = models.Contact(name=name,email=email,text=text)
	po.save()
	return HttpResponseRedirect('/')

def qa(request):

	q = QA.objects.all()
	return render_to_response('site/question.html',locals())

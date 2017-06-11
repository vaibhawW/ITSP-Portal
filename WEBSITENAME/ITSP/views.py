from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse #as redirect

def index(request):
	return HttpResponse("hello world");
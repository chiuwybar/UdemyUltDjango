from django.http import HttpResponse
from django.shortcuts import render

def home (request):
	return render(request, 'home.html')

def translate(request):
	
	return HttpResponse("You're on the translate page! " + request.GET['originaltext'])
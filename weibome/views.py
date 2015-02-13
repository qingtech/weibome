#from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	#return HttpResponse("Hello, welcome to WeiboMe!")
	return render_to_response('index.html',)

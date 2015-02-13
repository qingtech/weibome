#encoding=utf-8
from django.shortcuts import render_to_response

def home(request):
	from weime.models import WeiboApp
	app1 = WeiboApp.objects.get(app_name = '微me')
	#print '%s, key=%s, secret: %s, callback_url:%s'%(app1.app_name, app1.app_key, app1.app_secret, app1.callback_url)
	return render_to_response('weime/index.html',)

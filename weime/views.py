#encoding=utf-8
from django.shortcuts import render_to_response, render

def home(request):
	from weime.models import WeiboApp
	app1 = WeiboApp.objects.get(app_name = '微me')

	from sinaweibopy.weibo import APIClient

	APP_KEY = app1.app_key
	APP_SECRET = app1.app_secret
	CALLBACK_URL = app1.callback_url
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	print url
	#print '%s, key=%s, secret: %s, callback_url:%s'%(app1.app_name, app1.app_key, app1.app_secret, app1.callback_url)

	#return render_to_response('weime/index.html',)
	return render(request, 'weime/index.html', {'auth_url':url})

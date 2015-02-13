#encoding=utf-8
#from django.http import HttpResponse
from django.shortcuts import render_to_response, render

def home(request):
	#return HttpResponse("Hello, welcome to weiboMe!")
	#return render_to_response('index.html',)
	#user is login
	from weime.models import WbUser
	from sinaweibopy.weibo import APIClient
	user = None
	client = None
	if request.session.has_key('uid'):
		uid = request.session['uid']
		user = WbUser.objects.get(id=uid)
		from weime.models import WeiboAuth
		auth = WeiboAuth.objects.filter(user__id = uid)[0]
		app1 = auth.weibo_app
		APP_KEY = app1.app_key
		APP_SECRET = app1.app_secret
		CALLBACK_URL = app1.callback_url
		client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
		client.set_access_token(auth.access_token, auth.expires_in)
	
	#user is not login
	if not user and request.GET.has_key('code'):

		code = request.GET['code']
	
		from weime.models import WeiboApp
		app1 = WeiboApp.objects.get(app_name = '微me')

		APP_KEY = app1.app_key
		APP_SECRET = app1.app_secret
		CALLBACK_URL = app1.callback_url
		client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
		r = client.request_access_token(code)
		access_token = r.access_token # 新浪返回的token，类似abc123xyz456
		expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
		client.set_access_token(access_token, expires_in)
		user = WbUser(id=r.uid,	idstr=r.uid)
		user.save()
		from weime.models import WeiboAuth
		auth = WeiboAuth.objects.filter(weibo_app__id=app1.id, user__id=r.uid)
		if auth:
			auth = auth[0]
			auth.access_token = access_token
			auth.expires_in = expires_in
		else:
			auth = WeiboAuth(weibo_app = app1, user = user, access_token = access_token, expires_in = expires_in)
		auth.save()
		request.session['uid'] = r.uid
		print 'access token: %s'%access_token
		print 'expires_in: %s'%expires_in

	import time
	count = 0
	max_id = int('7FFFFFFFFFFFFFF0', 16)
	max_id = int('1FFFFFFFFFFFFFF0', 16)
	max_id = int('FFFFFFFFFFFFF0', 16)
	max_id = int('FFFFFFFFFFFF0', 16)
	max_id = int('FFFFFFFFFFF0', 16)
	max_id = 0
	# TODO: get max_id from DB
	print 'max_id: %s'%max_id
	while True:
		#time.sleep(30)
		if not client:
			return render(request, 'index.html', )
		r = client.statuses.user_timeline.get(max_id = max_id, count = 200)
		#r = client.statuses.user_timeline.get(count = 2)
		for st in r.statuses:
			count = count + 1
			#print '%d:%s'%(count,st.id)
			#print st
			#print '++++++++++++++++++++++++++++++++++++++++++++++++++'
			if max_id == 0 or st.id - 1 < max_id:
				max_id = st.id - 1
		#time.sleep(30)
		break
	return render(request, 'index.html', {'statuse_list':r.statuses} )

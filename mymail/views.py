from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.template.context_processors import csrf
from mymail.models import user
from django.contrib import auth
from django.contrib.auth.models import User



def home(request):
	return render(request, 'create_account.html')

def registered(request):
	f_name = request.GET.get('f_name')
	l_name =  request.GET.get('l_name')
	mail = request.GET.get('mail')
	userid = request.GET.get('user_name')
	gender = request.GET.get('optionsRadios')
	password = request.GET.get('password')

	if not user.objects.filter(user_id = userid):
		obj = user(first_name = f_name,last_name=l_name,email=mail,user_id=userid,gender=gender,password=password)
		obj.save()
		return render_to_response('registration.html', {},context_instance=RequestContext(request))
	else:
		html = '<html><body><h1>Error UserName already exists</h1><br>click <a href="/../mymail">here</a> to Register</body></html>'
		return HttpResponse(html)

def user_validate(request):
	userid = request.GET.get('userid')
	password = request.GET.get('pwd')
	try:
		us = user.objects.get(user_id=userid)
	except user.DoesNotExist:
		return HttpResponseRedirect('/../mymail/')
	print us.password
	if us is not None:
		if us.password == password:
			return HttpResponseRedirect('/mymail/success/')
		else:
			return HttpResponseRedirect('/../mymail/')
	else:
		# return render_to_response('create_account.html', {},context_instance=RequestContext(request))
		return HttpResponseRedirect('/../mymail/')

def success_login(request):
	return render(request,'success.html')

# Create your views here.

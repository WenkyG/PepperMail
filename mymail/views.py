from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.template.context_processors import csrf
from mymail.models import user, mailing
from django.contrib import auth
from django.contrib.auth.models import User



def home(request):
	return render(request, 'create_account.html')

def registered(request):
	f_name = request.POST.get('f_name')
	l_name =  request.POST.get('l_name')
	mail = request.POST.get('mail')
	userid = request.POST.get('user_name')
	gender = request.POST.get('optionsRadios')
	password = request.POST.get('password')

	if not user.objects.filter(user_id = userid):
		obj = user(first_name = f_name,last_name=l_name,email=mail,user_id=userid,gender=gender,password=password)
		obj.save()
		return render_to_response('registration.html', {},context_instance=RequestContext(request))
	else:
		html = '<html><body><h1>Error UserName already exists</h1><br>click <a href="/../mymail">here</a> to Register</body></html>'
		return HttpResponse(html)

def user_validate(request):
	userid = request.POST.get('userid')
	password = request.POST.get('pwd')
	try:
		us = user.objects.get(user_id=userid)
	except user.DoesNotExist:
		return HttpResponseRedirect('/../mymail/')
	# print us.password
	if us is not None:
		if us.password == password:
			request.session["user_id"] = userid 
			return render_to_response('success.html',{'user_name':request.session["user_id"]})
		else:
			return HttpResponseRedirect('/../mymail/')
	else:
		# return render_to_response('create_account.html', {},context_instance=RequestContext(request))
		return HttpResponseRedirect('/../mymail/')

def success_login(request):
	return render(request,'success.html')
def new_mail(request):
		return render(request,'new_mail.html')
def sending(request,p):
	sent_from = request.session["user_id"]
	sent_to = request.POST.get('to')
	subj = request.POST.get('subject')
	content = request.POST.get('content')
	try:
		use = user.objects.get(user_id=sent_to)
		# print use, sent_to, sent_from, subj, content
	except user.DoesNotExist:
		return HttpResponseRedirect('../new_mail')
	if use is not None:
		m = mailing(sender=user.objects.get(user_id=sent_from),receiver=user.objects.get(user_id=sent_to),subject=subj,messege=content)
		# print m
		m.save()
		# str1 = "/mymail/success/" + p
		return HttpResponseRedirect('/mymail/success/'+p+'/')
def inbox_mail(request):
	i = user.objects.get(user_id=request.session["user_id"])
	# print i.id
	u = mailing.objects.filter(receiver_id=i.id)
	return render_to_response('inbox.html',{'u':u})
def sent_mail(request):
	i = user.objects.get(user_id=request.session["user_id"])
	print i.id
	u = mailing.objects.filter(sender_id=i.id)
	return render_to_response('sent.html',{'u':u})

def trash_mail(request):
	return render(request,'trash.html')
# Create your views here.

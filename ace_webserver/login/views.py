from django.shortcuts import render
from .models import *
import jwt
from django.core.mail import EmailMessage
import random 
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth import authenticate, login,logout

class UploadFileForm(forms.Form):
    file = forms.FileField()

@login_required
@csrf_exempt
def import_login_table(request):
	if request.user.is_authenticated():
		user=str(request.user)
		try:
			login_data_row=login_data.objects.get(login_id=str(user))
			if (login_data_row.group_id==1):
			    if request.method == "POST":
			        form = UploadFileForm(request.POST,request.FILES)
			        if form.is_valid():
			            request.FILES['file'].save_to_database(
			                model=login_data,
			                mapdict=['login_id','group_id'])
			            return HttpResponse("OK")
			        else:
			            return HttpResponseBadRequest()
			    else:
			        form = UploadFileForm()
			        return render(request,'upload.html',{'form': form})
		        return render(request,'upload.html',{'form': form})
		except:
			return HttpResponse("Page not found")
	else:
		return HttpResponse("page not found")


def email_verification(request):
	try:
		email=str(request.GET.get('email'))
		otp=str(request.GET.get('otp'))
		# email=jwt.decode(email,'secret',algorithms=['HS256'])
		# otp=jwt.decode(otp,'secret',algorithms=['HS256'])
		print email
		print otp
		try:
			login_data_row=login_data.objects.get(email=email)
			if login_data_row.otp==otp:
				setattr(login_data_row,'email_flag',True)
				login_data_row.save()
				return HttpResponse("email verification done")
			else:
				return HttpResponse("email verification  not done")
		except:
			return HttpResponse("email_id and otp not get")
	except:
		return HttpResponse("Failed")

# http://127.0.0.1:8000/verify_email?email=arpitj938@gmail.com&otp=123456

def login_view(request):
	if request.user.is_authenticated():
		return render(request,'main.html',{'logout':'logout'})
	else:
		if request.method=='POST':
			login_id=str(request.POST.get('login_id'))
			password=str(request.POST.get('password'))
			password=jwt.decode(password,'secret',algorithms=['HS256'])
			try:
				login_data_row=login_data.objects.get(login_id=login_id)
				print login_id
				if login_data_row.password==password:
					if login_data_row.email_flag==1:
						user = authenticate(username=login_id, password=password)
						if user is not None:
							login(request, user)
							print 'login done'
							return HttpResponseRedirect("/welcome/")
						else:
							return render(request,'main.html',{'login_status':'wrong login_id or password'})
					else:
						return render(request,'main.html',{'login_status':'complete your email verification'})
				else:
					return render(request,'main.html',{'login_status':'wrong login_id or password'})
			except:
				return render(request,'main.html',{'login_status':'wrong login_id or password'})
		else:
			return render(request,'main.html')















# Create your views here.

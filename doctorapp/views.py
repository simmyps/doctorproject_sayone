from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctorapp.models import TbAddpatient
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import check_password 
import json

def home(request):
	return render(request,"doctorlogin.html")

def signup(request):
	return render(request,"signup.html")

def ajaxsignup(request):
	dict1={}
	try:

		fname=request.POST["txtfname"]		
		lname=request.POST["txtlname"]
		uname=request.POST["txtuname"]
		pwd=request.POST["txtpwd"]
		cpwd=request.POST["txtcpwd"]
		if(pwd==cpwd):
			x=User.objects.create_user(is_superuser="0",username=uname,password=pwd,first_name=fname,last_name=lname)
			x.save()
			dict1["val2"]=0
			dict1["status"]=True
		else:
			dict1["val1"]=0
			dict1["status"]=True	
	except Exception as e:
		print(e)
		dict1["status"]=False	
	jsondata=json.dumps(dict1)
	return HttpResponse(jsondata,content_type="application/json")

def ajaxlogin(request):
	dict2={}
	try:
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				fname=username.first_name
				print(username)
			except Exception as e:
				print(e)
				
		uname=request.POST["txtname"]
		pwd=request.POST["txtpwd"]
		user=authenticate(request,username=uname,password=pwd)
		if user is not None:
			dict2["login"]=0
			login(request,user)		
			dict2["status"]=True
		else:
			dict2["val1"]=1
			dict2["status"]=True
	except Exception as e:
		print(e)
		dict2["val"]="Wrong password/username"
		dict2["status"]=False
	jsondata=json.dumps(dict2)
	return HttpResponse(jsondata,content_type="application/json")

def doctorhomepage(request):
	return render(request,"doctorhomepage.html")

def addpatient(request):
	return render(request,"addpatients.html")


def ajaxaddpatient(request):
	dict3={}
	try:
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				fname=username.first_name
				print(username)
			except Exception as e:
				print(e)		
		name=request.POST["txtpname"]
		address=request.POST["txtapad"]
		mcondition=request.POST["txtacondition"]
		pmedicine=request.POST["txtamedicine"]
		tbpatient=TbAddpatient(pname=name,paddress=address,pcondition=mcondition,pmedicine=pmedicine,dname=fname)
		tbpatient.save()
		dict3["status"]=True
	except Exception as e:
		print(e)
		dict3["status"]=False
	jsondata=json.dumps(dict3)
	return HttpResponse(jsondata,content_type="application/json")

def viewpatient(request):
	return render(request,"viewpatient.html")


def ajaxviewpatient(request):
	lis=[]
	dict4={}
	try:
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				fname=username.first_name
				print(username)
			except Exception as e:
				print(e)
			result=TbAddpatient.objects.filter(dname=fname)
			for rs in result:
				lis.append(rs.pname)
			dict4["val1"]=lis
			dict4["status"]=True
		else:
			print("User not validated")
	except Exception as e:
		print(e)
		dict4["status"]=False
	jsondata=json.dumps(dict4)
	return HttpResponse(jsondata,content_type="application/json")


def searchpatient(request):
	return render(request,"searchpatient.html")


def ajaxview(request):
	lis=[]
	dict5={}
	try:
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				fname=username.first_name
				print(username)
			except Exception as e:
				print(e)
			result=TbAddpatient.objects.filter(dname=fname)
			for rs in result:
				lis.append(rs.pname)
			dict5["val1"]=lis
			dict5["status"]=True
		else:
			print("User not validated")
	except Exception as e:
		print(e)
		dict5["status"]=False
	jsondata=json.dumps(dict5)
	return HttpResponse(jsondata,content_type="application/json")
	


def ajaxseachpatient(request):
	dict6={}
	try:
		sname=request.POST["txtsname"]
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				fname=username.first_name
				print(username.first_name)
			except Exception as e:
				print(e)
			result=TbAddpatient.objects.filter(pname=sname,dname=fname)
			dict6["pname"]=result[0].pname
			dict6["address"]=result[0].paddress
			dict6["condition"]=result[0].pcondition
			dict6["medicine"]=result[0].pmedicine
			dict6["status"]=True
	except Exception as e:
		print(e)
		dict6["status"]=False
	jsondata=json.dumps(dict6)
	return HttpResponse(jsondata,content_type="application/json")


def addmulcondition(request):
	return render(request,"addmuticondition.html")


def ajaxaddserach(request):
	dict7={}
	try:
		name=request.POST["txtpname"]
		username=None
		if request.user.is_authenticated:
			try:
				username=request.user
				fname=username.first_name
				print(username.first_name)
			except Exception as e:
				print(e)
			result=TbAddpatient.objects.filter(pname=name,dname=fname)
			dict7["val1"]=result[0].pcondition
			dict7["val2"]=result[0].pmedicine
			dict7["status"]=True
	except Exception as e:
		print(e)
		dict7["status"]=False
	jsondata=json.dumps(dict7)
	return HttpResponse(jsondata,content_type="application/json")
				
def ajaxupdate(request):
	dict8={}
	try:
		name=request.POST["txtpname"]
		condition=request.POST["txtacon"]
		medicine=request.POST["txtamedi"]
		result=TbAddpatient.objects.get(pname=name)
		result.pcondition=condition
		result.pmedicine=medicine
		result.save()
		dict8["status"]=True
	except Exception as e:
		print(e)
		dict8["status"]=False
	jsondata=json.dumps(dict8)
	return HttpResponse(jsondata,content_type="application/json")	


def doctorlogout(request):
	try:
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				print(username)
			except Exception as e:
				print(e)

		logout(request)
		return redirect("doctor first page")
	except Exception as e:
		print(e)

def ajaxpaview(request):
	lis=[]
	dict9={}
	try:
		username = None
		if request.user.is_authenticated:
			try:
				username = request.user
				fname=username.first_name
				print(username)
			except Exception as e:
				print(e)
			result=TbAddpatient.objects.filter(dname=fname)
			for rs in result:
				lis.append(rs.pname)
			dict9["val1"]=lis
			dict9["status"]=True
		else:
			print("User not validated")
	except Exception as e:
		print(e)
		dict9["status"]=False
	jsondata=json.dumps(dict9)
	return HttpResponse(jsondata,content_type="application/json")

		





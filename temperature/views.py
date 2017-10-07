from __future__ import unicode_literals
from .models import Temperature 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(received_data.tem_value)
	hum_data=str(received_data.hum_value)
	moisture=str(received_data.moisture)
	ult_data=str(received_data.ult_value)
	water_data=str(received_data.water_value)

	context={'tem':temp_data,'hum':hum_data,'moist':moisture,'ult':ult_data,'wat':water_data}
	return render(request,'temperature/index.html',context)
def getdata(request):
	if request.method=='GET' :
		tem_value=request.GET['temperature']
		hum_value=request.GET['humidity']
		moisture=request.GET['soilmoisture']
		ult_value=request.GET['ultrasonic']
		water_value=request.GET['water']
		t_obj=Temperature()
		t_obj.tem_value=tem_value
		t_obj.hum_value=hum_value
		t_obj.moisture=moisture
		t_obj.ult_value=ult_value
		t_obj.water_value=water_value
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")
def temp(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(received_data.tem_value)
	
	context={'tem':temp_data}
	return render(request,'temperature/temp.html',context)
def hum(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	hum_data=str(received_data.hum_value)
	
	context={'hum':hum_data}
	return render(request,'temperature/hum.html',context)
def moist(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	
	moisture=str(received_data.moisture)
	context={'moist':moisture}
	return render(request,'temperature/moist.html',context)
def ult(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	
	ult_data=str(received_data.ult_value)
	context={'ult':ult_data}
	return render(request,'temperature/ult.html',context)
def wat(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	
	water_data=str(received_data.water_value)
	context={'wat':water_data}
	return render(request,'temperature/wat.html',context)







from django.shortcuts import render

from .models import job
def home(request):
	job_s=job.objects
	return render(request,'jobs/home.html',{'jobs':job_s})
# Create your views here.

from django.shortcuts import render, get_object_or_404

from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def job_details(request, job_id):
    detail_job = get_object_or_404(Job, pk=job_id)
    if job_id == 2:
        return render(request, 'jobs/books_detail.html')
    elif job_id == 1:
        return render(request, 'jobs/tech_exp_detail.html')
    else:
        return render(request, 'jobs/home.html')
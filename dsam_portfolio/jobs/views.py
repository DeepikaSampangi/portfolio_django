from django.shortcuts import render, get_object_or_404

from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def job_details(request, job_id):
    detail_job = get_object_or_404(Job, pk=job_id)
    if detail_job.job_name == 'Blogger':
        return render(request, 'blog/allblogs.html',{'blogs':None})
    else:
        return render(request, 'jobs/job_detail.html', {'detail_jobs':detail_job})
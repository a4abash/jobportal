from django.shortcuts import render,redirect
from jobseeker.forms import JobSeekerForm
from jobseeker.forms import SkillForm
from .models import JobSeeker
from jobseeker.forms import ExperienceForm
# Create your views here.
def create(request):
    if request.method=='GET':
        context = {
            'form': JobSeekerForm()
        }
        return render(request,'jobseeker_create.html',context)

    else:
        form = JobSeekerForm(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'jobseeker_create.html', {'form':form})

def skill_store(request):
    if request.method=='GET':
        return redirect('dashboard')
    else:
        form = SkillForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            a = JobSeeker.objects.get(user_id = request.user.id)
            data.jobseeker_id = a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')

def exp_store(request):
    if request.method=='GET':
        return ('dashboard')
    else:
        form = ExperienceForm(request.POST)
        if form.is_valid:
            data = form.save(commit=False)
            a = JobSeeker.objects.get(user_id = request.user.id)
            data.jobseeker_id=a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')



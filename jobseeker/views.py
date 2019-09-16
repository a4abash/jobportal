from django.shortcuts import render,redirect
from jobseeker.forms import JobSeekerForm
from jobseeker.forms import SkillForm,JobSeekerUpdateForm,JobSeekerProjectForm
from .models import JobSeeker,Skill,Project
from jobseeker.forms import ExperienceForm
from django.contrib.auth.models import User
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

def remove(request,x):
    s = Skill.objects.get(id=x)
    s.delete()
    return redirect('dashboard')

def name_update(request):
    if request.method=='GET':
        return redirect('dashboard')
    else:
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        a = User.objects.get(id=request.user.id)
        a.first_name=f
        a.last_name=l
        a.save()
        return redirect('dashboard')

def details_update(request):
    if request.method=='GET':
        return redirect('dashboard')
    else:
        b = JobSeeker.objects.get(user_id=request.user.id)
        form = JobSeekerUpdateForm(request.POST or None,instance=b)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

def edit_project(request,x):
    project = Project.objects.get(id=x)
    form = JobSeekerProjectForm(request.POST or None,instance=project)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form':form,
    }
    return render(request,'edit_project.html',context)

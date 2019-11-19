from django.shortcuts import render, redirect
from jobseeker.forms import JobSeekerForm,ProfileImageForm
from jobseeker.forms import SkillForm, JobSeekerUpdateForm, JobSeekerProjectForm, JobseekerDescriptionUpdateForm
from .models import JobSeeker, Skill, Project, Experience
from jobseeker.forms import ExperienceForm
from django.contrib.auth.models import User
from easyjob.views import checkCompanyOrJobseeker
from django.contrib.auth.decorators import login_required


# Create your views here.
# Calls the jobseeker creation form
@login_required(login_url='signin')
def create(request):
    r = checkCompanyOrJobseeker(request.user.id)
    if r == 1:
        return redirect('dashboard')
    elif r == 2:
        return redirect('company_dashboard')
    else:
        if request.method == 'GET':
            context = {
                'form': JobSeekerForm()
            }
            return render(request, 'jobseeker_create.html', context)

        else:
            form = JobSeekerForm(request.POST, request.FILES or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = request.user.id
                data.save()
                return redirect('dashboard')
            else:
                return render(request, 'jobseeker_create.html', {'form': form})


# Update  User Profile image
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'dashboard')
    else:
        j = JobSeeker.objects.get(user_id=request.user.id)
        f = ProfileImageForm(request.POST, request.FILES, instance=j)
        if f.is_valid():
            f.save()
            return redirect('dashboard')
        else:
            return render(request, 'dashboard.html')


# Jobseeker first name and last name section
def name_update(request):
    if request.method == 'GET':
        return redirect('dashboard')
    else:
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        a = User.objects.get(id=request.user.id)
        a.first_name = f
        a.last_name = l
        a.save()
        return redirect('dashboard')


# Jobseeker details update section
def details_update(request):
    if request.method == 'GET':
        return redirect('dashboard')
    else:
        b = JobSeeker.objects.get(user_id=request.user.id)
        form = JobSeekerUpdateForm(request.POST or None, instance=b)
        if form.is_valid():
            form.save()
            return redirect('dashboard')


# Jobseeker skills update section
def skill_store(request):
    if request.method == 'GET':
        return redirect('dashboard')
    else:
        form = SkillForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            a = JobSeeker.objects.get(user_id=request.user.id)
            data.jobseeker_id = a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')


# jobseeker skill remove section
def remove(request, x):
    s = Skill.objects.get(id=x)
    s.delete()
    return redirect('dashboard')


# Jobseeker description edit section
def edit_description(request):
    if request.method == 'GET':
        return redirect('dashboard')
    else:
        b = JobSeeker.objects.get(user_id=request.user.id)
        form = JobseekerDescriptionUpdateForm(request.POST or None, instance=b)
        if form.is_valid():
            form.save()
            return redirect('dashboard')


# jobseeker project edit section
def edit_project(request, x):
    j = JobSeeker.objects.get(user_id=request.user.id)
    project = Project.objects.get(id=x)
    if j.id == project.jobseeker_id:
        form = JobSeekerProjectForm(request.POST or None,instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        context = {
            'form': form,
        }
        return render(request, 'edit_project.html', context)


# jobseeker project remove section
def rmvprj(request, x):
    s = Project.objects.get(id=x)
    s.delete()
    return redirect('dashboard')


# adds experience to experience table of jobseeker
def experience_add(request):
    if request.method == 'GET':
        return ('dashboard')
    else:
        form = ExperienceForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            a = JobSeeker.objects.get(user_id=request.user.id)
            data.jobseeker_id = a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')


# deletes the entry from experience table
def exp_dlt(request, x):
    d = Experience.objects.get(id=x)
    d.delete()
    return redirect('dashboard')

'''
# modifies the experience table
def exp_edit(request, x):
    experience = Experience.objects.get(id=x)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid:
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'edit_experience.html', context)
'''

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from company.models import Job
from .forms import SignUpForm
from django.contrib.auth.models import User
from jobseeker.models import JobSeeker, Project, Skill, Experience
from jobseeker.forms import JobSeekerProjectForm, SkillForm, ExperienceForm, JobSeekerUpdateForm, JobseekerDescriptionUpdateForm, ProfileImageForm
from company .forms import CompanyUpdateDescription, Company, CompanyDetailUpdateForm
from general.models import Slider, Testimonial


# Home page
def home(request):
    context = {
        'slider': Slider.objects.all()[:3],
        'js': JobSeeker.objects.all()[:5],
        'testimonial': Testimonial.objects.all()[:4]
    }
    return render(request, 'home.html', context)


# Signup page
def signup(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }
        return render(request, 'signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is successfully created")
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})


# Signin page
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            id = request.user.id
            x = checkCompanyOrJobseeker(id)
            if x == 1:
                return redirect('dashboard')
            elif x == 2:
                return redirect('company_dashboard')
            else:
                return redirect('who')
        else:
            messages.error(request, "Your Password does not match")
            return redirect('signin')


# check if user is company or jobseeker
def checkCompanyOrJobseeker(id):
    try:
        a = JobSeeker.objects.get(user_id=id)
        return 1
    except:
        try:
            c = Company.objects.get(user_id=id)
            return 2
        except:
            return 3


# to check the who actually is the user
@login_required(login_url='signin')
def who(request):
    r = checkCompanyOrJobseeker(request.user.id)
    if r == 1:
        return redirect('dashboard')
    elif r == 2:
        return redirect('company_dashboard')
    else:
        return render(request, 'who.html')


@login_required(login_url='signin')
# Jobseeker project update section
def dashboard(request):
    if request.method == 'GET':
        a = User.objects.get(id=request.user.id)
        b = JobSeeker.objects.get(user_id=request.user.id)
        project = Project.objects.filter(jobseeker_id=b.id)[::-1]
        skill = Skill.objects.filter(jobseeker_id=b.id)
        experience = Experience.objects.filter(jobseeker_id=b.id)
        context = {
            'user': a,
            'jobseeker': b,
            'pform': ProfileImageForm(instance=b),  # To update jobseeker profile Picture
            'jform': JobSeekerUpdateForm(instance=b),  # To update jobseeker details
            'sform': SkillForm(),  # Sending skill form to jobseeker dashboard
            'skill': skill,  # skill is used to print the values form skill table
            'dform': JobseekerDescriptionUpdateForm(instance=b),  # To update jobseeker description
            'jobseeker_project_form': JobSeekerProjectForm(),  # Sending Jobseeker project form to update
            'project': project,  # project is used to print values from project table
            'expform': ExperienceForm(),  # sending Jobseeker Experience form
            'experience': experience,  # experience is used to print the values from experience table

        }
        return render(request, 'dashboard.html', context)
    else:
        form = JobSeekerProjectForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            a = JobSeeker.objects.get(user_id=request.user.id)
            data.jobseeker_id = a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')


# for company
def company_dashboard(request):
    if request.method == 'GET':
        x = User.objects.get(id=request.user.id)
        y = Company.objects.get(user_id=request.user.id)
        job = Job.objects.filter(company_id=y.id)[::-1][:4]
        context = {
            'user': x,
            'company': y,
            'cform': CompanyUpdateDescription(instance=y),  # form for updating description section
            'job': job,  # sends entire list of available jobs to company_dashboard
            'companyupdateform': CompanyDetailUpdateForm(instance=y),  # form for updating about section of company
        }
        return render(request, 'company_dashboard.html', context)
    else:
        form = CompanyUpdateDescription(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            x = Company.objects.get(user_id=request.user.id)
            data.save()
            data.company_id = x.id
            return redirect('company_dashboard')
        else:
            return redirect('company_dashboard')


# for signout
def signout(request):
    logout(request)
    return redirect('signin')

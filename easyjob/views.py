from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobseeker.models import JobSeeker
from company.models import Company
from .forms import SignUpForm
from django.contrib.auth.models import User
from jobseeker.models import JobSeeker,Project
from jobseeker.forms import JobSeekerProjectForm
def index(request):
    return render(request,'index.html')

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
            messages.success(request,"Your account is successfully created")
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form':form})


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
            if x==1:
                return redirect('dashboard')
            elif x==2:
                return redirect('company_dashboard')
            else:
                return redirect('who')
        else:
            messages.error(request, "Your Password does not match")
            return redirect('signin')

@login_required(login_url='signin')
def dashboard(request):
    if request.method=='GET':
        a = User.objects.get(id=request.user.id)
        b = JobSeeker.objects.get(user_id=request.user.id)
        project = Project.objects.filter(jobseeker_id=b.id)[::-1]
        context = {
            'user' : a,
            'jobseeker' : b,
            'jobseeker_project_form':JobSeekerProjectForm(),
            'project':project,
        }
        return render(request, 'dashboard.html',context)
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

def signout(request):
    logout(request)
    return redirect('signin')

def company_dashboard(request):
    x = User.objects.get(id=request.user.id)
    y = Company.objects.get(user_id=request.user.id)
    context = {
        'user': x,
        'company' : y
    }
    return render(request,'company_dashboard.html',context)

def who(request):
    return render(request,'who.html')

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

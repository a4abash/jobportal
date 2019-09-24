from django.shortcuts import render, redirect
from .forms import CompanyForm, JobForm, CompanyUpdateDescription, CompanyDetailUpdateForm
from .models import Company, Job
from django.contrib.auth.models import User


# Create your views here.
# Calls the company creation form
def create(request):
    if request.method == 'GET':
        context = {
            'form': CompanyForm()
        }
        return render(request, 'company_create.html', context)

    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('company_dashboard')
        else:
            return render(request, 'company_create.html', {'form': form})


# ADD/Post vacancy
def vacancy_create(request):
    if request.method == 'GET':
        context = {
            'form': JobForm(),
        }
        return render(request, 'add_vacancy.html', context)
    else:
        form = JobForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            c = Company.objects.get(user_id=request.user.id)
            data.company_id = c.id
            data.save()
            return redirect('company_dashboard')
        else:
            return render(request, 'add_vacancy.html', {'form': form})


# Updates the name of company
def name_update(request):
    if request.method == 'GET':
        return redirect('company_dashboard')
    else:
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        a = User.objects.get(id=request.user.id)
        a.first_name = f
        a.last_name = l
        a.save()
        return redirect('company_dashboard')


# Updates the details of company
def update_companyDetails(request):
    if request.method == 'GET':
        return redirect('company_dashboard')
    else:
        b = Company.objects.get(user_id=request.user.id)
        form = CompanyDetailUpdateForm(request.POST or None, instance=b)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard')


# List all the added vacancies
def vacancy_view(request):
    c = Company.objects.get(user_id=request.user.id)
    context = {
        'job': Job.objects.filter(company_id=c.id)
    }
    return render(request, 'view_vacancy.html', context)


# Provide the detail of particular task
def vacancy_details(request, x):
    j = Job.objects.get(id=x)
    context = {
        'job': j
    }
    return render(request, 'vacancy_details.html', context)


# Updates the description of company
def edit_cdescription(request):
    if request.method == 'GET':
        return redirect('company_dashboard')
    else:
        b = Company.objects.get(user_id=request.user.id)
        form = CompanyUpdateDescription(request.POST or None, instance=b)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard')



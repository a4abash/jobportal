from django.shortcuts import render,redirect
from .forms import CompanyForm
# Create your views here.
def create(request):
    if request.method=='GET':
        context = {
            'form': CompanyForm()
        }
        return render(request,'company_create.html',context)

    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('company_dashboard')
        else:
            return render(request, 'company_create.html', {'form':form})
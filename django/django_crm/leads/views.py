from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LeadForm, LeadModelForm
# Create your views here.

from .models import Lead, Agent


def landing_page(request):
    return render(request, 'landing.html')

def lead_list(request):
    leads = Lead.objects.all()

    context={
        'leads': leads,
    }
    # return HttpResponse("HEllo world")
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context={
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    form=LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context={
        "form": form
    }
    return render(request,'leads/lead_create.html', context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form=LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context={
        "form": form,
        "lead": lead
        
    }
    return render(request, 'leads/lead_update.html', context)
        
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')

# For understanding
# def lead_create(request):
#     form=LeadForm()
#     if request.method == 'POST':
#         # print("Received a post request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             # print("This form is valid")
#             # print(form.cleaned_data)

#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             agent=Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             # print("Lead has been created.")
#             return redirect('/leads')
#     context={
#         "form": form
#     }
#     return render(request,'leads/lead_create.html', context)

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form=LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
            
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
            
#             lead.save()
#             return redirect('/leads')
#     context={
#         "form": form,
#         "lead": lead
        
#     }
#     return render(request, 'leads/lead_update.html', context)
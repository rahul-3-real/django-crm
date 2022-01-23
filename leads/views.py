from django.shortcuts import redirect, render
from .models import Lead
from .forms import LeadModelForm

# Create your views here.


def lead_list(request):
    leads = Lead.objects.all()
    template_name = 'leads/list.html'
    context = {
        'leads': leads
    }
    return render(request, template_name, context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    template_name = 'leads/detail.html'
    context = {
        'lead': lead
    }
    return render(request, template_name, context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')

    template_name = 'leads/create.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')

    template_name = 'leads/update.html'
    context = {
        'lead': lead,
        'form': form
    }
    return render(request, template_name, context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:lead_list')

from django.urls import reverse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead
from .forms import LeadModelForm

# Create your views here.


class LeadListView(ListView):
    queryset = Lead.objects.all()
    template_name = 'leads/list.html'
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    queryset = Lead.objects.all()
    template_name = 'leads/detail.html'
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    form_class = LeadModelForm
    template_name = 'leads/create.html'

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Visit the site to see the new Lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    template_name = 'leads/update.html'

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(DeleteView):
    queryset = Lead.objects.all()
    template_name = 'leads/delete.html'

    def get_success_url(self):
        return reverse('leads:lead_list')

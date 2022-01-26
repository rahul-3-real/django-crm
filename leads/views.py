from django.urls import reverse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm

# Create your views here.


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(
                organization=user.userprofile,
                agent__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                organization=user.agent.organization,
                agent__isnull=False
            )
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(
                organization=user.userprofile,
                agent__isnull=True)
            context.update({
                'unassigned_leads': queryset,
            })
        return context


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    form_class = LeadModelForm
    template_name = 'leads/create.html'

    def get_success_url(self):
        return reverse('lead_list')

    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Visit the site to see the new Lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    form_class = LeadModelForm
    template_name = 'leads/update.html'

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse('lead_list')


class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/delete.html'

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse('lead_list')

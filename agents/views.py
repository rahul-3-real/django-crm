import random
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from accounts.models import Agent
from .forms import CreateAgentForm
from .mixins import OrganizerAndLoginRequiredMixin

# Create your views here.


class AgentListView(OrganizerAndLoginRequiredMixin, ListView):
    template_name = 'agents/list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = 'agents/detail.html'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'agents/create.html'
    form_class = CreateAgentForm

    def get_success_url(self):
        return reverse('agent_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(f'{random.randint(0, 1000000)}')
        user.is_agent = True
        user.is_organizer = False
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message="You were added as an Agent on CRM. Please come login to start working.",
            from_email='admin@test.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/update.html'
    form_class = CreateAgentForm

    def get_success_url(self):
        return reverse('agent_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agent_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

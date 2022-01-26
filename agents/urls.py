from django.urls import path
from . import views


urlpatterns = [
    path('', views.AgentListView.as_view(), name="agent_list"),
    path('<int:pk>/', views.AgentDetailView.as_view(), name="agent_detail"),
    path('<int:pk>/update', views.AgentUpdateView.as_view(), name="agent_update"),
    path('<int:pk>/delete', views.AgentDeleteView.as_view(), name="agent_delete"),
    path('create/', views.AgentCreateView.as_view(), name="agent_create"),
]

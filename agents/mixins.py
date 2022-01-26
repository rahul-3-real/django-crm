from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin


class OrganizerAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect('lead_list')
        return super().dispatch(request, *args, **kwargs)

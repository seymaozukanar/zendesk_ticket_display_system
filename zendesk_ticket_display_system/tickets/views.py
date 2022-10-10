from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse
from .models import Ticket
from .utils import collect_user_tickets


class TicketListView(ListView):

    model = Ticket
    context_object_name = "tickets"
    template_name = "tickets/ticket_list.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return redirect(reverse("users:login"))

    def get_queryset(self):
        queryset = collect_user_tickets(self.request.user)
        return queryset.order_by("-creation_datetime")


class TicketDetailView(DetailView):

    model = Ticket
    context_object_name = "ticket"
    template_name = "tickets/ticket_detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        return context

from django.urls import path
from .views import TicketListView, TicketDetailView


urlpatterns = [
    path("<int:id>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("", TicketListView.as_view(), name="ticket-list"),
]

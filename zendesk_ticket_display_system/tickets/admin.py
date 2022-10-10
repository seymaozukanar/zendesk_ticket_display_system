from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "General Information", {"fields": ("zendesk_id", "type", "url")}
        ),
        (
            "Status", {"fields": ("status", "priority")}
        ),
        (
            "Description", {"fields": ("subject", "description")}
        ),
        (
            "Related People", {"fields": ("submitter", "assignee", "requester")}
        )
    )
    list_display = ("zendesk_id", "submitter", "assignee", "priority", "type", "status")
    list_filter = ("status", "priority", "type")
    search_fields = ("status", "priority", "type", "submitter", "assignee")


admin.site.register(Ticket, TicketAdmin)

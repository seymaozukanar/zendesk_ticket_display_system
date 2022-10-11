from dateutil import parser
from django.db.models import QuerySet
from zendesk_ticket_display_system import constants
from zenpy import Zenpy

from .models import Comment, Ticket


def collect_user_tickets(user) -> QuerySet:

    creds = {"email": constants.zendesk_email,
            "token": constants.zendesk_api_token,
            "subdomain": constants.zendesk_subdomain}
    client = Zenpy(**creds)

    user_tickets = Ticket.objects.filter(submitter=user)
    client_tickets = client.tickets()
    zendesk_id_list = list()

    for ticket in user_tickets:
        zendesk_id_list.append(ticket.zendesk_id)

    if user_tickets.count() != client_tickets.count:
        # create new Ticket objects if any
        for ticket in client_tickets:
            if ticket.id not in zendesk_id_list:
                _ticket = Ticket.objects.create(
                zendesk_id = ticket.id,
                type = ticket.type,
                url = ticket.url,
                status = ticket.status,
                priority = ticket.priority,
                subject = ticket.subject,
                description = ticket.description,
                creation_datetime = parser.parse(ticket.created_at),
                submitter = user,
                requester = ticket.requester.name,
                assignee = ticket.assignee.name,
                )
                # create Comment objects
                for comment in client.tickets.comments(ticket=ticket.id):
                    if comment.body != ticket.description:
                        Comment.objects.create(
                            author = comment.author.name,
                            body = comment.body,
                            ticket = _ticket,
                        )

    return Ticket.objects.filter(submitter=user)

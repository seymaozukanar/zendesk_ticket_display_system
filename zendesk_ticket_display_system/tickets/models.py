from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):

    zendesk_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=355, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    subject = models.TextField(max_length=355, blank=True, null=True)
    description = models.TextField(max_length=355, blank=True, null=True)
    creation_datetime = models.DateTimeField(blank=True, null=True)

    submitter = models.ForeignKey(User, related_name="tickets", on_delete=models.CASCADE,  null=True)
    requester = models.CharField(max_length=255, blank=True, null=True)
    assignee = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self, *args, **kwargs):
        return f'{self.zendesk_id}'


class Comment(models.Model):

    author = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(max_length=355, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, related_name="comments", on_delete=models.CASCADE)

'''
    Forms for adding and adjusting BugTicket model

    Created Ticket = 
    Status: New
    User Assigned: None
    User who Completed: None
    User who filed: Person who's logged in
'''
from django import forms
from bug_ticket_app.models import BugTicket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = [
            'title',
            'description',
        ]


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = [
            'title',
            'description'
        ]


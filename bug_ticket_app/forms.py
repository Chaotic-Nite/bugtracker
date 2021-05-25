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
    def __init__(self, *args, **kwargs):
        super(CreateTicketForm, self).__init__(*args, **kwargs)

        self.fields['status'].inital = dict(BugTicket.STATUS_CHOICES).get('New')
        self.fields['status'].required = False
        self.fields['assigned_user'].required = False

    class Meta:
        model = BugTicket
        fields = [
            'title',
            'description',
            'status',
            'assigned_user'
        ]


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = [
            'title',
            'description'
        ]


from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from bug_user_app.models import CustomUser
from bug_user_app.forms import LoginForm
from bug_ticket_app.models import BugTicket
from bug_ticket_app.forms import CreateTicketForm, EditTicketForm


@login_required(login_url='/login/')
def index(request):
    new_tickets = BugTicket.objects.filter(status='New')
    progress_tickets = BugTicket.objects.filter(status='In Progress')
    done_tickets = BugTicket.objects.filter(status='Done')
    invalid_tickets = BugTicket.objects.filter(status='Invalid')
    return render(request, 'index.html', {'new':new_tickets, 'progress':progress_tickets, 'done':done_tickets, 'invalid':invalid_tickets})


@login_required(login_url='/login/')
def user_detail_view(request, user_id):
    current_user = CustomUser.objects.get(id=user_id)
    working_tickets = BugTicket.objects.filter(assigned_user=current_user)
    filed_tickets = BugTicket.objects.filter(filed_user=current_user)
    completed_tickets = BugTicket.objects.filter(completed_user=current_user)
    return render(request, 'user_detail.html', {'current_user': current_user, 'progress': working_tickets, 'filed':filed_tickets, 'completed':completed_tickets})


# Stack Overflow Daniel Roseman for saving additional fields
@login_required(login_url='/login/')
def create_ticket_view(request):
    if request.method ==  'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.filed_user = request.user
            obj.save()
            newest_id = BugTicket.objects.latest('id')
            return HttpResponseRedirect(reverse('ticket_detail', args=(newest_id.id,)))
    
    form = CreateTicketForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required(login_url='/login/')
def edit_ticket_view(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    if ticket.filed_user == request.user:
        if request.method ==  'POST':
            form = CreateTicketForm(request.POST, instance=ticket)
            form.save()
            return HttpResponseRedirect(reverse('ticket_detail', args={ticket_id,}))
        
        form = EditTicketForm(instance=ticket)
        return render(request, 'generic_form.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('homepage'))


@login_required(login_url='/login/')
def ticket_detail_view(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def assign_view(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    if ticket.assigned_user == None:
        ticket.status = 'In Progress'
        ticket.assigned_user = request.user
    else:
        ticket.status = 'New'
        ticket.assigned_user = None
    ticket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'], '/')


def done_view(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'Done'
    ticket.completed_user = ticket.assigned_user
    ticket.assigned_user = None
    ticket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'], '/')


def invalid_view(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'Invalid'
    ticket.assigned_user = None
    ticket.completed_user = None
    ticket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'], '/')


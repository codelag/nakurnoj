from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *

# clients, contacts, payers
@login_required(login_url='login')
def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/clients.html', context)
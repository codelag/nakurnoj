from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
@login_required(login_url='login')
def lists(request):

    tasks = Tdlist.objects.order_by('-cr_date')

    context = {
        'tasks': tasks
    }

    return render(request, 'tdlists/lists.html', context)


@login_required(login_url='login')
def add_task(request):

    if request.method == 'POST':

        user_id = request.POST['user_id']
        task = request.POST['task']

        tdlist = Tdlist(
            task=task,
            user_id=user_id
        )

        tdlist.save()

        return redirect('tdlists')
    
    else:

        return redirect('tdlists')

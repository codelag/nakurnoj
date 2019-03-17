from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
@login_required(login_url='login')
def lists(request):

    user_id = request.user.id

    tasks = Tdlist.objects.order_by('-cr_date').filter(user_id=user_id)

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


@login_required(login_url='login')
def edit(request, task_id):

    if request.method == 'POST':

        new_value = request.POST['task']

        task = Tdlist.objects.get(pk=task_id)

        task.task = new_value

        task.save()

        return redirect('tdlists')

    else:
        
        task = Tdlist.objects.get(pk=task_id)

        context = {
            'task': task
        }

        return render(request, 'tdlists/edit.html', context)


@login_required(login_url='login')
def delete(request, task_id):

    task = Tdlist.objects.get(pk=task_id)

    task.delete()

    return redirect('tdlists')


@login_required(login_url='login')
def check(request, task_id):

    task = Tdlist.objects.get(pk=task_id)

    if task.is_check == True:
        task.is_check = False
    else:
        task.is_check = True
    task.save()

    return redirect('tdlists')
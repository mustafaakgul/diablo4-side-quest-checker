from django.shortcuts import render, redirect
from django.http import HttpResponse
from quests.models import Quest
from quests.forms import QuestForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def quest_dashboard(request):
    if request.method == "POST":
        form = QuestForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, ("Quest added successfully!"))
        return redirect('todolist')
    else:
        all_quests = Quest.objects.filter(manage=request.user)
        paginator = Paginator(all_quests, 10)
        page = request.GET.get('pg')
        all_quests = paginator.get_page(page)

        return render(request, 'quests/quests.html', {'all_quests': all_quests})


@login_required
def delete_quest(request, id):
    quest = Quest.objects.get(pk=id)
    # quest = get_object_or_404(Todo, id = id)
    if quest.manage == request.user:
        quest.delete()
    else:
        messages.error(request, ("Access Restricted, You Are Not Allowed!"))

    return redirect('quests')


@login_required
def edit_quest(request, id):
    if request.method == "POST":
        quest = Quest.objects.get(pk=id)
        # quest = get_object_or_404(Todo, id = id)
        form = QuestForm(request.POST or None, instance=quest)
        if form.is_valid():
            form.save()
        messages.success(request, ("Quest edited successfully!"))
        return redirect('quests')
    else:
        quest = Quest.objects.get(pk=id)
        return render(request, 'quests/edit.html', {'quest': quest})


@login_required
def complete_quest(request, id):
    quest = Quest.objects.get(pk=id)
    if quest.manage == request.user:
        quest.done = True
        # quest.done = not quest.done
        quest.save()
    else:
        messages.error(request, ("Access Restricted, You Are Not Allowed."))

    return redirect('quests')


@login_required
def pending_quest(request, id):
    quest = Quest.objects.get(pk=id)
    quest.done = False
    quest.save()

    return redirect('quests')


def index(request):
    context = {
        'index_text': "Welcome Index Page.",
    }
    return render(request, 'quests/index.html', context)


def contact(request):
    context = {
        'contact_text': "Welcome Contact Page.",
    }
    return render(request, 'core/contact.html', context)


def about(request):
    context = {
        'about_text': "Welcome About Page.",
    }
    return render(request, 'core/about.html', context)


def index_sample(request):
    #return HttpResponse("main page")
    context = {
        "number1" : 10,
        "number2" : 20,
        "number" : 30,
        "numbers" : [1,2,3,4,5]
    }
    todos = Todo.objects.all()

    return render(request, "index.html", {"todos":todos})
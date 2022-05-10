from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

class newTaskForm(forms.Form):
    task = forms.CharField(label ="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.

def index(request):
    if "task_list" not in request.session:
        request.session["task_list"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["task_list"]
    })

def add(request):
    if request.method == "POST":
        form  = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["task_list"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": newTaskForm()
    })
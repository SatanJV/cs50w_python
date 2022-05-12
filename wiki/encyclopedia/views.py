from turtle import title
from xml.dom import ValidationErr
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from . import util

class newSearchForm(forms.Form):
    query = forms.CharField(label ="")

class newEntryForm(forms.Form):
    title = forms.CharField(label ="", error_messages={'already_exists': 'This entry already exists!'})
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if util.get_entry(title) != None:
            raise forms.ValidationError(self.fields['title'].error_messages['already_exists'])
        return title

class newEditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": newSearchForm()
    })

def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "content": util.get_entry(entry),
        "form": newSearchForm()
    })

def query_results(request):
    if request.method == "POST":
        form = newSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            result = util.get_entry(query)
            if result != None:
                return HttpResponseRedirect("entry/" + query)
            else:
                entry_list = util.list_entries()
                result_list = []
                for entry in entry_list:
                    if entry.upper().find(query.upper()) != -1:
                        result_list.append(entry)
            return render(request, "encyclopedia/query_results.html", {
                "form": newSearchForm(),
                "results": result_list
            })
        else:
            return render(request, "index.html", {
                "form": form
            })
    return render(request, "encyclopedia/query_results.html", {
        "form": newSearchForm()
    })

def add_new(request):
    if request.method == "POST":
        form = newEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect("entry/" + title)
        else:
            return render(request, "encyclopedia/add_new.html", {
                "entry_form": form,
                "form": newSearchForm()
            })
    return render(request, "encyclopedia/add_new.html", {
        "entry_form": newEntryForm(),
        "form": newSearchForm()
    })

def edit(request, entry):
    if request.method == "POST":
        content=util.get_entry(entry)
        form = newEditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(entry, content)
            return HttpResponseRedirect("entry/" + entry)
        else:
            return render(request, "encyclopedia/edit.html", {
                "entry": entry,
                "content": content,
                "edit_form": form,
                "form": newSearchForm()
            })
    content = util.get_entry(entry)
    return render(request, "encyclopedia/edit.html", {
        "entry": entry,
        "content": content,
        "form": newSearchForm(),
        "edit_form": newEditForm()
    })
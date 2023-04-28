import markdown2
import random as r
from django.shortcuts import render, redirect
from . import util
from django import forms
from django.contrib import messages

class NewPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title of your page'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter contents of your page in Markdown'}))

class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter contents of your page in Markdown'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def random(request):
    title = r.choice(util.list_entries())
    return redirect("entry", title)

def entry(request, title):
    if util.get_entry(title) != None:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "contents": markdown2.markdown(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

def error(request):
    return render(request, "encyclopedia/error.html")

def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) == None:
                util.save_entry(title, content)
                messages.add_message(request, messages.SUCCESS, "Page was succesfully created")
                return redirect(entry, title=title)
            else:
                return render(request, "encyclopedia/error2.html", {
                    "title": title,
                })
        else:
            return render(request, "encyclopedia/new.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/new.html", {
            "form": NewPageForm()
        })

def edit(request, title):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            messages.add_message(request, messages.SUCCESS, "Page was succesfully edited")
            return redirect("entry", title=title)
        else:
            return render(request, "encyclopedia/edit.html", {
                "form": form
            })
    else:
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": EditPageForm(initial={'content':entry})
        })
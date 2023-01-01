from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if util.get_entry(title) != None:
        return render(request, "encyclopedia/entry.html", {
            "contents": markdown2.markdown(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title,
        })

def error(request):
    return render(request, "encyclopedia/error.html")


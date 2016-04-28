from django.http import HttpResponse
from django.shortcuts import render

from planner.forms import PlannerForm
from .models import Planner

def planner_list(request):
    queryset = Planner.objects.all()
    context = {
        "title" : "List",
        "object_list" : queryset
    }
    return render(request, "planner_list.html", context)


def planner_create(request):
    form = PlannerForm(request.POST or None, request=request)
    months_list = request.POST.getlist('month')   # Ex: ['Jan', 'Mar', 'Dec']

    # Preparing JSONField datatype for saving
    temp_dict = {}
    for i in months_list:
        # Intentionally use this format because query is easier than store list.
        temp_dict[i] = True
    # import pdb; pdb.set_trace()
    context = { "form" : form }
    return render(request, "planner_post.html", context)


def planner_detail(request, id=None):
    return HttpResponse("Get")


def planner_update(request, id=None):
    return HttpResponse("Update")


def planner_delete(request, id=None):
    return HttpResponse("Delete")

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
    print(request)
    month = request.POST
    print(month)
    import pdb; pdb.set_trace()

    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.save()
    # else:
    #     return HttpResponse("Invalid Submitted Form")
    return render(request, "planner_post.html")


def planner_detail(request, id=None):
    return HttpResponse("Get")


def planner_update(request, id=None):
    return HttpResponse("Update")


def planner_delete(request, id=None):
    return HttpResponse("Delete")

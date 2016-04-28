from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
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
    if request.method == 'POST':
        form = PlannerForm(request.POST or None, request=request)
        if form.is_valid():
            comment = request.POST.getlist('comment')
            scheduler_type = request.POST.getlist('scheduler_type')
            start_type = request.POST.getlist('start_type')
            start_time = request.POST.getlist('start_time')
            stop_time = request.POST.getlist('stop_time')
            month_list = request.POST.getlist('month_list')
            week_day = request.POST.getlist('week_day')
            date_day = request.POST.getlist('date_day')
            new_record = Planner.objects.create(

            )
            # import pdb; pdb.set_trace()
            return HttpResponseRedirect(reverse('list'))
    else:
        print(request)
        form = PlannerForm()
    context = {
        "form": form
    }
    return render(request, "planner_post.html", context)


def planner_detail(request, id=None):
    return HttpResponse("Get")


def planner_update(request, id=None):
    return HttpResponse("Update")


def planner_delete(request, id=None):
    return HttpResponse("Delete")

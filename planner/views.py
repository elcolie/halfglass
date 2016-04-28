from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

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
        form = PlannerForm(request.POST or None)
        if form.is_valid():
            comment = request.POST.get('comment')
            scheduler_type = request.POST.get('start_type')
            start_type = request.POST.get('start_type')
            month_list = request.POST.getlist('month_list')
            week_day = request.POST.getlist('week_day')
            date_day = request.POST.getlist('date_day')
            start_time = request.POST.get('start_time')
            stop_time = request.POST.get('stop_time')
            stop_type = request.POST.get('stop_type')
            lifetime_quantity = request.POST.get('lifetime_quantity')
            lifetime_unit = request.POST.get('lifetime_unit')
            new_record = Planner.objects.create(comment=comment,
                                                scheduler_type=scheduler_type,
                                                start_type=start_type,
                                                start_time=start_time,
                                                stop_time=stop_time,
                                                month_json=month_list,
                                                weekday_json=week_day,
                                                schedule_days=date_day,
                                                stop_type=stop_type,
                                                lifetime_quantity=lifetime_quantity,
                                                lifetime_unit=lifetime_unit,
                                                )
            new_record.save()
            return HttpResponseRedirect(reverse("planner:list"))
    else:
        form = PlannerForm()
    context = {
        "form": form
    }
    return render(request, "planner_post.html", context)


def planner_detail(request, id):
    instance = get_object_or_404(Planner, id=id)
    context = {
        "title": instance.comment,
        "instance": instance,
    }
    # import pdb; pdb.set_trace()
    return render(request, "planner_detail.html", context)


def planner_update(request, id=None):
    return HttpResponse("Update")


def planner_delete(request, id=None):
    return HttpResponse("Delete")

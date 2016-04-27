from django.http import HttpResponse


def scheduler_list(request):
    return HttpResponse("List")


def scheduler_create(request):
    return HttpResponse("Post")


def scheduler_detail(request):
    return HttpResponse("Get")


def scheduler_update(request):
    return HttpResponse("Update")


def scheduler_delete(request):
    return HttpResponse("Delete")

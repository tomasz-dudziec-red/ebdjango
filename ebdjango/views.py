from django.http import HttpResponse


def index(request):
    return HttpResponse("bababababaaba12334")

    # Leave the rest of the views (detail, results, vote) unchanged

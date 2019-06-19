# coding=utf-8
import json

from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext

from ebdjango.models import TVSetting


def index(request):
    return HttpResponse("bababababaaba12334")

    # Leave the rest of the views (detail, results, vote) unchanged


def index2(request):
    template = loader.get_template("ebdjango/index.html")
    title_string = "This is a title"
    context = RequestContext(request, {
        'title': title_string,
    })
    return HttpResponse(template.render(context))


def example(request):
    template = loader.get_template("ebdjango/index2.html")
    title_string = "This is a title"
    context = RequestContext(request, {
        'title': title_string,
    })
    return HttpResponse(template.render(context))


def coming_soon(request):
    template = loader.get_template("ebdjango/coming_soon.html")
    title_string = "This is a title"
    context = RequestContext(request, {
        'title': title_string,
    })
    return HttpResponse(template.render(context))


def tvsettings(request):
    return JsonResponse({'color': 'blue',
                         'size': 5,
                         'theme': 'dark',
                         'featuredApps': [1, 2, "youtube", 5.0],
                         'themeURL': 'https://www.istockphoto.com/pl/zdj%C4%99cie/golden-cebuli-na-drewnianym-tle-rustykalnym-gm480134211-36493838'})


def dynamic_tvsettings(request):
    tvSettingObject = TVSetting.objects.first()
    return JsonResponse({'color': tvSettingObject.color,
                         'size': tvSettingObject.size,
                         'featuredApps': [1, 2, "youtube", 5.0],
                         'publication_date': tvSettingObject.pub_date,
                         'themeURL': tvSettingObject.themeURL})


def get_cards(request):
    path_to_cards_file = './static/ebdjango/resources/results.txt'

    with open(path_to_cards_file) as json_file:
        data = json.load(json_file)

    what_to_show = {"nothing_to_sho": True}

    print data
    return JsonResponse(data, safe=False)

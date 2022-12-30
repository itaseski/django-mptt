from django.http import HttpResponse


def index(request):
    response = "My List of Food Recipes Goes Here"
    return HttpResponse(response)

from django.http import HttpResponse
from django.template import loader

#This is what is currently displayed to the dialogue screen.
def index(request):
    return HttpResponse("Hello, world. You're at the dialogue index.")
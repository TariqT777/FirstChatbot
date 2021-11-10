from django.http import HttpResponse
from django.template import loader
from chatbotDialogue import ChatbotTalk
#This is what is currently displayed to the dialogue screen.
def index(request):
    return HttpResponse("Hello, world. You're at the dialogue index.")

def chatbot(request): #Trying to display chatbot output from chatbotTalk file but having issues.
    return HttpResponse(ChatbotTalk.talk)
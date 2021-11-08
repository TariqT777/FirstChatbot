#Tariq Thomas 
#10/21/21

import chatterbot
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
#import train
chatbot = ChatBot(
    "Allen Iverson",
    logic_adapters=[
    {"import_path": "chatterbot.logic.BestMatch", 
    "statement_comparison_function": LevenshteinDistance,
    "response_selection_method": chatterbot.response_selection.get_first_response}] #These three statements allow the bot to make an accurate choice given input from a user.
   ) #Creates new chatbot. Allen Iverson initials : A.I. 

trainer = ChatterBotCorpusTrainer(chatbot)


#This trains the chatbot with pre-set dialogue. The chatbot will be able to reactively learn from conversations using this trainer.
trainer.train(
    "chatterbot.corpus.english" 
)

def talk():
    while True: #This will allow the user to continue having dialogue with the chatbot until the user decides to stop.
        request = input('Talk to me: ')
        response = chatbot.get_response(request)
        print(response)
        yield response
        if request == "":
            break
talk()

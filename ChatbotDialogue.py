#Tariq Thomas 
#10/21/21
import chatterbot
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import train
chatbot = ChatBot(
    "Allen Iverson",
    logic_adapters=[
    {"import_path": "chatterbot.logic.BestMatch", 
    "statement_comparison_function": LevenshteinDistance,
    "response_selection_method": chatterbot.response_selection.get_first_response}] #These three statements allow the bot to make an accurate choice given input from a user.
   ) #Creates new chatbot. Allen Iverson initials : A.I. 

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)


while True:
    request = input('Talk to me: ')
    response = chatbot.get_response(request)
    print(response)

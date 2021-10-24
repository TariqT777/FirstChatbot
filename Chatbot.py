#Tariq Thomas 
#10/21/21
import chatterbot
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ListTrainer
import train
chatbot = ChatBot(
    "Allen Iverson",
    logic_adapters=[
    {"import_path": "chatterbot.logic.BestMatch", 
    "statement_comparison_function": LevenshteinDistance,
    "response_selection_method": chatterbot.response_selection.get_first_response}] #These three statements allow the bot to make an accurate choice given input from a user.
   ) #Creates new chatbot. Allen Iverson initials : A.I. 


trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')

print(response)

'''
response = chatbot.get_response("What's your fav sport?")
print(response)
'''
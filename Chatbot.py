#Tariq Thomas 
#10/21/21
import chatterbot
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
chatbot = ChatBot(
    "Allen Iverson",
    logic_adapters=[
    {"import_path": "chatterbot.logic.BestMatch",
    "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
    "response_selection_method": chatterbot.response_selection.get_first_response}]
   ) #Creates new chatbot. Allen Iverson initials : A.I. 
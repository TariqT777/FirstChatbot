from Chatbot import chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hi friend"
])

trainer.train([
    "Hey",
    "Hi, nice to meet you"
])
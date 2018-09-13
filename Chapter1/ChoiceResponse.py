import random


responses = {
    "what's your name?" : [
        "my name is EchoBot",
        "they call me EchoBot",
        "the name's Bot, Echo Bot"
    ]
}

def respond(msg) :
    if msg in responses :
        return random.choice(responses[msg])


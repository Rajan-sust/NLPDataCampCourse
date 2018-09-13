import random

responses = {
    "what's your name?" : ["my name is EchoBot","they call me EchoBot",
        "the name's Bot, Echo Bot"
    ]
}

default = ["sorry!I'd not understand you","Soory! I'm small brain"]

def respond(msg) :
    if msg in responses :
        return random.choice(responses[msg])
    return random.choice(default)


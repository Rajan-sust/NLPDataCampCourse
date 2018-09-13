import re

def swapPronoun(text) :
    if 'I' in text:
        text = re.sub('I','You',text)
    if 'my' in text :
        text = re.sub('my','your',text)
    return text

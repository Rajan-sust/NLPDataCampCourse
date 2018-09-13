import re

# adding parenthesis define group

pattern = "if (.*)"
text = "what would happen if bots took over the world"

match = re.search(pattern,text)

try :
    print(match.group(0)) # if bots took over the world
    print(match.group(1)) # bots took over the world

except :
    print("no matched")


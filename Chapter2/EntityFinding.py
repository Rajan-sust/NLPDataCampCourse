import re

pattern = re.compile("[A-Z]{1}[a-z]*")
msg = "Mary is a good girl.Bob also good boy"

ls = pattern.findall(msg)

print(ls)


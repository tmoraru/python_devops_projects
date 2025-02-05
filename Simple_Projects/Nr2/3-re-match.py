#REGULAR EXPERESION

import re

text = "Todays was so cold outside"
pattern = r"so"

# match will check if outside is available in pattern text
match = re.match(pattern, text)

# if it match will print it
if match:
    print("Match found:", match.group())
#if not 
else:
    print("Match not found")
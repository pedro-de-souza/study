import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")

# Match 1
# Match 2

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())    

# abcdefghi
# abcdefghi
# bc
# de
# ('bc', 'de', 'fgh', 'g')


pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

# abc
# ('abc', 'ghi')

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")

# Match 1
# Match 2
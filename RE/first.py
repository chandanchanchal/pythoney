import re

print("without raw string:")
# path_to_search = "c:\example\task\new"
target_string = r"c:\example\task\new\exercises\session1"

# regex pattern
pattern = "^c:\\example\\task\\new"
# \n and \t has a special meaning in Python
# Python will treat them differently
res = re.search(pattern, target_string)
print(res.group())

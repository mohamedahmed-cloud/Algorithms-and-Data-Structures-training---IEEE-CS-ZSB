import re
string = input()
pattern = re.compile("^\w{1,16}@(\w{1,16}\.)*\w{1,16}(|/\w{1,16})$")
if pattern.match(string):
    print("YES")
else:
    print("NO")

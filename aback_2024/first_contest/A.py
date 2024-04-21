import re
pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[a-z]).{8,}$'

nickname = input()


if re.match(pattern, nickname):
    print("YES")
else:
    print("NO")

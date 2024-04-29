import re

text = input()
text = text.replace(', ', ',')
text = text.replace(' ,', ',')
text = text.replace(',', ', ')

split_text = text.split(' ')

max_length = 0
for word in split_text:
    if len(word.strip(',')) > max_length:
        max_length = len(word.rstrip(','))

max_length *= 3

output = []
current_line = ''
for word in split_text:
    spaces = 0 if len(current_line) == 0 else 1
    if len(current_line) + len(word) + spaces <= max_length:
        current_line += ' '*spaces + word
    else:
        if current_line[-1] == ' ':
            current_line = current_line.rstrip(' ')
        print(current_line)
        current_line = word
if current_line[-1] == ' ':
    current_line = current_line.rstrip(' ')
print(current_line)

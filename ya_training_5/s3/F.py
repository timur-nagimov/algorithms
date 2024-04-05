set_dict = set(input().split())
words = list(input().split())
ans = ''

for i in range(len(words)):
    for let_i in range(len(words[i])):
        splited_part = str(words[i][:let_i+1])
        if splited_part in set_dict:
            words[i] = splited_part
            break


print(' '.join(words))

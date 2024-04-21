str_1 = input().strip()
str_2 = input().strip()

final_str = ''
command = ''
cursor_position = 0

i = 0
while i < len(str_2):
    if str_2[i] == '<':
        if cursor_position is None:
            cursor_position = len(final_str)
        i += 1
        command = ''
        while i < len(str_2) and str_2[i] != '>':
            if str_2[i] != ' ':
                command += str_2[i]
            i += 1
        i += 1

        if command == 'left':
            cursor_position = max(0, cursor_position - 1)
        elif command == 'right':
            cursor_position = min(len(final_str), cursor_position + 1)
        elif command == 'delete':
            if cursor_position < len(final_str):
                final_str = final_str[:cursor_position] + \
                    final_str[cursor_position + 1:]
        elif command == 'bspace':
            if cursor_position > 0:
                final_str = final_str[:cursor_position -
                                      1] + final_str[cursor_position:]
                cursor_position = max(0, cursor_position - 1)
        cursor_position = min(cursor_position, len(final_str))
    else:
        if str_2[i] != ' ':
            if cursor_position is None:
                cursor_position = len(final_str)
            final_str = final_str[:cursor_position] + \
                str_2[i] + final_str[cursor_position:]
            cursor_position += 1
        i += 1

# print('FINAL:', final_str)
if final_str == str_1:
    print("YES")
else:
    print("NO")

f = open('input.txt')
dict = {}
mx = 1
for line in f:
    b = line.split()
    b = ''.join(b)
    line = b
    for c in line:
        if c in dict:
            dict[c] += 1
            mx = max(mx, dict[c])
        else:
            dict[c] = 1
s = ""
for i in dict:
    s += i
s = sorted(s)
for i in range(mx):
    str = ''
    for i in s:
        if dict[i] >= mx:
            str += '#'
        else:
            str += ' '
    print(str)
    mx -= 1
print(*s, sep="")

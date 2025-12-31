a = input()
t = ""
mode = 0
i = 0

if ('-' not in a and '+' not in a):
    print(int(a))
else:
    while (a[i] != '-' and a[i] != '+'):
        t += a[i]
        i += 1
    sum = int(t)
    if (a[i] == '-'):
        mode = 1
    t = ""
    for j in range (i+1, len(a)):
        if (a[j] != '-' and a[j] != '+'):
            t += a[j]
        else:
            x = int(t)
            t = ""
            if (mode == 1):
                sum -= x
            elif (a[j] == '+' and mode == 0):
                sum += x
            elif (a[j] == '-' and mode == 0):
                mode = 1
                sum += x
    if (mode == 0):
        sum += int(t)
    else:
        sum -= int(t)
    print(sum)
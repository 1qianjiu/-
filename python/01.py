#maopaopaixu

txt = [12,43,2,44,11,23,4,34]
a = 0
p = 0
y = 0

for y in range(len(txt)-1):
    for p in range(len(txt)-y-1):
        if txt[p] > txt[p + 1]:
              a = txt[p]
              txt[p] = txt[p + 1]
              txt[p + 1] = a
print(txt)



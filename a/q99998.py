while True:
    s = input()
    if not s:
        break

    values = s.split(" ")
    print(values)

# =======

lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

print(lines) # print(",".join(lst)) ---- for loop

# ====
lst = []
while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x)
print(lst) # print(",".join(lst)) ---- for loop
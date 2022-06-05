Num, Kol = list(map(int, input().split()))
menu = input()
al = ''
Control = [{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'v': 0, 'u': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}]
for m in menu:
    c = Control[-1].copy()
    c[m] += 1
    Control.append(c)
    if m not in al:
        al += m
laf = len(al)*Kol
def delta(i,ii):
    maxx = 0
    for a in al:
        d = Control[ii+1][a] - Control[i][a]
        if d > maxx:
            maxx = d
        if maxx > Kol:
            break
    return maxx
find = False
Kout1 = 0
Uout2 = 0
for lenght in range(laf, 0, -1):
    for firstDay in range(0, Num-lenght):
        d = delta(firstDay, firstDay+lenght)
        if d <= Kol:
            Kout1 = lenght
            Uout2 = firstDay
            find = True
            break
    if find:
        break
print(Kout1+1, Uout2+1)

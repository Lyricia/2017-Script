from getStationInfo import *

from tkinter import messagebox

#dictlist = getStationInfo('05158')

d = dict()
d1 = dict()
d2 = dict()
l = list()

d['a'] = 'aa'
d['b'] = 'bb'
d['c'] = 'cc'
d1['a'] = 'aa1'
d1['b'] = 'bb1'
d1['c'] = 'cc1'
d2['a'] = 'aa2'
d2['b'] = 'bb2'
d2['c'] = 'cc2'
l.append(d)
l.append(d1)
l.append(d2)




print ('\n'.join(str(p) for p in l))
print(l)
s = str()
for d in l:
    for d2 in d:
        s+=d[d2]
        s+='\n'

print(s)
messagebox.showinfo('a', s )
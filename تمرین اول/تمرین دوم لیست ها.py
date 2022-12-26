import random

mlist = [
1,2,3,5,4,6,9,10,22,11,13]

if mlist == 2:
    print(mlist)
else:
       pass
       
       
mp = [1,2,4,5]
mp.extend(mlist)
mp.sort()
mp.remove(1)
if mp != 10:
    mp.append(12)
    
elif not mp == 13:
    mp.remove(5)

var = random.randint(10,30)
print(var,mp)

import random
import matplotlib.pyplot as plt
import numpy as np
freq=int(input("Enter no of time you want to toss a coin"))
head=0#head =1
tail=0#tail=2
t=[]
tosscounth=[]
tosscountt=[]
y=[]
count=0
for i in range(1,freq+1):
    toss=random.randrange(1,3)
    y.append(i)
    if(toss==1):
        head=head+1
        tosscounth.append(head/i)
        tosscountt.append(tail/i)
    else:
        tail=tail+1
        tosscounth.append(head/i)
        tosscountt.append(tail/i)


print("no of head=",head)
print("no of tails=",tail)
print(y[:11])
print(tosscounth[:11])
print(tosscountt[:11])
plt.plot(y,tosscountt,tosscounth)
plt.xlabel("TOSS COUNT(FREQUENCY)")
plt.ylabel("PROPORTION")
plt.show()






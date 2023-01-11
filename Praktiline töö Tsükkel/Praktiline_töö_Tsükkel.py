from math import * 
from random import * 
#Ülesanne 7

import random
результат= ""
for i in range(5):
    результат +=str(random.randint(0, 8))
print(результат)


# Ülesanne 0
# Väljund tsüklite abil, paaritute numbritega 1 kuni 50.

x=0
while True:
    if x==50:
        break
    elif x%2==1:

        print(x, end=" ")
    x+=1

x=0
while x<=50:
    if x%2==1:
        print(x, end=" ")
    x+=1

for x in range(0,50,1):
    if x%2==1:
        print(x, end=" ")
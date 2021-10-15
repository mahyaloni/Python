# multiply, odd/even numbers
a=[2, 3, 4, 5, 6, 7, 8, 9]
i=[2*a for a in range(2,10)]
print(i)
# [4, 6, 8, 10, 12, 14, 16, 18]

for num in a:
    if num%2==0:
        print(num*2)   
# [4, 8, 12, 16]

a=[i for i in a if i%2!=0]
print(a)  
# [3, 5, 7, 9]

for num in a:
    if num%2==0:
        print(num*2)
    elif num%2==1:
        print(num.real)
print(list(reversed(a)))
# [9, 7, 5, 3]

import random
list_1=random.sample(range(1,100),15)
even_list=[]
odd_list=[]
for num in list_1:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(even_list, odd_list)
# [48, 50, 52, 54, 34, 40] [5, 49, 69, 43, 15, 37, 93, 17, 31]

def result(k0:float,r:float,n:int):
    kn=k0*(1+r)**n
    return kn
k0=float(input('enter Initial Capital'))
r=float(input('enter Interest Rate'))
n=int(input('enter Time'))
kn=result(k0,r,n)
print(f'Capital after{n} years:{kn}')

# enter Initial Capital 20
# enter Interest Rate 50
# enter Time 12
# Capital after 12 years:6.192586887512428e+21
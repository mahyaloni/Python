import numpy as np
from numpy import random
A1=random.rand(5,5)
B1=random.rand(5,7)
Z1=random.rand(7,5)
A=A1.round(2)
B=B1.round(2)
Z=Z1.round(2)
print(A)
print(B)
print(Z)
print(A@B)
print(A*(-6))
print(A**2)
print(A@A)
H=A@B@Z
print(H)
print(np.transpose(H))
print(np.linalg.det(H))
I=np.eye(5)
print(I)
I1=I-A
print(I1)
print(np.linalg.inv(I1))
print(Z@(np.linalg.inv(I1)))
a=np.full((5,5),1)
zro=np.zeros((3,3))
a[1:4,1:4]=zro
a[2,2]=9
print(a)
import numpy as np
import matplotlib.pyplot as plt
k=np.linspace(0,100,100)
f=1*(k**(0.5))
plt.figure(figsize=(10,7))
plt.plot(1*(k**(0.5)))
plt.plot(2*(k**(0.5)))
plt.plot(3*(k**(0.5)))
plt.plot(4*(k**(0.5)))
plt.plot(5*(k**(0.5)))
plt.plot(6*(k**(0.5)))
plt.title('cobb_douglas production function $f(k)=A.k^a$',fontname='Times new roman',loc='center')
plt.xlabel('capital',fontname='Times new roman')
plt.ylabel('output',fontname='Times new roman')
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
GDP=np.linspace(0,5000,10)
Life_exp=np.random.rand(10)*100
Freedom=np.arange(10)*10
z=GDP+Freedom*20

scale=np.random.rand(100)
color=np.random.rand(100)
plt.figure(figsize=(12,7))
plt.scatter(GDP,Life_exp,c=Freedom,s=1000)
plt.colorbar().set_label('Freedom',fontsize=15)
plt.xlabel('GDP')
plt.ylabel('Lif_expectancy')
plt.title('Camparing GDP, Lif_expectancy and Freedom in2017', loc='center')
plt.grid()
plt.show()


# output
[[0.99 0.09 0.81 0.53 0.39]
 [0.12 0.33 0.91 0.49 0.3 ]
 [0.01 0.77 0.52 0.77 0.42]
 [0.76 0.69 0.4  0.74 0.9 ]
 [0.36 0.41 0.91 0.86 0.95]]
[[0.21 0.65 0.1  0.74 0.48 0.87 0.25]
 [0.34 0.34 0.75 1.   0.85 0.94 0.96]
 [0.75 0.32 0.64 0.93 0.01 0.39 0.23]
 [0.07 0.94 0.1  0.76 0.97 0.12 0.16]
 [0.38 0.77 0.74 0.41 0.56 0.84 0.97]]
[[0.75 0.4  0.4  0.14 0.5 ]
 [0.89 0.55 0.87 0.88 0.88]
 [0.18 0.43 0.52 0.43 0.87]
 [0.36 0.51 0.87 0.09 0.56]
 [0.19 0.86 0.32 0.09 0.83]
 [0.78 0.51 0.05 0.95 0.78]
 [0.89 0.41 0.74 0.16 0.87]]
[[1.0313 1.7318 1.0265 2.1386 1.2923 1.653  0.9833]
 [0.9682 1.173  1.1129 1.7605 0.9905 1.0803 0.9255]
 [0.8674 1.4819 1.2991 2.0184 1.6466 1.3805 1.3919]
 [1.088  2.2452 1.5895 2.5558 2.1771 2.3106 1.9358]
 [1.3187 2.2045 1.7149 2.5658 1.8966 1.9547 1.752 ]]
[[-5.94 -0.54 -4.86 -3.18 -2.34]
 [-0.72 -1.98 -5.46 -2.94 -1.8 ]
 [-0.06 -4.62 -3.12 -4.62 -2.52]
 [-4.56 -4.14 -2.4  -4.44 -5.4 ]
 [-2.16 -2.46 -5.46 -5.16 -5.7 ]]
[[9.801e-01 8.100e-03 6.561e-01 2.809e-01 1.521e-01]
 [1.440e-02 1.089e-01 8.281e-01 2.401e-01 9.000e-02]
 [1.000e-04 5.929e-01 2.704e-01 5.929e-01 1.764e-01]
 [5.776e-01 4.761e-01 1.600e-01 5.476e-01 8.100e-01]
 [1.296e-01 1.681e-01 8.281e-01 7.396e-01 9.025e-01]]
[[1.5422 1.2681 1.8719 1.9201 1.6008]
 [0.6479 1.2815 1.3397 1.5466 1.254 ]
 [0.8439 1.3589 1.6694 1.714  1.5453]
 [1.7256 1.4837 2.5665 2.3705 2.1924]
 [1.4103 1.8513 2.3464 2.5458 2.3221]]
[[ 5.679457  5.254652  5.537376  4.14622   7.347725]
 [ 4.458746  4.19107   4.573978  3.06829   5.940377]
 [ 5.558338  5.440812  5.693696  3.84815   7.652714]
 [ 7.959205  7.501393  7.683304  5.74234  10.627296]
 [ 7.6277    7.132213  7.570516  5.400886 10.151205]]
[[ 5.679457  4.458746  5.558338  7.959205  7.6277  ]
 [ 5.254652  4.19107   5.440812  7.501393  7.132213]
 [ 5.537376  4.573978  5.693696  7.683304  7.570516]
 [ 4.14622   3.06829   3.84815   5.74234   5.400886]
 [ 7.347725  5.940377  7.652714 10.627296 10.151205]]
0.0021896924259843663
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
[[ 0.01 -0.09 -0.81 -0.53 -0.39]
 [-0.12  0.67 -0.91 -0.49 -0.3 ]
 [-0.01 -0.77  0.48 -0.77 -0.42]
 [-0.76 -0.69 -0.4   0.26 -0.9 ]
 [-0.36 -0.41 -0.91 -0.86  0.05]]
[[ 2.52179589 -1.14555177 -0.20774463 -0.6648936  -0.91644235]
 [-0.98818272  1.27679992  0.15212869 -0.0839402  -0.28006821]
 [-1.16051224  0.51482359  0.70084375 -0.00732658 -0.20784496]
 [ 0.60382574 -0.69965312 -0.7545181   0.30316472 -0.36906494]
 [-0.68168801 -0.44245761 -0.47066121 -0.39445408  0.9743604 ]]
[[ 0.77556053 -0.46169466 -0.15558263 -0.68996089 -0.44698593]
 [ 0.6227334  -0.87446203 -0.56964567 -0.72463117 -0.61783633]
 [-0.90788517 -0.07525605 -0.34145798 -0.37239917  0.29552728]
 [-0.93317329  0.37592081  0.28105472 -0.48215478 -0.14115318]
 [-1.25351657  0.61492805 -0.14292624 -0.50097492  0.29401019]
 [ 1.4469198  -1.22640864 -1.13332093 -0.58146053 -0.45866266]
 [ 0.48400792 -0.61196627 -0.13409373 -0.92626115 -0.29562378]]
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]












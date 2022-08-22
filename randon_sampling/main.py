import pandas as pd
import numpy as np
from random import choice
data=pd.read_csv('parkinsons.csv')
a=data['MDVP:Jitter(%)']
b=data['MDVP:Jitter(Abs)']
c=data['MDVP:RAP']
d=data['MDVP:PPQ']
e=data['Jitter:DDP']
f=data['MDVP:Shimmer']
g=data['MDVP:Shimmer(dB)']
h=data['Shimmer:APQ3']
i=data['Shimmer:APQ5']
j=data['MDVP:APQ']
k=data['Shimmer:DDA']
l=data['NHR']
m=data['status']
n=data['RPDE']
o=data['DFA']
p=data['spread1']
q=data['spread2']
r=data['D2']
s=data['PPE']
a=np.std(a)
b=np.std(b)
c=np.std(c)
d=np.std(d)
e=np.std(e)
f=np.std(f)
g=np.std(g)
h=np.std(h)
i=np.std(i)
j=np.std()
k=np.std(a)
l=np.std(a)
m=np.std(a)
n=np.std(a)
o=np.std(a)
p=np.std(a)
q=np.std(a)
r=np.std(a)
s=np.std(s)


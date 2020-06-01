import numpy as np
from pandas import *

Index= ['aaa','bbb','ccc','ddd','eee']
Cols = ['A', 'B', 'C','D']
df = DataFrame(abs(np.random.randn(5, 4)), index= Index, columns=Cols)
df.save('testando_denovo_essa_merda.html')
''' df
          A         B         C         D
aaa  2.431645  1.248688  0.267648  0.613826
bbb  0.809296  1.671020  1.564420  0.347662
ccc  1.501939  1.126518  0.702019  1.596048
ddd  0.137160  0.147368  1.504663  0.202822
eee  0.134540  3.708104  0.309097  1.641090
'''
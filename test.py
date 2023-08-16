
innt = 100_000
adj_innt = 172_000
skatt_kr = 37_840
s = 0.22
adj = 1.72

Se = s*adj
x=0.3784


import re
from rates import Rates
r = Rates('Norway')
print(r.tax)

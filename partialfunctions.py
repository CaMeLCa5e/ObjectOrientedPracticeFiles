#partial functions

from functools import partial

#create a new function that multiplies things by 2
dbl =  partial(multiply,2)
print dbl(4)


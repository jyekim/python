import numpy 
speed =[99, 86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

"89.76923076923077"

from scipy import stats                         
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)


import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)


import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)
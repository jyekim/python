import numpy 
speed =[99, 86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

"89.76923076923077"

from scipy import stats                         
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)
import math

error = math.pow(10, -7)


def f(x) :
	return math.pow(x,2) - 4*x + 4 - math.log(x)

c0 = 2
c1 = 4 
for i in range(10): 
	c2 = (c0*f(c1) - c1*f(c0)) / (f(c1)-f(c0))

	print i
	print c2
	print f(c2)

	if math.fabs(f(c2)) < error :
		print "f(c2) is less than acceptable error"
		break
	else :
		c0 = c1 
		c1 = c2
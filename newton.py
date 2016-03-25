import math

def f(x):
	return math.exp(x) + math.pow(2,-x) + 2*math.cos(x) - 6

log2 = .6931
# the derivative f(x)
def g(x):
	return math.exp(x) + (-2**-x)*log2  - 2*math.sin(x)

error = math.pow(10, -6)

c0 = 1.5000

for i in range(10):
	c1 = c0 - (f(c0)/g(c0))
	print i
	print c1

	if (math.fabs(c0 - c1) < error):
		break

	else :
		c0 = c1

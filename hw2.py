# import math
# e = 0;
# a = 0;
# b = 1;
# c = 1;

# for i in range(5):
# 	print math.e * math.e
# 	print math.exp(c) - (2*math.pow(c,2)) + (3*c) - 2
# 	print "hello world"


# def bisection(a, b, e):
# 	c = (a + b)/2
# 	print c


# bisection(1,2,3);

import math

# while(result > math.pow(10, -8))
a = 0.0
b = 1.0
error = math.pow(10, -8)

def f(c):
	return math.exp(c) - math.pow(c,2) + (3*c) - 2

for i in range(20):
	c = (a+b)/2
	print i
	print c 
	print f(c)

	# if f(c) < error:
	# 	break;
	if f(a) * f(c) > 0:
		print f(a)
		print "made it here"
		a = c
	elif f(a) * f(c) < 0:
		b = c
	else : 
		break;


	# if (abs(result) < error):
	# 	break
	# elif ():

	# if computeFunction(c) < error:
	# 	print "made it"
	# else 

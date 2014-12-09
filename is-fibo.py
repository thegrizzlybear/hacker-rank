from math import sqrt

def isfibo(number):
	l = 5 * (number ** 2) - 4
	r = 5 * (number ** 2) + 4


	sq_l = int(sqrt(l))
	sq_r = int(sqrt(r))


	if sq_l ** 2 == l or sq_r ** 2 == r:
		print "IsFibo"
	else:
		print "IsNotFibo"


if __name__ == '__main__':
	
	test_cases  = input()
	numbers = []

	for i in range(test_cases):
		numbers.append(input())


	for num in numbers:
		isfibo(num)

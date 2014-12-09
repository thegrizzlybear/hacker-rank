'''
	Program to find the length of the utopian tree

'''

if __name__ == '__main__':
	
	length= 1
	tree_length = []
	for i in range(61):
		if i == 0:
			pass
		elif i%2 != 0:
			length= 2*length
		else:
			length = length + 1

		tree_length.append(length)


	test_cases = input()
	cycles = []
	for i in range(test_cases):
		cycles.append(input())


	for i in cycles:
		print tree_length[i]

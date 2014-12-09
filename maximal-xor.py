'''
	find the maximal XOR value between a range
'''

def find_maximal_xor(l,r):
	xor_values = []
	for i in range(l,r+1):
		for j in range(l,r+1):
			xor_values.append(i^j)	

	return max(xor_values)

if __name__ == '__main__':
	l = input()
	
	r = input()


	print find_maximal_xor(l,r)

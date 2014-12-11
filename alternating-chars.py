
'''
	finds what is the minimum number of deletions needed
'''


def need_deletions(l_str):
	str_list = list(l_str) # convert string in list
	count = 0
	for i in range(len(str_list)-1):
		if str_list[i] == str_list[i+1]:
			count += 1
		else:
			continue
	return count			

if __name__ == '__main__':
	 
	test_cases = input()
	lovely_strings = []	

	for i in range(test_cases):
		lovely_strings.append(raw_input())


	for l_str in lovely_strings:
		print need_deletions(l_str)

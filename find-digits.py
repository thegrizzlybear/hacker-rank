def give_count(number):
       count = 0
       for i in range(len(number)):
		print number[i],number
                if int(number[i])!= 0:
                       if int(number)%int(number[i]) == 0:
                            count += 1
                            
       print count
                            

if __name__ == '__main__':
       test_cases = int(raw_input())
       numbers = []
       for i in range(test_cases):
            numbers.append(raw_input())
            
       print numbers, test_cases
       for num in numbers:
            give_count(num)

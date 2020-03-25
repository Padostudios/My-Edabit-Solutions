def index_multiplier(lst):
	counter =0
	summ = 0	
	for i in lst:
		i*counter
		summ = summ + i*counter
		counter = counter + 1
	return summ
		
print(index_multiplier([1,2,3,4,5]))



#another solution
def index_multiplier(lst):
	return sum([i*lst[i] for i in range(len(lst))])
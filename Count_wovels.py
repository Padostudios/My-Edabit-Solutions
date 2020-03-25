def count_vowels(txt):
	flag = 0
	wovels=["a","e","o","u","i"]
	for i in txt:
		if i in wovels:
			flag=flag+1
	return flag


print(count_vowels("Prediction"))



#another solution

def count_vowels(txt):
	return sum([1 for i in txt.lower() if i in "aeiou"])
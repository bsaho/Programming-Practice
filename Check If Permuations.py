import collections

def checkIfPermutations (s1,s2):
	set1= set (s1)
	set2= set (s2)

	if set1==set2:
		return "True"
	else:
		return "False"


print (checkIfPermutations("Lord of the Rings", "Lord of the Rings"))
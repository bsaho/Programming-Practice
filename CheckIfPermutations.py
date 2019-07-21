import collections

def checkIfPermutations (s1,s2):
	s1=s1.replace (" ","")
	s2=s2.replace (" ","")
	set1= set (s1.lower ())
	set2= set (s2.lower ())
	print (set1)
	print (set2)

	if set1==set2:
		return "True"
	else:
		return "False"


print (checkIfPermutations("COYA", "YOCA"))
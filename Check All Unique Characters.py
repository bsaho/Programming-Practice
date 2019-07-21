def checkIfUnique (s):

	#python uses timsort, which has O(n) space complexity
	s=sorted (s)
	for i in range (0, (len (s) -1)):
		if s[i]==s[i+1]:
			return "Not unique"
	return "Unique"


print (checkIfUnique ("GeeksforGeeks"))
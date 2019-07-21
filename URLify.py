def URLify (s):
	s=s.strip ()
	s_array= s.split()
	print (s_array)
	URL_string=""

	for x in range (0,len (s_array)):
		
		if x != ( len (s_array) -1):
			# print ((len (s_array)-1))
			print (x)
			print (s_array[x])

			URL_string=URL_string + s_array[x] + "%0"
		else:
			URL_string+=s_array[x]
	return URL_string



print ("Result: " + URLify ("Mr John Smith  "))

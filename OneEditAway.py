def checkOneEditAway (str1, str2):
	lenDiff= len (str1) - len (str2)
	
	if lenDiff<-2 or lenDiff>2:
		print ("False")


checkOneEditAway ("pale","palelll")


# reading hilary's favorite foods file into a list
hilary_file = open("hilary_fav_foods.txt")
hilary_favs = hilary_file.read().splitlines()
hilary_file.close()


#reading tonya's favorite foods file into a list
tonya_file = open("tonya_fav_foods.txt")
tonya_favs = tonya_file.read().splitlines()
tonya_file.close()

def compare_favs(a, b):
	if (a[0] == b[0]):
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different"

compare_favs(hilary_favs, tonya_favs)

def compare_favs2(a, b):
	for x in a:
		for y in b:
			if x == y:
				print "We both love " + x + "!"

compare_favs2(hilary_favs, tonya_favs)


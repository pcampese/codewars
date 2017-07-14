def recoverSecret(triplets):
	import pprint
	import collections
	import operator

	# Print arguments
	print('triplets = ')
	pprint.pprint(triplets)
	print

	# Rotate the matrix
	rotated = list(zip(*triplets))
	print('triplets rotated =')
	pprint.pprint(rotated)
	print

	# Turn it into a list of sets
	set_list = [set(row) for row in rotated]
	print('set_list')
	pprint.pprint(set_list)
	print

	# Get the first letter
	first = set_list[0] - set_list[1] - set_list[2]
	print('first = {}'.format(first))
	print

	# Get the last letter
	last = set_list[2] - set_list[0] - set_list[1]
	print('last = {}'.format(last))
	print

	# For each row (in the rotated triplet) (i.e. column in original triplet)
	# get the set of each
		

	# Flatten the list
	flat = []
	for triplet in triplets:
		flat.extend(triplet)
	print('flat = {}'.format(flat))
	print

	# Try counting everything
	count = dict(collections.Counter(flat))
	print('count = ')
	pprint.pprint(count)
	print

	# Sort the count, based on values
	count_sorted = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
	print('count_sorted = ')
	pprint.pprint(count_sorted)
	print

	return 0
	
	
	
	
# w h a t i s u p
  # ['t','u','p'],				t			u	p	
  # ['w','h','i'],	w	h			i				
  # ['t','s','u'],				t		s	u		
  # ['a','t','s'],			a	t		s			
  # ['h','a','p'],		h	a					p	
  # ['t','i','s'],				t	i	s			
  # ['w','h','s']		w	h				s			

# w
# w	h
# w	h	a
# w	h	a	t
# w	h	a	t	u
# w	h	a	t	u	p
	# Need to fail here, because we already reached the last letter, but we still have unused letters: ['i', 's']
# w	h	a	t	u
	# No other options where 'u' is NOT the last letter.  Go backwards again
# w	h	a	t	s
# w	h	a	t	s	u
# w	h	a	t	s	u	p
# w	h	a	t	s	u
	# No other options where 'u' is NOT the last letter.  Go backwards again
# w	h	a	t	s
	# No other options where 's' is NOT the last letter.  Go backwards again
# w	h	a	t	i
# w	h	a	t	i	s
# w	h	a	t	i	s	u
# w	h	a	t	i	s	u	p
	# SOLVED


# m a t h i s f u n
# [['t', 's', 'f'],			t			s	f			
 # ['a', 's', 'u'],		a				s		u		
 # ['m', 'a', 'f'],	m	a					f			
 # ['a', 'i', 'n'],		a			i				n	
 # ['s', 'u', 'n'],						s		u	n	
 # ['m', 'f', 'u'],	m						f	u		
 # ['a', 't', 'h'],		a	t	h						
 # ['t', 'h', 'i'],			t	h	i					
 # ['h', 'i', 'f'],				h	i		f			
 # ['m', 'h', 'f'],	m			h			f			
 # ['a', 'u', 'n'],		a						u	n	
 # ['m', 'a', 't'],	m	a	t							
 # ['f', 'u', 'n'],							f	u	n	
 # ['h', 's', 'n'],				h		s			n	
 # ['a', 'i', 's'],		a			i	s				
 # ['m', 's', 'n'],	m					s			n	
 # ['m', 's', 'u']]	m					s		u		
 

# l o v e
 # ['l', 'o', 'e'],	l	o		e
 # ['o', 'v', 'e']]		o	v	e
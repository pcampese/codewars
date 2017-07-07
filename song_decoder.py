# https://www.codewars.com/kata/dubstep/train/python

def song_decoder(song):
	# Print arguments
	print('song = {}'.format(song))

	# Split on WUB
	# Then, loop through and only keep elements that are NOT empty (i.e. '')
	# Then, join the final word

	return ' '.join([w for w in song.split('WUB') if w !=  ''])
def generate_bc(url, separator):
	import cgi
	import re

	print('url = [{}]'.format(url))
	separator = separator.strip()	# Remove whitespace before/after the separator
	print('separator = [{}]'.format(separator))
	print

	url_components = url.split('/')
	print('url_components = {}'.format(url_components))

	# print('url_components[0]: {} --> Trash'.format(url_components[0]))
	# print('url_components[1]: {} --> Keep both UPPER and lower versions of it'.format(url_components[1]))
	# print('url_components[2]: {} --> Strip out the .html at the end'.format(url_components[2]))

	# Get the page file name (i.e extract 'webpage' from webpage.html?more)
	# Goal: url_components[2].split('.')[0].upper()
	html = url_components[-1]			# Grab the last element, which has the name.html (or similar) text
	html = re.split('\.|\?|#', html)	# Use re.split to split on various anchors (., ?, #)
	print('html = {}'.format(html))

	html = html[0].upper()	# Strip out the page name only (before the '.html').  Upercase it.
	
	# If the 'html' page is INDEX, then remove it from the url list
	if (html == 'INDEX'):
		url_components.pop()
		html = url_components[-1].upper()

	print

	html_tags = [
		'<a href="/">HOME</a> ',
#		separator,
		' <a href="/',
#		url_components[1],
		'/">',
#		url_components[1].upper(),
		'</a> ',
#		separator,
		' <span class="active">',
#		html,
		'</span>'
	]
	
	# Format the output
	# Process the first element in the array the sameway
	beginning = '<a href="/">HOME</a> '
	# Repeat the middle items the same way
	middle = ''
	memory = ''
	for element in url_components[1:-1]:
		print('element = {}'.format(element))
		memory += element + '/'
		middle += ''.join([separator, ' <a href="/', memory, '">', element.upper(), '</a> ',])
	# Process the last element the same way
	end = ''.join([separator, ' <span class="active">', html, '</span>'])

	result = ''.join([beginning, middle, end])
	print('result = {}'.format(result))

	return result
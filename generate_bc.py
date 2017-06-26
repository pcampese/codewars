def generate_bc(url, separator):
	import re

	# Display variables that are passed in to the method
	print('url = [{}]'.format(url))
	separator = separator.strip()	# Remove whitespace before/after the separator
	print('separator = [{}]'.format(separator))
	print

	# Split the url into it's components, separate by '/'
	print('+ Split the url')
	url_components = url.split('/')
	print('url_components = {}'.format(url_components))
	print

	# Replace all '-'s with spaces (for url elements that are less than 30 characters)
	print("Replace - with ' '")
	for index in range(len(url_components)):
		value = url_components[index]
		if (len(value) < 30):
			url_components[index] = value.replace('-', ' ')
	print('url_components = {}'.format(url_components))
	print

	# Merge back any http or https links that were broken during the "split on '/'" operation earlier
	# Example, https://www.site.com should stay together, instead of
	# being split into: http:, '', www.site.com
	print('Merge back links starting with http or https')
	if (url_components[0] == 'http:' or url_components[0] == 'https:'):
		url_components[0] += url_components.pop(1)
		url_components[0] += '//'
		url_components[0] += url_components.pop(1)
	print('url_components = {}'.format(url_components))
	print
	
	# Remove any trailing empty '' (i.e. created due to a trailing / at the end: www.home.com/)
	print("Remove any trailing ''")
	url_components = [element for element in url_components if element]
	print('url_components = {}'.format(url_components))
	print

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

	# Reference list of HTML tags to use for formatting output
	html_tags = [
		'<a href="/">HOME</a> ',
		' <a href="/',
		'/">',
		'</a> ',
		'<span class="active">',
		'</span>'
	]

	# If the number of url_components is 1, do special formatting...
	if (len(url_components) == 1 ):
		print('+ Length = 1')
		result = html_tags[4] + 'HOME' + html_tags[5]
	else:
		# Format the output
		# Process the first element in the array the sameway
		print('+ Processing: Beginning')
		beginning = '<a href="/">HOME</a> '

		# Repeat the middle items the same way
		print('+ Processing: Middle')
		middle = ''
		tag = ''
		for element in url_components[1:-1]:
			print('element = {}'.format(element))
			# If the element is longer than 30 characters, then it needs special processing
			length = len(element)
			if (length >= 30):
				print('++ Special Processing for length: [{}]'.format(length))
				element_list = element.split('-')
				value = ''
				print('++ element_list = {}'.format(element_list))
				# Remove words from this list
				removal_list = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
				for word in element_list:
					if word not in removal_list:
						print('+++ Process word: [{}]'.format(word))
						value += word[0]
				print('++ value: [{}]'.format(value))
			else:
				value = element
			tag += element + '/'
			middle += ''.join([separator, ' <a href="/', tag, '">', value.upper(), '</a> ',])

		# Process the last element the same way
		print('+ Processing: End')
		end = ''.join([separator, ' <span class="active">', html, '</span>'])

		# Prepare the final result
		result = ''.join([beginning, middle, end])
	print('result = {}'.format(result))

	return result
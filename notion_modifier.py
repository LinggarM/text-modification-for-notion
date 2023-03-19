import time
from youtube_helper import get_title, get_channel_name

def notion_modifier(inputfile, outputfile, modify_type= 'add_bullet'):
	"""
	Modify text in the 'inputfile' with various modify type and write the output to the 'outputfile'

	Parameters:
	inputfile (string): the name of the input file which will be processed ('.txt' format)
	outputfile (string): the name of the output file which will be used to write the output ('.txt' format)
	modify_type (string): the type of the modification that will be done to the text, (option: 'add_newline', 'add_bullet', 'add_number', 'normalize_notion_link', 'add_youtube_title_and_channel_name')
	"""

	# Read the file
	with open(inputfile, 'r') as f :

		# Get the input text
		text = f.read()

		# Type: Add New Line
		if (modify_type == 'add_newline'):
			text = add_newline(text)

		# Type: Add Bullet
		if (modify_type == 'add_bullet'):
			text = add_bullet(text)

		# Type: Add Number
		if (modify_type == 'add_number'):
			text = add_number(text)

		# Type: Normalize Notion Link
		if (modify_type == 'normalize_notion_link'):
			text = normalize_notion_link(text)

		# Type: Add Youtube Title & Channel Name
		if (modify_type == 'add_youtube_title_and_channel_name'):
			text = add_youtube_title_and_channel_name(text)

		# Write text to the output file
		with open(outputfile, 'w') as f :
			f.write(text)

def add_newline(text):
	"""
	Add new line for every new line in the 'text', so that the output will have double new line for each new line from the input

	Parameters:
	text (string): the text which will be processed

	Returns:
	text_output (string): the output text that already processed
	"""
	# Add new line for each new line
	text_output = text.replace("\n", "\n\n")

	# Return the output
	return text_output

def add_bullet(text):
	"""
	Add '- ' (hyphen and spaces) in start of each line of the 'text'

	Parameters:
	text (string): the text which will be processed

	Returns:
	text_output (string): the output text that already processed
	"""
	# Add bullet in the first line
	text_output = f"- {text}"

	# Add bullet for all lines after the first line
	text_output = text_output.replace("\n", "\n- ")

	# Return the output
	return text_output

def add_number(text):
	"""
	Add number in start of each line from of the text
	The number will be from 1 to the number of the lines
	The format is like this -> ("1. ")

	Parameters:
	text (string): the text which will be processed

	Returns:
	text_output (string): the output text that already processed
	"""
	# Split the text for each line
	text_splitted = text.split('\n')

	# Initialize the output text
	text_output = ""

	# Add number in the start of each line
	for i, data in enumerate(text_splitted):
		text_output = f"{text_output}{i+1}. {data}\n" 

	# Return the output
	return text_output

def normalize_notion_link(text):
	"""
	This function used to normalize the format of text with url link in notion

	Example Input:
	- [https://www.youtube.com/watch?v=H8kocPOT5v0](https://www.youtube.com/watch?v=H8kocPOT5v0) Polynomial Regression in Python
	- [https://www.geeksforgeeks.org/life-cycle-phases-of-project-management/](https://www.geeksforgeeks.org/life-cycle-phases-of-project-management/)

	Example Output:
	- https://www.youtube.com/watch?v=H8kocPOT5v0
	- https://www.geeksforgeeks.org/life-cycle-phases-of-project-management
	"""
	# Split the text for each line
	url_list = text.split("\n")

	# Initialize the output text
	text_output = ""

	for data in url_list:
		# Check whether it's a link format or just a text
		if '[' in data:
			# Get the url only
			url = data.split("[")[1].split("]")[0]

			# Append to text_output
			text_output = f"{text_output}- {url}\n"
		else:
			text_output = f"{text_output}{data}\n"

	# Return the output
	return text_output

def add_youtube_title_and_channel_name(text):
	# Split the text for each line
	url_list = text.split("\n")

	# Initialize the output text
	text_output = ""

	# Initialize time counter
	begin = time.time()

	for data in url_list:
		# Check whether it's a link format or just a text
		if 'http' in data:
			# Get the pure url
			url = f"http{data.split('http')[1]}"

			# Get the title & channel name
			title = get_title(url)
			channel_name = get_channel_name(url)

			# Append to text_output
			text_output = f"{text_output}- {url} {title} - {channel_name}\n"
		else:
			text_output = f"{data}\n"
	
	# Get processing time
	time.sleep(1)  # store end time 
	end = time.time()  # total time taken
	print(f"Processing complete {end - begin} seconds")

	# Return the output
	return text_output
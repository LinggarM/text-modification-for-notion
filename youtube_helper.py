from pytube import YouTube, Playlist

def get_title(url):
	"""
	Get the title for a given URL (video or playlist)
	
	Parameters:
	url(string): url of the video or playlist
	
	Returns:
	title: the title of the video or playlist
	"""
	# Initialize the channel name
	title = ""

	# Check if the URL is a playlist or a video
	if 'playlist' in url:
		# Get playlist data and title
		title = Playlist(url).title
	else:
		# Get video data and title
		title = YouTube(url).title

	# Return the title
	return title

def get_channel_name(url):
	"""
	Get the channel name for a given URL (video or playlist)
	
	Parameters:
	url(string): url of the video or playlist
	
	Returns:
	channel_name: the name of the channel
	"""
	# Initialize the channel name
	channel_name = ""

	# Check if the URL is a playlist or a video
	if 'playlist' in url:
		# Get playlist data and owner channel name
		channel_name = Playlist(url).owner
	else:
		# Get video data and author channel name
		channel_name = YouTube(url).author

	# Return the channel name
	return channel_name
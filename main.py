from notion_modifier import *

input_filename = "files/input.txt"
output_filename = "files/output.txt"

# notion_modifier(input_filename, output_filename, 'add_newline')
# notion_modifier(input_filename, output_filename, 'add_bullet')
# notion_modifier(input_filename, output_filename, 'add_number')
# notion_modifier(input_filename, output_filename, 'normalize_notion_link')
notion_modifier(input_filename, output_filename, 'add_youtube_title_and_channel_name')
# 3 user inputs, a text file, string to search for, string to replace the search string
input_file = input('Drag and drop the text file to be edited: ')
search_string = input('What string would you like to replace? ')
replacement_string = input('What would you like to replace it with? ')

# input_file when dragged into terminal already has '' around it, input defaults to string type and the file path ends up coming in like "'/Users/shane/Desktop/find_and_replace.txt'", if those single quotes are present conditionally replace them with empty string to get valid file path
formatted_file_path = input_file if "'" not in input_file else input_file.replace("'", "")

print(formatted_file_path)

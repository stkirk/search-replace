# 3 user inputs, a text file, string to search for, string to replace the search string
input_file = input('Drag and drop the text file to be edited: ')
search_string = input('What string would you like to replace? ')
replacement_string = input('What would you like to replace it with? ')

formatted_file_path = input_file if "'" not in input_file else input_file.replace("'", "")

print(formatted_file_path)

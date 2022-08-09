# 3 user inputs, a text file, string to search for, string to replace the search string
input_file = input('Drag and drop the text file to be edited: ')
search_string = input('What string would you like to replace? ')
replacement_string = input('What would you like to replace it with? ')

# input_file when dragged into terminal already has '' around it, input defaults to string type and the file path ends up coming in like "'/Users/shane/Desktop/find_and_replace.txt'", if those single quotes are present conditionally replace them with empty string to get valid file path
formatted_file_path = input_file if "'" not in input_file else input_file.replace("'", "")

# open file in read/write mode
file_in = open(formatted_file_path, "r+")

# read file to string value
text = file_in.read()
#count occurences of search string param
search_count = text.count(search_string)

# replace search_string with replacement string
new_text = text.replace(search_string, replacement_string)
# count occurences of replacement
replacement_count = new_text.count(replacement_string)

# clear text from file to 0 bytes --> maybe change later to sile_in.write(new_text)
file_in.truncate(0)

# write new text into file
file_in.write(new_text)

# close file
file_in.close()

print('---------------------------------------')
print(f"{search_string} found {search_count} times")
print(f"replaced by {replacement_string} {replacement_count} times")

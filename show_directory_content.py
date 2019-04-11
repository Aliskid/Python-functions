def show_directory_content(path_of_directory, extension):

	'''prints all the file ending by the specified extension in the asked directory'''

	print "Please choose a valid", "."+extension, "file :\n"
	for entry in os.listdir(path_of_directory):
		if fnmatch.fnmatch(entry, "*."+extension):
			return entry

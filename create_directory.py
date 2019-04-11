def create_directory(path):

	'''creates a folder in the specified path'''
	
	try:
		if not os.path.exists(path):
			os.makedirs(path)
		print ("%s directory has been successfully created" % path)
	except OSError:  
		print ("The creation of the directory %s failed" % path)

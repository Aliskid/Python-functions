def multiprocessing_functions():

	''' Intermediate function to speed your function's execution
	by using multiprocessing '''

	manager = multiprocessing.Manager()
	info_dict = manager.dict()
	jobs = []
	p = multiprocessing.Process(target=your_function, args=(...))
	jobs.append(p)
	p.start()
	for proc in jobs:
		proc.join()
	return info_dict

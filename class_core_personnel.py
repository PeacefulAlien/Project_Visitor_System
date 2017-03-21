import class_personnel

class core_personnel(class_personnel):
	
	def __init__(self, first, last, ID_number, mobile_number, status=None):
		super().__init__(first, last, ID_number, mobile_number)
		if status == None:
			status = list()
		else:
			status = status
  
	
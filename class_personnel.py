class all_personnel():
	
	def __init__(self, first, last, ID_number, mobile_number):
		self.first = first
		self.last = last
		self.full = first + " " + last
		self.ID_number = ID_number
		self.mobile_number = mobile_number
	  
if __name__ == "__main__":
  test_personnel_01 = all_personnel("zao", "sun", "2070", "0763929606")
  print(test_personnel_01.full)
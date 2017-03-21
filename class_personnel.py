import datetime

class all_personnel():
	
	def __init__(self, first, last, ID_number, mobile_number):
		self.first = first
		self.last = last
		self.full = first + " " + last
		self.ID_number = ID_number
		self.mobile_number = mobile_number
		
		if bool[checkin_input == "t"]:
			self.avi_list.append(self.full)
		elif bool[checkin_input == "f"]:
			self.unavi_list.append(self.full)
		else:
			self.avi_list = self.avi_list
			self.unavi_list = self.unavi_list
		#status(checkin list) require external input
		
		self.checkin_date = today()if bool[checkin_input == "t"]
		self.checkin_time = checkin_time
		self.checkout_time = checkout_time
		#checkin_date & checkin_time requires external input
	
	
	
	def demo_avi_list():
		print(avi_list)
	
	def demo_unavi_list():
		print(unavi_list)
		
	
if __name__ == "__main__":
  test_personnel_01 = all_personnel("zao", "sun", "2070", "0763929606")
  print("{0}{1}".format(test_personnel_01.status, test_personnel_01.full))

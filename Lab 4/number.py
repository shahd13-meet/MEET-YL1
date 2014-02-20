class Integer(object):
	def __init__(self,number):
		self.number = number

	def Display(self, np):
		if np == "negative":
			print (self.number - 2*self.number)
		elif np == "positive":
		 	print self.number


class NegativeInteger(Integer)
	def __init__(self, number):
		Integer.__init__(self,number,False):
	def display(self)
		Integer.Display(self)
	print "This is a negative number"
			
		     
		
if __name__=="__main__":
   	print "Michele"

	print "Enter a number"	
	test = Integer(input())
	print "negative or positive?"
	np = raw_input()
	test.Display(np)










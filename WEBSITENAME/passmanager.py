"""
Manages the passwordList module of the ITSP app.
"""

from ITSP.models import passwordList
import string
import random

__obj__ 		= passwordList.objects
allObjs 		= __obj__.all()
__obj_count 	= len(list(allObjs))

def updateCount():
	"""
		Refreses the count, you won't need this.
	"""
	global __obj__
	global allObjs
	global __obj_count
	__obj__ 		= passwordList.objects
	allObjs 		= __obj__.all()
	__obj_count 	= len(list(allObjs))


def generate(count=150):
	"""
		Generates random string passwords lowercase and numbers and adds "count" number of objects in module
	"""
	temp=''
	for x in range(count):
		temp = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
		passwordList.objects.create(password = temp);
	updateCount()

def reset():
	"""
		Removes all passwords.
	"""
	response = raw_input( "This is going to delete all the objects from model passwordList. Do you intend to do that? (Y/n) :")
	if(response == "Y") :	allObjs.delete()
	else : print "Action canceled by user." 
	updateCount()

def count():
	"""
		returns the number of objects in module
	"""
	return __obj_count
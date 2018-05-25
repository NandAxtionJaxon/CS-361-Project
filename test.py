import PyUnit
import urllib
import webapp2
import unittest
from login import Login

#wanted to test page navigation from one to the other if something went wrong but we did not know how.

#CHANGES

class TestS1(unittest.TestCase):

	def setUp(self):
		self.login = Login()
		
	def tear(self):
		del self.login
		
	def test_correct_login(self):
		self.login.login_open()
		self.assertEqual(self.login.Username[0], "jacks429")
		self.assertEqual(self.login.password[0], "12345")
		self.assertEqual(self.login.account[0], "student")
		self.assertEqual(self.login.count, "3")
		
#also, at this point we realize that there is not much to test as far as back and forth communication between pages and users...
#Once we get to databases it will be pertinent to test, but for this phase we literally write text files and then read from them. We saw it as counterproductive to write a ton of lists for potential users when we knew that we would be using databases soon.
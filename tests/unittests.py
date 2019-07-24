import sys
sys.path.append('..')
import unittest
from hyperspinxmltotext import functions

test_xml_file = "menuexample.xml"
test_minidom_object = functions.parse_xml_file(test_xml_file)

class TestFileRead(unittest.TestCase):

	def test_decodes_nodename(self):	
		self.assertEqual(functions.parse_xml_file_nodename(), '#document')

	def test_returns_minidom_document(self):
		# self.assertEqual(type(functions.parse_xml_file(test_xml_file)), '<class \'xml.dom.minidom.Document\'>')
		# NOTE: Had to use assertMultiLineEqual since assertEqual also compares the object types -not just their values.
		self.assertMultiLineEqual(str(type(functions.parse_xml_file(test_xml_file))), '<class \'xml.dom.minidom.Document\'>')

	def test_game_names(self):
		# verify the game_names function returns... something?
		self.assertTrue(functions.game_names(test_minidom_object))

	
	#def test_game_names(self, test_minidom_object):
	#	# verify the game_names function returns... something?
	#	self.assertEqual(functions.game_names(test_minidom_object), '1941')

	#def test_game_descriptions(self):
	#    # verify the expected game name can be extreacted from the test XML file
	#	print("\ntesting game_descriptions...")
	#	print("\nsetting test_xml_file...")
	#	test_xml_file = "menuexample.xml"
	#	print("\nsetting test_minidom_object...")
	#	test_minidom_object = functions.parse_xml_file(test_xml_file)
	#	print("test_minidom_object is:")
	#	print(test_minidom_object)
	#	print("\nsetting first_game value...")
	#	first_game = functions.game_descriptions(test_minidom_object)
	#	print(first_game)
	#	self.assertEqual((first_game[0]), '1941: Counter Attack (World 900227)')

if __name__ == '__main__':
	unittest.main()
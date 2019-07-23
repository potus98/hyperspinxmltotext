import sys
sys.path.append('..')
import unittest
from hyperspinxmltotext import functions

test_xml_file = "menuexample.xml"

class TestFileRead(unittest.TestCase):

	def test_decodes_nodename(self):	
		self.assertEqual(functions.parse_xml_file_nodename(), '#document')

	def test_returns_minidom_document(self):
		# self.assertEqual(type(functions.parse_xml_file(test_xml_file)), '<class \'xml.dom.minidom.Document\'>')
		# NOTE: Had to use assertMultiLineEqual since assertEqual also compares the object types -not just their values.
		self.assertMultiLineEqual(str(type(functions.parse_xml_file(test_xml_file))), '<class \'xml.dom.minidom.Document\'>')

if __name__ == '__main__':
	unittest.main()
import sys
sys.path.append('..')
import unittest
from hyperspinxmltotext import functions

class TestFileRead(unittest.TestCase):

	def test_decodes_nodename(self):
		# self.assertTrue(main() == '#document')
		self.assertEqual(functions.parse_xml_file(), '#document')

if __name__ == '__main__':
	unittest.main()
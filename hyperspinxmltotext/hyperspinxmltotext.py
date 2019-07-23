from functions import parse_xml_file_nodename
from functions import parse_xml_file

filename = "/home/john/Databases-xml-menus/MAME/MAME.xml"

if __name__ == "__main__":
	print (parse_xml_file_nodename())
	print (type(parse_xml_file(filename)))

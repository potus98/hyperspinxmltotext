from functions import parse_xml_file_nodename
from functions import parse_xml_file
from functions import game_names
from functions import game_descriptions

filename = "/home/john/Databases-xml-menus/MAME/MAME.xml"

if __name__ == "__main__":
	print (parse_xml_file_nodename())

	print (type(parse_xml_file(filename)))

	doc = parse_xml_file(filename)
	
	print (game_names(doc))

	print (game_descriptions(doc))

	print (game_descriptions(doc)[0])
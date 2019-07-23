# from functions import parse_xml_file_nodename
# from functions import parse_xml_file
# from functions import game_names
# from functions import game_descriptions
from functions import *

filename = "/home/john/Databases-xml-menus/MAME/MAME.xml"
top_folder_filter = "/home/john/Databases-xml-menus"

if __name__ == "__main__":
	print (parse_xml_file_nodename())

	print (type(parse_xml_file(filename)))

	doc = parse_xml_file(filename)
	print (game_names(doc))

	print (game_descriptions(doc))

	print (game_descriptions(doc)[0])

	print (system_names(top_folder_filter))

	system_folders = system_names(top_folder_filter)
	print (menus_to_process(top_folder_filter, system_folders))

	menus_to_process_list = menus_to_process(top_folder_filter, system_folders)
	for menu in menus_to_process_list:
		doc = parse_xml_file(menu)
		print ("processing file %s: ", menu)
		print (game_descriptions(doc))

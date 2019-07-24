from functions import *

filename = "/home/john/Databases-xml-menus/MAME/MAME.xml"
top_folder_filter = "/home/john/Databases-xml-menus"


if __name__ == "__main__":

	doc = parse_xml_file(filename)
	system_names_list = system_names(top_folder_filter)
	for system_name in system_names_list:
		process_system(top_folder_filter, system_name)

	# Following was being used to help troubleshoot unittest
	#
	# names = game_names(doc)
	# print (names[0])

	# descriptions = game_descriptions(doc)
	# print (descriptions[0])

	# print (game_names(doc)[0])
from functions import *

filename = "/home/john/Databases-xml-menus/MAME/MAME.xml"
top_folder_filter = "/home/john/Databases-xml-menus"


if __name__ == "__main__":

	doc = parse_xml_file(filename)
	system_names_list = system_names(top_folder_filter)
	for system_name in system_names_list:
		process_system(top_folder_filter, system_name)

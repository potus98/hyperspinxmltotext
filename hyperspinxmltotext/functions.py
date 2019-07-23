import os
import sys
import xml.dom.minidom
import glob

def parse_xml_file_nodename():
	# load and parse an XML file then return the nodeName
	doc = xml.dom.minidom.parse("../tests/menuexample.xml");

	# print out the document node and a field
	# print (doc.nodeName)
	# print (doc.firstChild.tagName)
	return (doc.nodeName)

def parse_xml_file(filename):
	# load and parse an XML file and return a usable object
	doc = xml.dom.minidom.parse(filename)
	return (doc)

def game_names(minidom_object):
	# return list of game names from minidom object
	game_list = []
	games = minidom_object.getElementsByTagName("game")
	for game in games:
		game_name = game.getAttribute("name")
		game_list.append(game_name)
	return(game_list)

def game_descriptions(minidom_object):
	# return list of game names from minidom object
	description_list = []
	games = minidom_object.getElementsByTagName("game")
	for game in games:
		# game_description = game.getElementsByTagName("description")[0].firstChild.nodeValue
		game_description = game.getElementsByTagName("description")[0].firstChild.nodeValue
		description_list.append(game_description)
	return(description_list)

def system_names(top_folder_filter):
	# returns a list of system names (ie: folder names per Hyperspin configuration expectations)
	# system_list = []
	system_names = sorted(os.listdir(top_folder_filter))
	return(system_names)

# def menus_to_process(top_folder_filter, system_folders):
	# returns a list of xml files to process
	# menus_to_process_list = []
	# for system in system_folders:
	# 	menu_file = top_folder_filter + "/" + system + "/" + system +".xml"
	# 	menus_to_process_list.append(menu_file)
	# return(menus_to_process_list)

#def menu_to_process(top_folder_filter, system_name):
	# returns the xml menu file for a given system
	# return(top_folder_filter + "/" + system_name + "/" + system_name +".xml")


def process_system(top_folder_filter, system_name):
	# accepts a system name and prints a human-friendly list of game descriptions based on the system's xml menu
	menu_file_to_process = top_folder_filter + "/" + system_name + "/" + system_name +".xml"
	doc = parse_xml_file(menu_file_to_process)
	#print ("processing file: ", menu_file_to_process)
	section_header = "Emulator: " + system_name
	print ("\n================================================")
	print (section_header)
	print ("================================================")
	# print (game_descriptions(doc))
	game_descriptions_list = game_descriptions(doc)
	for game_description in game_descriptions_list:
		print(game_description)


# if __name__ == "__main__":
#	main();

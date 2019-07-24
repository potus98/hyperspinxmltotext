import os
import sys
import xml.dom.minidom
import glob


def parse_xml_file_nodename():
	# load and parse an XML file then return the nodeName
	doc = xml.dom.minidom.parse("../tests/menuexample.xml");
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
		game_description = game.getElementsByTagName("description")[0].firstChild.nodeValue
		description_list.append(game_description)
	return(description_list)


def system_names(top_folder_filter):
	# returns a list of system names (ie: folder names per Hyperspin configuration expectations)
	system_names = sorted(os.listdir(top_folder_filter))
	return(system_names)


def process_system(top_folder_filter, system_name):
	# accepts a system name and prints a human-friendly list of game descriptions based on the system's xml menu
	menu_file_to_process = top_folder_filter + "/" + system_name + "/" + system_name +".xml"
	doc = parse_xml_file(menu_file_to_process)
	section_header = "Emulator: " + system_name
	print ("\n================================================")
	print (section_header)
	print ("================================================")
	game_descriptions_list = game_descriptions(doc)
	for game_description in game_descriptions_list:
		print(game_description)


# if __name__ == "__main__":
#	main();

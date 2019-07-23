import os
import sys
import xml.dom.minidom

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
	

# if __name__ == "__main__":
#	main();

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

# if __name__ == "__main__":
#	main();

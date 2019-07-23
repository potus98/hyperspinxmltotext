import os
import sys
import xml.dom.minidom

def main():
	# use the parse() function to load and parse an XML file
	doc = xml.dom.minidom.parse("../tests/menuexample.xml");

	# print out the document node and a field
	print (doc.nodeName)
	print (doc.firstChild.tagName)


if __name__ == "__main__":
	main();

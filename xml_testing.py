# xml_testing.py

from xml.dom import minidom

xmldoc = minidom.parse('C:\\Users\\Max\\Downloads\\gcide_xml-0.51.zip\\gcide_xml-0.51\\xml_files.gcide_a.xml')


for i in xmldoc:
     print('test')

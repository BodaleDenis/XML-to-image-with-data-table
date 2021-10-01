import xml.etree.ElementTree as ET
import sys
from os import path

sys.path.append("./")


class XmlParser:
    def __init__(self, doc_name: str):
        self.parser = ET.parse(doc_name).getroot()
        self.root = ET.parse(doc_name)
        self.doc_name = doc_name

    def get_xml_root_name(self):
        return self.parser.tag

    def get_xml_root_value(self):
        return self.parser.attrib

    def get_node_tag_and_value(self, index: int):
        children_tag = self.parser[index].tag
        children_value = self.parser[index].attrib
        children_tag_value = (children_tag, children_value)
        return children_tag_value

    def get_values_of_child_node(self, index: int):
        node = self.parser[index]
        elements = []
        for element in node:
            element_value_tag = (element.tag, element.text)
            elements.append(element_value_tag)
        return elements


# Driver code
xmlparser = XmlParser("test/dummy.xml")
# print(len(xmlparser.parser))
print(xmlparser.get_xml_root_name())
print(xmlparser.get_xml_root_value())
print(xmlparser.get_node_tag_and_value(0))
print(xmlparser.get_values_of_child_node(0))

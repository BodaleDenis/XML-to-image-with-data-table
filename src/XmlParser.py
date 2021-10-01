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

    def format_atrib_data(self, key_values, dictionary):
        str_value = str()
        for key in key_values:
            str_value += dictionary[key] + " "
        return str_value

    def extract_elements_data(self):
        elements_value = list()
        elements_tag = list()
        elements_dict = dict()

        for node in self.parser:
            for element in node:
                elements_tag.append(element.tag)
                if element.attrib:
                    elements_value.append(
                        self.format_atrib_data(element.attrib.keys(), element.attrib)
                    )
                else:
                    elements_value.append(element.text)
        print(elements_tag)
        print(elements_value)
        for i, j in zip(elements_tag, elements_value):
            elements_dict.setdefault(i, []).append(j)
        return elements_dict


# Driver code
# xmlparser = XmlParser("test/dummy.xml")
# print(xmlparser.extract_elements_data())

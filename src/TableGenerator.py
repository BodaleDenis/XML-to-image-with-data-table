import sys
import os

sys.path.append("./")
from XmlParser import XmlParser
import plotly.graph_objects as plotly_graph


class TableGenerator:
    def __init__(self, doc_to_table):
        self.xml_data = XmlParser(doc_to_table)

    def extract_keys(self, dictionary, key_values):
        list_of_keys = list()
        for key in key_values:
            list_of_keys.append(key)
        return list_of_keys

    def first_row(self):
        dictionary = self.xml_data.extract_elements_data()
        keys_values = dictionary.keys()
        first_row = tuple(self.extract_keys(dictionary, keys_values))
        return first_row

    def table_data(self):
        raw_data = self.xml_data.extract_elements_data().values()
        formatted_data = list()
        for data in raw_data:
            formatted_data.append(data)
        return formatted_data

    def merge_data(self):
        table_data = self.table_data()
        first_row = self.first_row()
        table_data.insert(0, first_row)
        return table_data

    def generate_table(self):

        first_row = self.first_row()
        table_data = self.table_data()
        table_header = dict(values=first_row)
        table_cells = dict(values=table_data)
        table = plotly_graph.Table(header=table_header, cells=table_cells)
        figure = plotly_graph.Figure(data=[table])
        if not os.path.exists("images"):
            os.mkdir("images")
        figure.write_image("images/fig1.png")


table = TableGenerator("test/dummy.xml")
# print(table.set_first_row())
print(table.table_data())
table.generate_table()

#!/usr/bin/python3
"""
This is the task_03_xml module
Contains: serialize_to_xml function and deserialize_from_xml function
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename, root_tag="data"):
    """
    serialize_to_xml function
    Parameters: python dict to serialize, filename to save it to
    """
    root = ET.Element(root_tag)

    def build_xml_tree(parent, d):
        for key, value in d.items():
            child = ET.SubElement(parent, key)
            if isinstance(value, dict):
                build_xml_tree(child, value)
            else:
                child.text = str(value)

    build_xml_tree(root, dictionary)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except IOError:
        return None


def deserialize_from_xml(filename):
    """
    deserialize_from_xml function
    Parameters: filename to read the XML data from
    Return: deserialized Pythn dict
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = deserialize_from_xml(ET.tostring(child))
    return result

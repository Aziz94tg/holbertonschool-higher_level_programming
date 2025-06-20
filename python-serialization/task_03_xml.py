import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        pass

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return

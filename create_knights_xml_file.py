import lxml.etree as et

FILE_PATH = "DATA/knights.txt"

root_element = et.Element("knights")
with open(FILE_PATH) as knights_in:
    for row in knights_in:
        name, title, color, quest, comment = row.rstrip().split(':')
        knight_element = et.SubElement(root_element, "knight", title=title)
        name_element = et.SubElement(knight_element, "name")
        name_element.text = name
        et.SubElement(knight_element, "color").text = color
        et.SubElement(knight_element, "quest").text = quest
        et.SubElement(knight_element, "comment").text = comment


# create UTF-8 encoded doc string (bytes object)
encoded_doc = et.tostring(root_element, pretty_print=True)
knights_doc = encoded_doc.decode()
print(knights_doc)

tree = et.ElementTree(root_element)
tree.write("knights.xml", pretty_print=True, xml_declaration=True)

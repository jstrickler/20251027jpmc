import lxml.etree as et

FILE_PATH = "DATA/solar.xml"

tree = et.parse(FILE_PATH)
print(tree)
# root_element = tree.getroot()
# print(root_element)
print()

#  tree.findall(...) same as tree.getroot().findall()

for planet_element in tree.findall(".//planet"):
    print(planet_element.get('planetname'))  # retrieves tag element
    for moon_element in planet_element.findall('moon'):
        print(f"    {moon_element.text}")

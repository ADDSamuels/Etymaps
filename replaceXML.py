##Copyright ©2024 Alexander Samuels##
#File reduces the size of the wikidata.xml file, by only including and converts it into a new xml file
import xml.etree.ElementTree as ElementTree
lineCount=0
page = []
with open(r"xml//wikidata.xml", 'r', encoding='utf-8') as file:
    with open(r"xml//text.txt", 'w', encoding='utf-8') as file2:
        for line in file:
            lineCount += 1
            if "<page>" in line:
                page = []
                page.append(line)
            elif "</page>" in line:
                page.append(line)
                page = '\n'.join(page)
                tree = ElementTree.fromstring(page)
                nameSpace = tree.find('ns')
                if (nameSpace.text) == '0': #e.g if the namespace is only an article
                    file2.write(page)
            else:
                page.append(line)
            if lineCount % 1000000 == 0: #periodically print a message (every 1000000 lines ), for the user to see the progress of convertings
                print(str(lineCount) + "\t" + str(round( (lineCount / 100000) / 3294 * 100)) + str("%"))

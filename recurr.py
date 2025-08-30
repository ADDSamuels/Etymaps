import re
import heapq
 
# Function to perform the sorting using
# heaop sort
def heap_sort(a):
    heapq.heapify(a)
    result = []
    while a:
        result.append(heapq.heappop(a))
    return result
print("Code is not finished")
#import xml.etree.ElementTree as ET
webpage = []
def getLangCode(inputLang):
    try:
        canonIndex = langCanon.index(inputLang)
        if canonIndex > len(langCode): #checks if canonIndex is found in the langCode list
            return "?"
        else:
            return langCode[canonIndex]
    except:
        return "?"
def heapify(a, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[i] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        b[i], b[largest] = b[largest] , b[i]
        a,b = heapify(a, n, largest)
    return a, b


def heapSort(a, b):
    n = len(a)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(a, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        a[i], a[0] = a[0], a[i]
        b[i], b[0] = b[0], b[i]
        # Heapify root element
        a, b = heapify(a, i, 0)
    return a,b
def importLangData():
    global langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars
    langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars=([] for i in range(12))
    with open(r'lang.txt', 'r', encoding = "utf8") as langFile:
        lineI = -1
        for langLine in langFile:
            langLine = langLine.strip().split(";")
            if lineI >= 0:
                langList = []
                lineJ = -1
                for langElement in langLine:
                    if lineJ >= 0:
                        langList.append(langElement)
                    lineJ += 1
                if len(langList) == 12:
                    langCode.append(langList[0])
                    langCanon.append(langList[1])
                    #langCategory.append(langList[2])
                    #langType.append(langList[3])
                    #langFamilycode.append(langList[4])
                    #langFamily.append(langList[5])
                    #langSortkey.append(langList[6])
                    #langAutodetect.append(langList[7])
                    #langExceptional.append(langList[8])
                    #langScriptCodes.append(langList[9])
                    #langAltName.append(langList[10])#also known as 'other names'
                    #langStandardChars.append(langList[11])
                    #don't need all lists so I am deleting some to help memory.
            lineI += 1
def search(term,langCode):
    page = []
    for line in lines:
        if "<ti>" in line:
            title = line#.replace("</ti>", "").replace("<ti>", "")
        else:
            temp = langCode + "|" + term 
            temp1 = temp + "<"
            temp2 = temp + "|"

            if temp in line:
                if temp1 in line or temp2 in line:
                    page.append(f"{title.strip()}:\t{line.strip()}\n")
                    #line.find(temp1) != -1 or line.find(temp2) != -1:
    print("now making file")
    with open(rf"re/{term}.txt", 'w', encoding = 'utf8') as file:
        for line in page:
            file.write(line)
def removeEquals(line):
    if line.find("=") != -1:
        line = re.sub(r"\|[^|]*=[^|]*\|", "|", line)
        if line.find("=") != -1:
            line = re.sub(r"\>[^>]*=[^|]*\|", ">", line)
            if line.find("=") != -1:
                line = re.sub(r"\|[^|]*=[^<]*\<", "<", line)
    return line
print("please wait for file to be loaded")
simpleTags = ["in", "de", "bo", "d?", "ca", "sl", "lbo", "slb", "ubo"]
only1Lang = ["ds", "cg", "ncg", "m", "unk", "unc", "rfe"] #mention (m) may also have 2 language tags
#unknown and uncertain sometimes don't havebar
#simpleTagNoEquals = 
affixes = ["af", "cf", "sf", "cp", "be", "cl", "apo" ,"aph" ,"cau" ,"acr"]
ofForms = ["a", "i", "n", "par", "-pinf", "vf", "abr", "abn", "acr", "act", "agn", 
            "akk", "alc", "al", "alp", "alr", "als", "alg", "aph", "apo", "arc", 
            "ari", "ars", "asm", "ahv", "att", "aug", "bf", "ca", "csp", "clp",
            "cmf", "com", "cti", "ctr", "cnv", "da", "ds", "dsp", "dsi", "dim",
            "ec", "eg", "ell", "elo", "edm", "edf", "euf", "ey", "fq", "f", "fp", 
            "f3p", "fs", "fsp", "fn", "frq", "g", "h-", "hm", "hv", "hf", "ho", "im", 
            "if", "is", "int", "ite", "i1", "i3", "le", "li", "mn", "m", "mp", "m3p",
            "med", "msf", "msc", "msr", "msp", "mm", "mo", "na", "ng", "nq", "np",
            "nes", "n2p", "nsf", "nm", "nsf", "nsp", "nqf", "ny-", "ob", "os", "ot", 
            "par", "pss", "pst", "pej", "prf", "p", "prp", "ps", "pp", "pf", "psa", 
            "ptl", "ptn", "rf", "rs", "ref", "rel", "rff", "ro", "ru", "sc", "sh",
            "si", "sl", "so", "sp", "sf", "ss", "sum", "sup", "sus", "syf", "syn",
            "ti", "to", "ucf", "ucs", "v", "wfa"]
i = 0
ofForms = ["of" + form for form in ofForms]
print(ofForms)
bigList = simpleTags.copy() + only1Lang.copy() + affixes.copy() + ofForms.copy()
bigListTags = ["<" + tag + ">" for tag in bigList]
print(bigListTags)
lines = []
content = []
contentI = []
with open(r'xml//translate.txt', 'r', encoding = 'utf8') as file:
    j = len(bigListTags) - 1
    lineCount = 0
    jList = [len(simpleTags), len(only1Lang), len(affixes), len(ofForms)]
    for line in file:
        i = 0
        lines.append(line)
        while not bigListTags[i] in line and i != j:
            i += 1
            if bigListTags[i] in line:
                #line = removeEquals(line)
                if bigList[i] in simpleTags:
                    line = removeEquals(line) # should delete soon
                    line = line.replace("||", "|")
                    line = line.replace("|-|", "|")
                    if line.find("|") != -1:
                        line = line[len(bigListTags[i]): - len(bigListTags[i]) - 2]
                        if line.count("|") > 2:
                            line2 = line.split("|",3)
                            line = line2[0] + "|" + line2[1] + "|" + line2[2]
                        if line.count("|") == 2:
                            content.append(line)
                            contentI.append(i)
                elif bigList[i] in only1Lang:
                    pass
                pass
        if lineCount % 100000 == 0:
            print(str(round((100 * lineCount) / 53673390, 2)) + str("%"))
        
        lineCount += 1
print("now sorting")
content,contentI = heapSort(content,contentI)
print(content)
print(len(content))
with open('content.txt', 'w', encoding = "utf-8") as file2:
     for fileLine in content:
         file2.write(f"{fileLine}\n")
with open('contentI.txt', 'w', encoding = "utf-8") as file2:
     for fileLine in contentI:
         file2.write(f"{fileLine}\n")
        

with open(r'xml//translate.txt', 'r', encoding = 'utf8') as file:
    lines = file.read().splitlines()
print("file loaded")
importLangData()

while True:
    term = input("Input your word:\t")
    language = input("Input your Language:\t")
    language =language[0].upper() + language[1:].strip()
    langCode = getLangCode(language)
    print(language)
    print(langCode)
    if langCode == "?":
        print("Please input your language code again")
    else:
        search(term, langCode)



# lowerAlphabet = "abcabcdefghijklmnopqrstuvwxyz"

# def convertToFileName(text):
#     textMem = ""
#     for char in text:
#         if char in lowerAlphabet:
#             textMem = textMem + char + "_"
#         else:
#             textMem = textMem + str(ord(char)) + "_"
#     return textMem
# def convertFromFileName(text):
#     if text.find("_") == -1:
#         raise Exception("convertFromFileNameError")
#     else:
#         if text[-1]!="_":
#             raise Exception("convertFromFileNameError")
#         else:
#             textMem = ""
#             textMem2 = ""
#             char = ""
#             for i in range(0,len(text)):
#                 char = text[i]
#                 if char != "_":
#                     textMem2 = textMem2 + char    
#                 else:
#                     if textMem2 in lowerAlphabet:
#                         textMem = textMem + textMem2    
#                     else:
#                         textMem = textMem + chr(int(textMem2))
#                     textMem2 = ""
#             return textMem

# fileName = convertToFileName(title)
# #if length of fileName is greater than 250, insert a placeholder
# if len(fileName) > 250:
#     with open(rf'badFileNames.txt', 'a', encoding = "utf-8") as file2:
#         file2.write(f"{title}<{badFileNames}\n")
#     fileName = str(badFileNames)
#     badFileNames += 1
#     with open(rf'badFileNames//{fileName}.txt', 'w', encoding = "utf-8") as file2:
#         for fileLine in newPage:
#             file2.write(f"{fileLine}\n")
# fileName
# with open(rf'data////{fileName}.txt', 'w', encoding = "utf-8") as file2:
#     for fileLine in newPage:
#         file2.write(f"{fileLine}\n")
# entryCount += 1

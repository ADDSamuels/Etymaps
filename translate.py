###Copyright ©2024 Alexander Samuels###
import xml.etree.ElementTree as ElementTree
import re
import unicodedata

#getLangCode returns the language code, used in heading names. For Example English --> en
def getLangCode(inputLang):
    try:
        canonIndex = langCanon.index(inputLang)
        if canonIndex > len(langCode): #checks if canonIndex is found in the langCode list
            return "?" 
        else:
            return langCode[canonIndex]
    except:
        return "?"
#initialise a new page, I use global variables, and then iterate on line breaks to print
def initnewPage():
    global newPage
    global newPointer
    titletag = "<ti>" + title + "</ti>"
    newPage = ["<pa>", titletag, "</pa>"]
    newPointer = 2
#such quotes are used in highlighting but I removed them   
def replaceQuotes(line):
    line = line.replace("'''", "")
    line = line.replace("''", "")
    return line
#adds tag and the line minus the tag to the newPage variable,
def addToPage(tag, lineMinusTag):
    global newPointer, newPage
    subtag1 = "<" + tag + ">"
    subtag2 = "</" + tag + ">"
    if len(lineMinusTag) > 0:
        insert = subtag1 + lineMinusTag + subtag2
    else:
        insert = subtag1 + subtag2
    newPage.insert(newPointer, insert)
    newPointer += 1
#remove tag from line (content) before addToPage() is called
def removeTag(tag, line):
    if line.count("|") > 1:
        line = line.split("|", 1)[1]
    lineMinusTag = line.replace("{{", "").replace("}}", "")
    addToPage(tag, lineMinusTag)
#splits line variable based on the  
def lineCut(line, char, lineSide):
    if line[0].find(char) != -1:
        if lineSide == 1:
            lineMem = line[0][:line[0].find(char)]
        else:
            lineMem = line[0][line[0].find(char)+2:]
        if len(lineMem) > 0: 
            if lineSide == 1:#eg, {{,[[
                line.insert(1, (line[0])[line[0].find(char):])
                line[0]=(line[0])[:line[0].find(char)]
            elif lineSide == 2:#eg, }} , ]]
                line.insert(1, (line[0])[line[0].find(char) + 2:])
                line[0]=(line[0])[:line[0].find(char) + 2]
        return line.copy()
    else:
        return line.copy()
def getTag(line):
    if line.find("|") >= 0:
        return line[2:].split("|", 1)[0],True
    return line[:2].replace("}}","").replace("]]",""),False
def ofForm(tag, line):
    if tag == "adj form of": #pos improve template, with more adjectives
        removeTag("ofa", line)
    elif tag == "inflection of" or tag == "infl of":
        removeTag("ofi", line)
    elif tag == "noun form of":
        removeTag("ofn", line)
    elif tag == "participle of":
        removeTag("ofpar", line)
    elif tag == "pi-nr-inflection of":
        removeTag("of-pinf", line)
    elif tag == "verb form of":
        removeTag("ofvf", line)
    elif tag == "abbreviation of" or tag == "abbr of" or tag == "abbrev of":
        removeTag("ofabr", line)
    elif tag == "abstract noun of":
        removeTag("ofabn", line)
    elif tag == "acronym of":
        removeTag("ofacr", line)
    elif tag == "active participle of":
        removeTag("ofacr", line)
    elif tag == "agent noun of":
        removeTag("ofagn", line)
    elif tag == "akkadogram of":
        removeTag("ofakk", line)
    elif tag == "alternative case form of" or tag == "alt case form of" or tag == "alt case form" or tag == "alt case of" or tag == "alt case" or tag == "altcase":
        removeTag("ofalc", line)
    elif tag == "alternative form of" or tag == "altform" or tag == "alt form" or tag == "alt form of":
        removeTag("ofal", line)
    elif tag == "alternative plural of":
        removeTag("ofalp", line)
    elif tag == "alternative reconstruction of":
        removeTag("ofalr", line)
    elif tag == "alternative spelling of" or tag == "alt sp" or tag == "alt sp of":
        removeTag("ofals", line)
    elif tag == "alternative typography of" or tag == "alt typ":
        removeTag("ofalg", line)
    elif tag == "aphetic form of":
        removeTag("ofaph", line)
    elif tag == "apocopic form of" or tag == "apoc of":
        removeTag("ofapo", line)
    elif tag == "archaic form of":
        removeTag("ofarf", line)
    elif tag == "archaic inflection of":
        removeTag("ofari", line)
    elif tag == "archaic spelling of" or tag == "archaic sp":
        removeTag("ofars", line)
    elif tag == "aspirate mutation of":
        removeTag("ofasm", line)
    elif tag == "assimilated harmonic variant of":
        removeTag("ofahv", line)
    elif tag == "attributive form of":
        removeTag("ofatt", line)
    elif tag == "augmentative of":
        removeTag("ofaug", line)
    elif tag == "broad form of":
        removeTag("ofbf", line)
    elif tag == "causative of":
        removeTag("ofca", line)
    elif tag == "censored spelling of" or tag == "cens sp":
        removeTag("ofcsp", line)
    elif tag == "clipping of" or tag == "clip of":
        removeTag("ofclp", line)
    elif tag == "combining form of" or tag == "com form":
        removeTag("ofcmf", line)
    elif tag == "comparative of":
        removeTag("ofcom", line)
    elif tag == "continuative of":
        removeTag("ofcti", line)
    elif tag == "contraction of" or tag == "contr of":
        removeTag("ofctr", line)
    elif tag == "conversion of":
        removeTag("ofcnv", line)
    elif tag == "dated form of" or tag == "dated form":
        removeTag("ofda", line)
    elif tag == "dated spelling of" or tag == "dated sp":
        removeTag("ofds", line)
    elif tag == "deliberate misspelling of":
        removeTag("ofdsp", line)
    elif tag == "desiderative of":
        removeTag("ofdsi", line)
    elif tag == "diminutive of" or tag == "dim of":
        removeTag("ofdim", line)
    elif tag == "eclipsis of":
        removeTag("ofec", line)
    elif tag == "eggcorn of":
        removeTag("ofeg", line)
    elif tag == "ellipsis of":
        removeTag("ofell", line)
    elif tag == "elongated form of":
        removeTag("ofelo", line)
    elif tag == "endearing diminutive of":
        removeTag("ofedm", line)
    elif tag == "endearing form of":
        removeTag("ofedf", line)
    elif tag == "euphemistic form of" or tag == "euph form":
        removeTag("ofeuf", line)
    elif tag == "eye dialect of":
        removeTag("ofey", line)
    elif tag == "female equivalent of" or tag == "femeq":
        removeTag("offq", line)
    elif tag == "feminine of":
        removeTag("off", line)
    elif tag == "feminine plural of":
        removeTag("offp", line)
    elif tag == "feminine plural past participle of":
        removeTag("off3p", line)
    elif tag == "feminine singular of":
        removeTag("offs", line)
    elif tag == "feminine singular past participle of":
        removeTag("offsp", line)
    elif tag == "former name of":
        removeTag("offn", line)
    elif tag == "frequentative of":
        removeTag("offrq", line)
    elif tag == "gerund of":
        removeTag("ofg", line)
    elif tag == "h-prothesis of":
        removeTag("ofh-", line)
    elif tag == "hard mutation of":
        removeTag("ofhm", line)
    elif tag == "harmonic variant of":
        removeTag("ofhv", line)
    elif tag == "hiatus-filler form of" or tag == "hf form":
        removeTag("ofhf", line)
    elif tag == "honorific alternative case form of" or tag == "honor alt case" or tag == "honour alt case":
        removeTag("ofho", line)
    elif tag == "imperfective form of":
        removeTag("ofim", line)
    elif tag == "informal form of":
        removeTag("ofif", line)
    elif tag == "informal spelling of":
        removeTag("ofis", line)
    elif tag == "initialism of" or tag == "init of":
        removeTag("ofint", line)
    elif tag == "iterative of":
        removeTag("ofite", line)
    elif tag == "IUPAC-1":
        removeTag("ofi1", line)
    elif tag == "IUPAC-3":
        removeTag("ofi3", line)
    elif tag == "lenition of":
        removeTag("ofle", line)
    elif tag == "literary form of":
        removeTag("ofli", line)
    elif tag == "masculine noun of":
        removeTag("ofmn", line)
    elif tag == "masculine of":
        removeTag("ofm", line)
    elif tag == "masculine plural of":
        removeTag("ofmp", line)
    elif tag == "masculine plural past participle of":
        removeTag("ofm3p", line)
    elif tag == "medieval spelling of":
        removeTag("ofmed", line)
    elif tag == "men's speech form of":
        removeTag("ofmsf", line)
    elif tag == "misconstruction of":
        removeTag("ofmsc", line)
    elif tag == "misromanization":
        removeTag("ofmsr", line)
    elif tag == "misspelling of" or tag == "missp":
        removeTag("ofmsp", line)
    elif tag == "mixed mutation of":
        removeTag("ofmm", line)
    elif tag == "momentane of":
        removeTag("ofmo", line)
    elif tag == "nasal mutation of":
        removeTag("ofna", line)
    elif tag == "negative of":
        removeTag("ofng", line)
    elif tag == "neuter equivalent of" or tag == "neuteq":
        removeTag("ofnq", line)
    elif tag == "neuter plural of":
        removeTag("ofnp", line)
    elif tag == "neuter singular of":
        removeTag("ofnes", line)
    elif tag == "neuter singular past participle of":
        removeTag("ofn2p", line)
    elif tag == "nomen sacrum form of":
        removeTag("ofnsf", line)
    elif tag == "nominalization of" or tag == "nom of":
        removeTag("ofnm", line)
    elif tag == "nonstandard form of" or tag == "nonstandard form" or tag == "nonst form" or tag == "ns form":
        removeTag("ofnsf", line)
    elif tag == "nonstandard spelling of" or tag == "nonst sp" or tag == "ns sp":
        removeTag("ofnsp", line)
    elif tag == "nuqtaless form of":
        removeTag("ofnqf", line)
    elif tag == "ny-obs in Malawi":
        removeTag("ofny-", line)
    elif tag == "obsolete form of" or tag == "obs form":
        removeTag("ofof", line)
    elif tag == "obsolete spelling of" or tag == "obs sp":
        removeTag("ofos", line)
    elif tag == "obsolete typography of" or tag == "obs typ":
        removeTag("ofot", line)
    elif tag == "paragogic form of":
        removeTag("ofpar", line)
    elif tag == "passive participle of":
        removeTag("ofpss", line)
    elif tag == "past participle of":
        removeTag("ofpst", line)
    elif tag == "pejorative of":
        removeTag("ofpej", line)
    elif tag == "perfective form of":
        removeTag("ofprf", line)
    elif tag == "plural of":
        removeTag("ofp", line)
    elif tag == "present participle of":
        removeTag("ofprp", line)
    elif tag == "pronunciation spelling of" or tag == "pron spelling of" or tag == "pron sp of" or tag == "pron sp":
        removeTag("ofps", line)
    elif tag == "pronunciation variant of":
        removeTag("ofpp", line)
    elif tag == "prothetic form of":
        removeTag("ofpf", line)
    elif tag == "pseudo-acronym of":
        removeTag("ofps", line)
    elif tag == "pt-pronoun-with-l":
        removeTag("ofptl", line)
    elif tag == "pt-pronoun-with-n":
        removeTag("ofptn", line)
    elif tag == "rare form of":
        removeTag("ofrf", line)
    elif tag == "rare spelling of" or tag == "rare sp":
        removeTag("ofrs", line)
    elif tag == "reflexive of":
        removeTag("ofref", line)
    elif tag == "relational adjective of" or tag == "rel adj of" or tag == "rel adj":
        removeTag("ofrel", line)
    elif tag == "rfform":
        removeTag("ofrff", line)
    elif tag == "romanization of":
        removeTag("ofro", line)
    elif tag == "runic spelling of":
        removeTag("ofru", line)
    elif tag == "scribal abbreviation of" or tag == "scrib of" or tag == "scrib abbr of" or tag == "scrib abbrev of" or tag == "scribal abbr of" or tag == "scribal abbrev of":
        removeTag("ofsc", line)
    elif tag == "short for":
        removeTag("ofsh", line)
    elif tag == "singular of":
        removeTag("ofsi", line)
    elif tag == "slender form of":
        removeTag("ofsl", line)
    elif tag == "soft mutation of":
        removeTag("ofso", line)
    elif tag == "spelling of":
        removeTag("ofsp", line)
    elif tag == "standard form of":
        removeTag("ofsf", line)
    elif tag == "standard spelling of" or tag == "stand sp":
        removeTag("ofss", line)
    elif tag == "sumerogram of":
        removeTag("ofsum", line)
    elif tag == "superlative of":
        removeTag("ofsup", line)
    elif tag == "superseded spelling of":
        removeTag("ofsus", line)
    elif tag == "syncopic form of":
        removeTag("ofsyf", line)
    elif tag == "synonym of" or tag == "syn of":
        removeTag("ofsyn", line)
    elif tag == "t-prothesis of":
        removeTag("oft-pr", line)
    elif tag == "Tifinagh spelling of":
        removeTag("ofti", line)
    elif tag == "topicalized form of":
        removeTag("ofto", line)
    elif tag == "uncommon form of" or tag == "uncommon form":
        removeTag("ofucf", line)
    elif tag == "uncommon spelling of" or tag == "uncommon sp":
        removeTag("ofucs", line)
    elif tag == "verbal noun of":
        removeTag("ofv", line)
    elif tag == "word-final anusvara form of":
        removeTag("ofwfa", line)
    elif tag.find("form of") > 0:
        line = currentLangCode + "|" + line.replace("{{","").replace("}}", "")
        addToPage("x", line)#form is very common so reduces space with just a <x> tag

#Check if text has cryillic characters
def hasCryillic(text):
    return bool(re.search('[\u0400-\u04FF]', text)) 

#removes certain diacritics
def removeDiacritics(text):
    return ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
def makeEntryName(text):
    text = re.sub(r'[aeɛioɵuʉt̪s̪]+[\u0300-\u036F]*', lambda match: removeDiacritics(match.group()), text)
    return text

def etymTag(tag, line, hasBar):
    if hasBar:
        if tag == "inh" or tag == "inherited" or tag == "inh" or tag == "inh-lite":#included template inh+, inh-lite
            removeTag("in", line)
        elif tag == "borrowed" or tag == "bor" or tag == "bor+":#included template bor+
            removeTag("bo", line)
        elif tag == "derived" or tag == "der" or tag == "der+" or tag == "der-lite":#included template der+, der-lite
            removeTag("de", line)
        elif tag == "undefined derivation" or tag == "uder" or tag == "der?":
            removeTag("d?", line)
        elif tag == "calque" or tag == "cal" or tag == "clq":
            removeTag("ca", line)
        elif tag == "semantic loan" or tag == "sl":
            removeTag("sl", line)
        elif tag == "partial calque" or tag == "pcal" or tag == "pclq":
            removeTag("pc", line)
        elif tag == "descendant" or tag == "desc":
            removeTag("ds", line)
        elif tag == "descendat tree" or tag == "desctree":
            removeTag("dt", line)
        elif tag == "cognate" or tag == "cog":
            removeTag("cg", line)
        elif tag == "noncognate" or tag == "noncog" or tag == "ncog" or tag == "nc":
            removeTag("ncg", line)
        elif tag == "learned borrowing" or tag == "lbor":
            removeTag("lbo", line)
        elif tag == "orthographic borrowing" or tag == "obor":
            removeTag("obo", line)
        elif tag == "semi-learned borrowing" or tag == "slbor":
            removeTag("slb", line)
        elif tag == "unadapted borrowing" or tag == "ubor":
            removeTag("ubo", line)
        elif tag == "mention" or tag == "m" or tag == "langname-mention" or tag == "m+":# included template m+
            removeTag("m", line)
        elif tag == "affix" or tag == "af":
            removeTag("af", line)
        elif tag == "prefix" or tag == "pre":
            removeTag("pf", line)
        elif tag == "confix" or tag == "con":
            removeTag("cf", line)
        elif tag == "suffix" or tag == "suf":
            removeTag("sf", line)
        elif tag == "compound" or tag == "cp":
            removeTag("cp", line)
        elif tag == "blend":
            removeTag("be", line)
        elif tag == "clipping":
            removeTag("cl", line)
        elif tag == "short for":
            removeTag("sh4", line)
        elif tag == "back-form" or tag == "bf" or tag == "back-formation":
            removeTag("bf", line)
        elif tag == "doublet" or tag == "dbt":
            removeTag("2l", line)
        elif tag == "onomatopoeic" or tag == "onom":
            removeTag("on", line)
        elif tag == "unk" or tag == "unknown":
            removeTag("unk", line)
        elif tag == "unc" or tag == "uncertain":
            removeTag("unc", line)
        elif tag == "rfe":
            removeTag("rfe", line)
        elif tag == "etystub":
            removeTag("ets", line)
        elif tag == "apocopic form":
            removeTag("apo", line)
        elif tag == "aphetic form":
            removeTag("aph", line)
        elif tag == "causative":
            removeTag("cau", line)
        



            ## add tag==acronomyn
def inputData(cutLines,caseN):
    i=0
    global newPage
    global newPointer
    global currentLangCode
    currentLangCode = ""
    #Set
    if len(headingList) > 0:
        currentLang = headingList[0]
        currentLangCode = getLangCode(currentLang)
        #print(currentLang + currentLangCode)
    newPointerMem = 0
    newPointerMem2 = 0
    
    #If there are multiple etymologies add tags around them
    if caseN==3:
        if (headingList[-1])[:9] == "Etymology":
            if len(headingList[-1]) > 9:
                newPointerMem = 1
                subtag1 = "<e" + headingList[-1][11:] + ">"
                subtag2 = "</e" + headingList[-1][11:] + ">"
                newPage.insert(newPointer, subtag1)
                newPointer += 1
                newPage.insert(newPointer, subtag2)
    
    for line in cutLines:
        line=re.sub(u'[\u064e\u064f\u0650\u0651\u0652\u064c\u064b\u064d\u0640\ufc62]', '', line)
        if currentLangCode=="grk-mar":
            if hasCryillic(line):
                re.sub(u'[\u0301]', '', line)
        elif currentLangCode=="zlw=slv":
            line=makeEntryName(line)
        else:
            replacements = [chr(0x303), chr(0x304), chr(0x307), chr(0x308), chr(0x323), chr(0x32E), chr(0x330), chr(0x331), chr(0x711), "[" + chr(0x730) + "-" + chr(0x74A) + "]"]
            for replacement in replacements:
                line = re.sub(replacement, "", line)
        tag=""
        if line.find("{{") == -1 and line.find("[[") == -1:
            if caseN!=0:
                if caseN == 3 and "Etymology" == headingList[-1]:
                    pass
                else:
                    pass#print(headingList[-1])
        elif line[:2] == "{{":
            tag, hasBar = getTag(line)
            if tag == "also" and hasBar:
                if line.find("|sc=") >= 0 or line.find("|uni=") >= 0 or line.find("|uniN=") >= 0 or line.find("|scN=") >= 0:
                    print(f"@also={line}")
                else:
                    addToPage("a", line.replace("}}","").replace("{{","")[5:])#need to add parser for appendix
            elif caseN==3:

                if "Etymology" == (headingList[-1])[:9]:
                    etymTag(tag,line,hasBar)
                elif "Alternative forms" == headingList[-1]:
                    if tag == "l" or tag == "l-self" or tag == "link" or tag == "ll":
                        removeTag("al", line)
                else:#nouns etc
                    if tag == "form of":
                        pass#get tag
                        removeTag("ofj", line)
                    elif tag == "lb":
                        pass#dp stuff
                    else:
                        line=line#only get |1= and |2= for line, ignore rest
                        ofForm(tag, line)
                        
                #pass#Etymology
            elif caseN==4:
                line=re.sub(r'\|sort=.+?\|', '|', line)
                line=re.sub(r'\|title=.+?\|', '|', line)
                line=re.sub(r'\|sc=.+?\|', '|', line)
                line=re.sub(r'\|collapse=.+?\|', '|', line)
                if "Derived terms" == headingList[-1]:
                    if tag[:3] == "col" or tag[:3] == "der":
                        cutLines = line.split('|')
                        clLang = cutLines[1].replace("{{", "").replace("}}", "")
                        clI = 0
                        for cutLine in cutLines:
                            if clI == 1:
                                cutLine = re.sub(r'[{{].+[}}].', '', cutLine).replace(r"/", "")
                                cutLine = re.sub(r'\].+\[', '|', cutLine)
                                cutLine = cutLine.replace("[", "").replace("]", "").replace("{{", "").replace("}}", "")
                                cutLine = [cutLine.split("|")]
                                clJ = 0
                                for cutLine2 in cutLine:
                                    if len(cutLine2[clJ])>0:
                                        clmem = "{{d|" + clLang + "|"+ cutLine2[clJ] + "}}"
                                        removeTag("d", clmem)
                                    clJ += 1
                            clI=1
                    elif tag == "l":
                        removeTag("d", line)
                #elif ":
                elif "Descendants" == headingList[-1]:
                    if tag == "desc" or tag == "descendant":
                        line = re.sub(r'\|bor=.+?\|', '|', line)
                        line = line.split("|")
                        if len(line) >= 3:
                            clmem = line[0] + "|" + line[1] + "|" + line[2] + "}}"
                            removeTag("v", clmem)
                elif "Translations" == headingList[-1]:
                    if tag == "t" or tag == "t+" or tag == "tt" or tag == "tt+":
                        line = re.sub(r'\|sc=.+?\|', '|', line)
                        line = re.sub(r'\|alt=.+?\|', '|', line)
                        line = re.sub(r'\|lit=.+?\|', '|', line)
                        line = re.sub(r'\|id=.+?\|', '|', line)
                        #keeping translations (tr=...)
                        line = line.split("|")
                        if len(line) == 3:
                            transMem = "{{t|" + line[1] + "|" + line[2]
                        elif len(line) >= 4:
                            transMem = "{{t|" + line[1] + "|" + line[2] + "|" + line[3]
                        removeTag("t", transMem)
                        
                    elif tag == "trans-top":
                        line = re.sub(r'\|id=.+?\|', '|', line)
                        line = re.sub(r'\|column-width=.+?\|', '|', line)
                        line = line.replace("}}", "").split("|")
                        if len(line) >= 2:
                            newPointerMem2 = 1
                            transMem = line[0] + "|" + line[1]
                            subtag1 = "<tr><trti>" + line[1] + r"</trti>"
                            subtag2 = "</tr>"
                            newPage.insert(newPointer, subtag1)
                            newPointer += 1
                            newPage.insert(newPointer, subtag2)
                    elif tag == "trans-bottom":
                        newPointer += newPointerMem2
                        newPointerMem2 = 0
        elif line[:2] == "[[":
            tag = getTag(line)
        else:
            print(f"ACHTUNG: Data not declined\tline={line}")
        i += 1
    newPointer += newPointerMem
def formatCase(subEntry, caseN):
    cutLines = []
    newLine = []
    mem = ""
    for line in subEntry:
        line = replaceQuotes(line)
        newLine = []
        line = [line]## I need to properly format html tags like, for example <math></math>
        while len(line)>0:
            line = lineCut(lineCut(lineCut(lineCut(line, "{{", 1), "[[", 1), "}}", 2), "]]", 2)
            newLine.append(line[0])
            line.pop(0)
        i = 0
        cutLines = cutLines.copy() + newLine.copy()
    enclosers = []
    enclosersI = []
    enclosersJ = []
    brackets=["{{", "}}", "[[", "]]"]
    i = 0
    i2 = 0
    cutLines2 = []
    for line in cutLines:
        j = 0
        oldChar = ""
        if not any(bracket in line for bracket in brackets):
            if len(enclosers) == 0:
                line = line.replace("\t", "").lower()
                cutLines2.append(line)
            else:
                mem = mem + line
        else:
            for char in line:
                sumChar = oldChar+char
                if sumChar in brackets:
                    if sumChar == "{{" or sumChar == "[[":
                        enclosers.append(sumChar)
                        enclosersI.append(i)
                        enclosersJ.append(j-1)     
                    else:
                        mem = ""
                        try:
                            for i2 in range(enclosersI[-1], i+1):
                                if i2 == enclosersI[-1]:
                                    if i2 == i:
                                        mem=(cutLines[i2])[enclosersJ[-1]:j + 1]
                                    else:
                                        mem=(cutLines[i2])[enclosersJ[-1]:]
                                elif i2 == i:
                                    mem=mem + (cutLines[i2])[:j + 1]
                                else:
                                    mem=mem + cutLines[i2]
                            enclosers.pop()
                            enclosersI.pop()
                            enclosersJ.pop()
                            cutLines2.append(mem)
                        except:
                            pass#print(f"i=({i}),i2=({i2}) ,j=({j}) \n line={line}\n cutLines={cutLines}\n enclosers={enclosers}\n enclosersI={enclosersI}\n enclosersJ={enclosersJ}") 
                oldChar=char
                j+=1
        i+=1
    inputData(cutLines2,caseN)
def loopThruPage(page):
    page2 = page.split("\n")
    page2 = list(filter(('').__ne__, page2))
    subEntry = []
    j = 0
    urequalN = 0
    mode=""
    urmode=""
    equalN2=0
    initnewPage()
    global headingList
    #Page=[]
    headingList=[]
    for line in page2:
        #print(line)
        line=re.sub(r'<.+>', '', line)
        equalN=0
        for a in range(2,7):
            if line[:a]=="======"[:a] and line[a]!="=":
                if line.count("=")==a*2:
                    urequalN=equalN2
                    equalN=a
                    equalN2=a
                    urmode=mode
                    mode=line.replace("=","")
                    #print(str(equalN)+"="+mode)
                    j+=1
        if equalN>0:
            match urequalN:
                case 0:
                    formatCase(subEntry,urequalN)
                case 1:
                    pass#skip case 1 since it's defective
                case 2:
                    headingList=[urmode]
                    formatCase(subEntry,urequalN)
                case _:
                    headingList.append(urmode)
                    formatCase(subEntry,urequalN)
            subEntry=[]

        else:
            subEntry.append(line)   
def importLangData():
    global langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars
    langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars=([] for i in range(12))
    with open(r"c://p//map//lang.txt",encoding="utf8") as langFile:
        lineI=-1
        for langLine in langFile:
            langLine=langLine.strip().split(";")
            if lineI>=0:
                lL=[]
                lineJ=-1
                for langElement in langLine:
                    if lineJ>=0:
                        lL.append(langElement)
                    lineJ+=1
                if len(lL)==12:
                    langCode.append(lL[0])
                    langCanon.append(lL[1])
                    langCategory.append(lL[2])
                    langType.append(lL[3])
                    langFamilycode.append(lL[4])
                    langFamily.append(lL[5])
                    langSortkey.append(lL[6])
                    langAutodetect.append(lL[7])
                    langExceptional.append(lL[8])
                    langScriptCodes.append(lL[9])
                    langAltName.append(lL[10])#also known as 'other names'
                    langStandardChars.append(lL[11])
            lineI+=1
newPage=[]
newPointer=""
importLangData()
print("Welcome to Etymaps Translation Program\nCopyright ©2024 Alexander Samuels")
lineI=0
webpage=[]
with open(r"C://p//map//xml//text.txt",encoding='utf8') as file:
    for line in file:
        lineI+=1
        if "<page>" in line:
            webpage = []
            webpage.append(line)
        elif "</page>" in line:
            #webpage is now finished to analyse
            webpage.append(line)
            webpage='\n'.join(webpage)
            tree = ElementTree.fromstring(webpage)
            title=(tree.find('title')).text
            revision=tree.find('revision')#returnTag(tree,"revision")
            if ((tree.find('ns')).text)=='0': #if not a special nor talk page
                #decided not to use usernames to credit users
                page=(revision.find("text")).text#returnTag(revision,"text").text #different variable name since text is too vague + converted to string so it is easier
                loopThruPage(page)
                if len(newPage)>3:
                    with open(r'c://p//Map//xml//translate.txt', 'a', encoding="utf-8") as f:
                        for fileLine in newPage:
                            f.write(f"{fileLine}\n")
        else:
            webpage.append(line)
        if lineI % 200000 == 0:
            print(str(lineI)+"\t"+str(round((100*lineI)/479268517,2))+str("%"))
            print("Title:\t\t"+title)
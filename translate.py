###Copyright ©2024 Alexander Samuels###
import xml.etree.ElementTree as ElementTree
import re
import unicodedata

#getLangCodeandScript returns the language code and also script, used in heading names. For Example English --> en, Latn
def getLangCodeAndScript(inputLang):
    try:
        canonIndex = langCanon.index(inputLang)
        if canonIndex > len(langCode): #checks if canonIndex is found in the langCode list
            return "?", ""
        else:
            return langCode[canonIndex], langScriptCodes[canonIndex]
    except:
        return "?", ""
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
#splits line variable based on the lineSide (1=Left of delimiter,2=right side of delimiter) and the delimiter
def lineCut(line, delimiter, lineSide):
    #checks if delimiter is found, if yes, cuts the line
    if line[0].find(delimiter) != -1:
        if lineSide == 1:
            lineMem = line[0][:line[0].find(delimiter)]
        else:
            lineMem = line[0][line[0].find(delimiter)+2:]
        if len(lineMem) > 0: 
            if lineSide == 1:#eg, {{,[[
                line.insert(1, (line[0])[line[0].find(delimiter):])
                line[0] = (line[0])[:line[0].find(delimiter)]
            else:#eg, }} , ]]
                line.insert(1, (line[0])[line[0].find(delimiter) + 2:])
                line[0] = (line[0])[:line[0].find(delimiter) + 2]
        return line.copy()
    else:
        return line.copy()
#returns tags; e.g {{tag|content1|content2}} would return tag and true 
def getTag(line):
    try:
        if line.find("|") >= 0:
            return line[2:].split("|", 1)[0],True
        return line[2:].replace("}}","").replace("]]",""),False
    #added of-forms in one function to make other functions more readable.
    except:
        print(f"Line:{line}")
        print(str(line[2:].replace("}}","").replace("]]",""),False))
def ofForm(tag, line):
    if tag == "adj form of": #pos improve template, with more adjectives
        removeTag("ofa", line)
    if tag == "inflection of" or tag == "infl of":
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
    elif tag.find("form of") > 0:#for alternative form of derivations, I keep them
        line = currentLangCode + "|" + line.replace("{{","").replace("}}", "")
        addToPage("x", line)#form is very common so reduces space with just a <x> tag

#removes certain diacritics only if the language is Slovincian
def removeDiacriticsFromSlovincian(text):
    return ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
#removes certain
def makeEntryNameFromSlovincian(text):
    text = re.sub(r'[aeɛioɵuʉt̪s̪]+[\u0300-\u036F]*', lambda match: removeDiacriticsFromSlovincian(match.group()), text)
    return text
#adds etymological tags in one function to make other functions more readable.
def etymTag(tag, line):
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
    elif tag == "descendant tree" or tag == "desctree":
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
    elif tag == "acronym":
        removeTag("acr", line)
#since regular expressions are computationally complex, I first check, if said tag is in the line
def regrexSub(tag, line):
    tag = "|" + tag + "="
    if tag in line:
        line = re.sub(rf"\{tag}.?\|", "|", line)
        if tag in line:
            line = re.sub(rf"\{tag}.?\}}", "}", line)
    return line
#cleans the text of characters which are not supported by the tag
def cleanTextForTags(line, currentLangCode, currentLangScript):
    #if language = Mariupol Greek, remove certain characters
    if currentLangCode == "grk-mar":
        if re.search('[\u0400-\u04FF]', line):
            re.sub(u'[\u0301]', '', line)
    # if language = Slovincian (a West-Slavic language near Słupsk, Pomerania, Poland)
    elif currentLangCode == "zlw-slv":
        line = makeEntryNameFromSlovincian(line)
    else:
        if "Arab" in currentLangScript:
            line = re.sub(u'[\u064e\u064f\u0650\u0651\u0652\u064c\u064b\u064d\u0640\ufc62]', '', line)
        if "Syrc" in currentLangScript:
            line = removeSyriacDiacritics(line)
        if "Latn" in currentLangScript:
            line = removeLatinDiacritics(line)
    return line
def processAlsoTemplate(line, hasBar):
    if hasBar:
        line = regrexSub('sc', line)
        line = regrexSub('scN', line)
        line = regrexSub('uni', line)
        line = regrexSub('uniN', line)
        addToPage("a", line.replace("}}","").replace("{{","")[5:])
#remove some unnecessary cosmetic data
#Removes specified combining diacritic characters from the text.
def removeLatinDiacritics(text):
    combiningChars = [
        '\u0303',  # Combining Tilde
        '\u0304',  # Combining Macron
        '\u0307',  # Combining Dot Above
        '\u0308',  # Combining Diaeresis
        '\u0323',  # Combining Dot Below
        '\u032E',  # Combining Breve
        '\u0330',  # Combining Tilde Below
        '\u0331'   # Combining Macron Below
    ]
    # Normalize the text to decomposed Unicode form and remove combining characters
    normalizedText = unicodedata.normalize('NFD', text)
    filteredText = ''.join(char for char in normalizedText if char not in combiningChars)
    # Line back to composed Unicode form
    return unicodedata.normalize('NFC', filteredText)
def removeSyriacDiacritics(text):
    combiningChars = [
    '\u0711', # syriac letter reversed pe
    '\u0730', # syriac small high ligature alef with lam with yeh
    '\u0731', # syriac small high zain
    '\u0732', # syriac small high seen
    '\u0733', # syriac small high sheen
    '\u0734', # syriac small high sad
    '\u0735', # syriac small high ain
    '\u0736', # syriac small high qaf
    '\u0737', # syriac small high noon with kasra
    '\u0738', # syriac small low noon with kasra
    '\u0739', # syriac small high word ar-rub
    '\u073A', # syriac small high sad with lam alef
    '\u073B', # syriac small high ain with lam alef
    '\u073C', # syriac small high qaf with lam alef
    '\u073D', # syriac small high jeem with yeh
    '\u073E', # syriac small high three dots
    '\u073F', # syriac small high seen with three dots
    '\u0740', # syriac small high sheen with three dots
    '\u0741', # syriac small high tah
    '\u0742', # syriac small high ain with three dots downwards
    '\u0743', # syriac small high alef with qamats
    '\u0744', # syriac small high kaf type 1
    '\u0745', # syriac small high lam alef
    '\u0746', # syriac small high meem
    '\u0747', # syriac small high noon
    '\u0748', # syriac small low noon
    '\u0749', # syriac small high jeem
    '\u074A'  # syriac small high three dots with downwards arrow below
]
    # Normalize the text to decomposed Unicode form and remove combining characters
    normalizedText = unicodedata.normalize('NFD', text)
    filteredText = ''.join(char for char in normalizedText if char not in combiningChars)
    # Line back to composed Unicode form
    return unicodedata.normalize('NFC', filteredText)
def regrexLine(line):
    line = regrexSub('title', line)
    line = regrexSub('sc', line)
    line = regrexSub('collapse', line)
    line = regrexSub('sort', line)
    return line
def processDefinitionTemplates(line, tag, hasBar):
    if hasBar:
        #if etymology then use the function
        if "Etymology" == (headingList[-1])[:9]:
            etymTag(tag, line)
        elif "Alternative forms" == headingList[-1]:
            if tag == "l" or tag == "l-self" or tag == "link" or tag == "ll":
                removeTag("al", line)
        else:#nouns etc
            if tag == "form of":
                removeTag("ofj", line)
            elif tag == "lb":
                pass
            else:
                line=line#only get |1= and |2= for line, ignore rest
                ofForm(tag, line)
def processDerivedTerms(line, tag):
    if (tag[:3] == "col" or tag[:3] == "der") and tag[:7]!="der-top" and tag[:10]!="der-bottom" and tag[:10]!="col-bottom" and tag[:7]!="col-top":
        cutLines = line.split('|')
        try:
            cutLineLang = cutLines[1].replace("{{", "").replace("}}", "")
            cutLineI = 0
            for cutLine in cutLines:
                if cutLineI == 1:
                    if "{" in cutLine:
                        cutLine = re.sub(r'[{{].+[}}].', '', cutLine).replace(r"/", "")
                    cutLine = re.sub(r'\].+\[', '|', cutLine)
                    cutLine = cutLine.replace("[", "").replace("]", "").replace("{{", "").replace("}}", "")
                    cutLineList = [cutLine.split("|")]
                    cutLineJ = 0
                    for cutLine2 in cutLineList:
                        if len(cutLine2[cutLineJ]) > 0:
                            clmem = "{{d|" + cutLineLang + "|"+ cutLine2[cutLineJ] + "}}"
                            removeTag("d", clmem)
                        cutLineJ += 1
                cutLineI=1
        except:
            print(f"cutLines:{cutLines}")
    elif tag == "l":
        removeTag("d", line)
def processDescendantTerms(line, tag):
    if tag == "desc" or tag == "descendant":
        line = regrexSub('bor', line)
        line = line.split("|")
        if len(line) >= 3:
            clmem = line[0] + "|" + line[1] + "|" + line[2] + "}}"
            removeTag("v", clmem)
def processTranslations(line, tag, transPointerMem):
    #a normal translation
    global newPointer
    global newPage
    transMem = ""
    if tag == "t" or tag == "t+" or tag == "tt" or tag == "tt+":
        line = regrexSub('alt', line)
        line = regrexSub('lit', line)
        line = regrexSub('id', line)
        #note that here I delete certain data for translation but keep transliterations (tr=), 
        #since I will be using them
        line = line.split("|")
        if len(line) == 3:
            transMem = "{{t|" + line[1] + "|" + line[2]
        elif len(line) >= 4:
            transMem = "{{t|" + line[1] + "|" + line[2] + "|" + line[3]#removes extra data which could be hiding in the folder
        removeTag("t", transMem)
    #at the very beginning of a translation    
    elif tag == "trans-top":
        line = regrexSub('id', line)
        line = regrexSub('column-width', line)
        line = line.replace("}}", "").split("|")
        if len(line) >= 2:
            addTagToPage("<tr><trti>" + line[1] + r"</trti>")
            transPointerMem = r"</tr>"
    #end of a translation
    elif tag == "trans-see":
        addTagToPage("<trsee>")
        transPointerMem = r"</trsee>"
    elif tag == "trans-top-also":
        addTagToPage("<tralso>")
        transPointerMem = r"</tralso>"
        newPointer += 1
    elif tag == "trans-bottom":
        addTagToPage(transPointerMem)
        transPointerMem = ""
    return transPointerMem
def inputData(cutLines):
    global newPage
    global newPointer
    global currentLangCode
    currentLangCode, currentLangScript = "", ""
    #Set language and language codes so they can be later referred
    if len(headingList) > 0:
        currentLang = headingList[0]
        currentLangCode, currentLangScript = getLangCodeAndScript(currentLang)
    newPointerMem, transPointerMem = "", ""
    #If there are multiple etymologies add tags around them
    if len(headingList) > 0:
        if (headingList[-1])[:9] == "Etymology":
            if len(headingList[-1]) > 9:
                subtag1 = "<e" + headingList[-1][10:] + ">"
                subtag2 = "</e" + headingList[-1][10:] + ">"
            else:
                subtag1 = "<e>"
                subtag2 = "</e>"
            newPointerMem = subtag2
            newPage.insert(newPointer, subtag1)
            newPointer += 1
    #print(f"hl:{headingList},title={title},cutLines={cutLines}")
    for line in cutLines:
        if line.find("{{") == -1 and line.find("[[") == -1:
            pass
            # if headerN!=0:
            #     if "Etymology" == headingList[-1][:9]:
            #         pass
            #     else:
            #         pass#print(headingList[-1])
        elif line[:2] == "{{":
            line = cleanTextForTags(line, currentLangCode, currentLangScript)
            tag, hasBar = getTag(line)
            line2 = regrexLine(line) # used for certain lines as it is redudant information for them!
            if len(headingList) > 0:
                if tag == "also":
                    processAlsoTemplate(line, hasBar)
                elif "Derived terms" == headingList[-1]:
                    processDerivedTerms(line2, tag)
                elif "Descendants" == headingList[-1]:
                    processDescendantTerms(line2, tag)
                elif "Translations" == headingList[-1]:
                    transPointerMem = processTranslations(line2, tag, transPointerMem)
                else:
                    processDefinitionTemplates(line, tag, hasBar)
                    #add compounds or idioms!
            #print(f"hl:{headingList},title={title}")
        elif line[:2]=="[[":
            pass#add support for derived terms or idioms
    if newPointerMem != "":
        newPage.insert(newPointer, newPointerMem)
        newPointer += 1
#gets a list and 
def splitOnTemplates(subEntry):
    cutLines = []
    for line in subEntry:
        line = replaceQuotes(line)
        newLine = []
        line = [line]
        while len(line) > 0:
            line = lineCut(lineCut(lineCut(lineCut(line, "{{", 1), "[[", 1), "}}", 2), "]]", 2)
            newLine.append(line[0])
            line.pop(0)
        cutLines = cutLines.copy() + newLine.copy()
    return cutLines
def formatCase(subEntry):
    splitLines = splitOnTemplates(subEntry)
    enclosers, enclosersI, enclosersJ, cutLines = [], [], [], []
    brackets = ["{{", "}}", "[[", "]]"]
    i = 0
    mem = ""
    for line in splitLines:
        j = 0
        oldChar = ""
        if not any(bracket in line for bracket in brackets):
            if len(enclosers) == 0:
                line = line.replace("\t", "").lower()
                cutLines.append(line)
            else:
                mem = mem + line
        else:
            for char in line:
                sumChar = oldChar + char
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
                                        mem = (splitLines[i2])[enclosersJ[-1]:j + 1]
                                    else:
                                        mem = (splitLines[i2])[enclosersJ[-1]:]
                                elif i2 == i:
                                    mem = mem + (splitLines[i2])[:j + 1]
                                else:
                                    mem = mem + splitLines[i2]
                            enclosers.pop()
                            enclosersI.pop()
                            enclosersJ.pop()
                            cutLines.append(mem)
                        except:
                            pass
                oldChar = char
                j += 1
        i += 1
    inputData(cutLines)
def addTagToPage(tag):
    global newPointer, newPointer
    newPage.insert(newPointer, tag)
    newPointer += 1

def loopThruPage(page):
    page2 = page.split("\n")
    page2 = list(filter(('').__ne__, page2))
    subEntry = []
    urequalN, equalN2 = 0, 0
    mode, urmode,ururmode = "", "", ""
    initnewPage() #initialise new page
    global headingList, newPage, newPointer
    headingList = []
    for line in page2:
        if "<" in line:
            if ">" in line:
                line = re.sub(r'<.+>', '', line)
        equalN = 0
        if line[:2] == "==":
            for i in range(2,7):
                if line[:i] == "======"[:i] and line[i] != "=":
                    if line.count("=") == i * 2:
                        urequalN = equalN2
                        equalN = i
                        equalN2 = i
                        urmode = mode
                        mode = line.replace("=", "")
            if equalN > 0:
                if urequalN != 1:
                    if urequalN == 2:
                        if urmode == "":
                            urmode = headingList[-1]
                            addTagToPage(r"</L" + getLangCode(urmode) + ">")
                        elif ururmode != "": #check if there any languages tags that haven't been closed of
                            addTagToPage(r"</L" + getLangCode(ururmode) + ">")#inserts the closing tag before inserting
                        headingList = [urmode]
                        addTagToPage("<L" + getLangCode(urmode) + ">") #inserts tags , e.g <Len> test.. </Len> around tags
                        ururmode=urmode
                    elif urequalN != 0:
                        headingList.append(urmode)
                    formatCase(subEntry)
                subEntry = []
            else:
                subEntry.append(line)
        else:
            subEntry.append(line)
    if urmode == "":
        if len(headingList)>0:
            print(headingList)
            urmode = headingList[-1]
            addTagToPage(r"</L" + getLangCode(urmode) + ">")
        else:
            pass#not expecting a print
            """ print("mistake")
            print(f"urmode=[{urmode}],mode=[{mode}],title=[{title}]") """
    elif ururmode != "": #check if there any languages tags that haven't been closed of
        addTagToPage(r"</L" + getLangCode(ururmode) + ">")#inserts the closing tag before inserting
    else:
        addTagToPage(r"</L" + getLangCode(urmode) + ">")
    
#imports language data from 
def importLangData():
    global langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars
    langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars=([] for i in range(12))
    with open("lang.txt", 'r', encoding = "utf8") as langFile:
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
                    langFamily.append(langList[5])
                    #langSortkey.append(langList[6])
                    #langAutodetect.append(langList[7])
                    #langExceptional.append(langList[8])
                    langScriptCodes.append(langList[9])
                    #langAltName.append(langList[10])#also known as 'other names'
                    #langStandardChars.append(langList[11])
                    #don't need all lists so I am deleting some to help memory.
            lineI += 1
newPage = []
newPointer = ""
importLangData()
print("Welcome to Etymaps Translation Program\nCopyright ©2024 Alexander Samuels")
lineCount = 0
webpage=[]
entryCount = 0
with open(r"xml//text.txt", 'r', encoding = 'utf8') as file:
    for line in file:
        lineCount += 1
        if "<page>" in line:
            webpage = []
            webpage.append(line)
        elif "</page>" in line:
            #webpage is now finished to analyse
            webpage.append(line)
            webpage = '\n'.join(webpage)
            tree = ElementTree.fromstring(webpage)
            title = (tree.find('title')).text
            revision = tree.find('revision')#returnTag(tree,"revision")
            if ((tree.find('ns')).text) == '0': #if not a special nor talk page
                #decided not to use usernames to credit users
                page = (revision.find("text")).text#returnTag(revision,"text").text #different variable name since text is too vague + converted to string so it is easier
                if not page is None:
                    loopThruPage(page)
                    #if NewPage is filled, added it to the file
                    if len(newPage) > 3: 
                        with open(r'xml//translate.txt', 'a', encoding = "utf-8") as file2:
                            #file2.write(f"--{title}--\n")
                            for fileLine in newPage:

                                file2.write(f"{fileLine}\n")
                            #file2.write(f"--/{title}--\n")
                        entryCount += 1
        else:
            webpage.append(line)
        if lineCount % 1000000 == 0:
            print(str(entryCount) + "\t" + str(round((100 * lineCount) / 479268517, 2)) + str("%"))
            print("Title:\t\t" + title)

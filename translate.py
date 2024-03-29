###Copyright ©2024 Alexander Samuels###
import xml.etree.ElementTree as ElementTree#since
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
#remove tag from line before addToPage
def addToPage2(tag, line):
    if line.count("|") > 1:
        line = line.split("|", 1)[1]
    lineMinusTag = line.replace("{{", "").replace("}}", "")
    addToPage(tag, lineMinusTag)

def lineCut(line, char,lineSide):
    if line[0].find(char)!=-1:
        if lineSide==1:
            lineMem=line[0][:line[0].find(char)]
        else:
            lineMem=line[0][line[0].find(char)+2:]
        if len(lineMem)>0:
            if lineSide==1:#eg, {{,[[
                line.insert(1,(line[0])[line[0].find(char):])
                line[0]=(line[0])[:line[0].find(char)]
            elif lineSide==2:#eg, }} , ]]
                line.insert(1,(line[0])[line[0].find(char)+2:])
                line[0]=(line[0])[:line[0].find(char)+2]
        return line.copy()
    else:
        return line.copy()
def getTag(line):
    if line.find("|")>=0:
        return line[2:].split("|",1)[0],True
    return line[:2].replace("}}","").replace("]]",""),False
def ofForm(tag, line):
    if tag == "adj form of":#pos improve template, with more adjectives
        addToPage2("ofa", line)
    elif tag == "inflection of" or tag == "infl of":
        addToPage2("ofi", line)
    elif tag == "noun form of":
        addToPage2("ofn", line)
    elif tag == "participle of":
        addToPage2("ofpar", line)
    elif tag == "pi-nr-inflection of":
        addToPage2("of-pinf", line)
    elif tag == "verb form of":
        addToPage2("ofvf", line)
    elif tag == "abbreviation of" or tag == "abbr of" or tag == "abbrev of":
        addToPage2("ofabr", line)
    elif tag == "abstract noun of":
        addToPage2("ofabn", line)
    elif tag == "acronym of":
        addToPage2("ofacr", line)
    elif tag == "active participle of":
        addToPage2("ofacr", line)
    elif tag == "agent noun of":
        addToPage2("ofagn", line)
    elif tag == "akkadogram of":
        addToPage2("ofakk", line)
    elif tag == "alternative case form of" or tag == "alt case form of" or tag == "alt case form" or tag == "alt case of" or tag == "alt case" or tag == "altcase":
        addToPage2("ofalc", line)
    elif tag == "alternative form of" or tag == "altform" or tag == "alt form" or tag == "alt form of":
        addToPage2("ofal", line)
    elif tag == "alternative plural of":
        addToPage2("ofalp", line)
    elif tag == "alternative reconstruction of":
        addToPage2("ofalr", line)
    elif tag == "alternative spelling of" or tag == "alt sp" or tag == "alt sp of":
        addToPage2("ofals", line)
    elif tag == "alternative typography of" or tag == "alt typ":
        addToPage2("ofalg", line)
    elif tag == "aphetic form of":
        addToPage2("ofaph", line)
    elif tag == "apocopic form of" or tag == "apoc of":
        addToPage2("ofapo", line)
    elif tag == "archaic form of":
        addToPage2("ofarf", line)
    elif tag == "archaic inflection of":
        addToPage2("ofari", line)
    elif tag == "archaic spelling of" or tag == "archaic sp":
        addToPage2("ofars", line)
    elif tag == "aspirate mutation of":
        addToPage2("ofasm", line)
    elif tag == "assimilated harmonic variant of":
        addToPage2("ofahv", line)
    elif tag == "attributive form of":
        addToPage2("ofatt", line)
    elif tag == "augmentative of":
        addToPage2("ofaug", line)
    elif tag == "broad form of":
        addToPage2("ofbf", line)
    elif tag == "causative of":
        addToPage2("ofca", line)
    elif tag == "censored spelling of" or tag == "cens sp":
        addToPage2("ofcsp", line)
    elif tag == "clipping of" or tag == "clip of":
        addToPage2("ofclp", line)
    elif tag == "combining form of" or tag == "com form":
        addToPage2("ofcmf", line)
    elif tag == "comparative of":
        addToPage2("ofcom", line)
    elif tag == "continuative of":
        addToPage2("ofcti", line)
    elif tag == "contraction of" or tag == "contr of":
        addToPage2("ofctr", line)
    elif tag == "conversion of":
        addToPage2("ofcnv", line)
    elif tag == "dated form of" or tag == "dated form":
        addToPage2("ofda", line)
    elif tag == "dated spelling of" or tag == "dated sp":
        addToPage2("ofds", line)
    elif tag == "deliberate misspelling of":
        addToPage2("ofdsp", line)
    elif tag == "desiderative of":
        addToPage2("ofdsi", line)
    elif tag == "diminutive of" or tag == "dim of":
        addToPage2("ofdim", line)
    elif tag == "eclipsis of":
        addToPage2("ofec", line)
    elif tag == "eggcorn of":
        addToPage2("ofeg", line)
    elif tag == "ellipsis of":
        addToPage2("ofell", line)
    elif tag == "elongated form of":
        addToPage2("ofelo", line)
    elif tag == "endearing diminutive of":
        addToPage2("ofedm", line)
    elif tag == "endearing form of":
        addToPage2("ofedf", line)
    elif tag == "euphemistic form of" or tag == "euph form":
        addToPage2("ofeuf", line)
    elif tag == "eye dialect of":
        addToPage2("ofey", line)
    elif tag == "female equivalent of" or tag == "femeq":
        addToPage2("offq", line)
    elif tag == "feminine of":
        addToPage2("off", line)
    elif tag == "feminine plural of":
        addToPage2("offp", line)
    elif tag == "feminine plural past participle of":
        addToPage2("off3p", line)
    elif tag == "feminine singular of":
        addToPage2("offs", line)
    elif tag == "feminine singular past participle of":
        addToPage2("offsp", line)
    elif tag == "former name of":
        addToPage2("offn", line)
    elif tag == "frequentative of":
        addToPage2("offrq", line)
    elif tag == "gerund of":
        addToPage2("ofg", line)
    elif tag == "h-prothesis of":
        addToPage2("ofh-", line)
    elif tag == "hard mutation of":
        addToPage2("ofhm", line)
    elif tag == "harmonic variant of":
        addToPage2("ofhv", line)
    elif tag == "hiatus-filler form of" or tag == "hf form":
        addToPage2("ofhf", line)
    elif tag == "honorific alternative case form of" or tag == "honor alt case" or tag == "honour alt case":
        addToPage2("ofho", line)
    elif tag == "imperfective form of":
        addToPage2("ofim", line)
    elif tag == "informal form of":
        addToPage2("ofif", line)
    elif tag == "informal spelling of":
        addToPage2("ofis", line)
    elif tag == "initialism of" or tag == "init of":
        addToPage2("ofint", line)
    elif tag == "iterative of":
        addToPage2("ofite", line)
    elif tag == "IUPAC-1":
        addToPage2("ofi1", line)
    elif tag == "IUPAC-3":
        addToPage2("ofi3", line)
    elif tag == "lenition of":
        addToPage2("ofle", line)
    elif tag == "literary form of":
        addToPage2("ofli", line)
    elif tag == "masculine noun of":
        addToPage2("ofmn", line)
    elif tag == "masculine of":
        addToPage2("ofm", line)
    elif tag == "masculine plural of":
        addToPage2("ofmp", line)
    elif tag == "masculine plural past participle of":
        addToPage2("ofm3p", line)
    elif tag == "medieval spelling of":
        addToPage2("ofmed", line)
    elif tag == "men's speech form of":
        addToPage2("ofmsf", line)
    elif tag == "misconstruction of":
        addToPage2("ofmsc", line)
    elif tag == "misromanization":
        addToPage2("ofmsr", line)
    elif tag == "misspelling of" or tag == "missp":
        addToPage2("ofmsp", line)
    elif tag == "mixed mutation of":
        addToPage2("ofmm", line)
    elif tag == "momentane of":
        addToPage2("ofmo", line)
    elif tag == "nasal mutation of":
        addToPage2("ofna", line)
    elif tag == "negative of":
        addToPage2("ofng", line)
    elif tag == "neuter equivalent of" or tag == "neuteq":
        addToPage2("ofnq", line)
    elif tag == "neuter plural of":
        addToPage2("ofnp", line)
    elif tag == "neuter singular of":
        addToPage2("ofnes", line)
    elif tag == "neuter singular past participle of":
        addToPage2("ofn2p", line)
    elif tag == "nomen sacrum form of":
        addToPage2("ofnsf", line)
    elif tag == "nominalization of" or tag == "nom of":
        addToPage2("ofnm", line)
    elif tag == "nonstandard form of" or tag == "nonstandard form" or tag == "nonst form" or tag == "ns form":
        addToPage2("ofnsf", line)
    elif tag == "nonstandard spelling of" or tag == "nonst sp" or tag == "ns sp":
        addToPage2("ofnsp", line)
    elif tag == "nuqtaless form of":
        addToPage2("ofnqf", line)
    elif tag == "ny-obs in Malawi":
        addToPage2("ofny-", line)
    elif tag == "obsolete form of" or tag == "obs form":
        addToPage2("ofof", line)
    elif tag == "obsolete spelling of" or tag == "obs sp":
        addToPage2("ofos", line)
    elif tag == "obsolete typography of" or tag == "obs typ":
        addToPage2("ofot", line)
    elif tag == "paragogic form of":
        addToPage2("ofpar", line)
    elif tag == "passive participle of":
        addToPage2("ofpss", line)
    elif tag == "past participle of":
        addToPage2("ofpst", line)
    elif tag == "pejorative of":
        addToPage2("ofpej", line)
    elif tag == "perfective form of":
        addToPage2("ofprf", line)
    elif tag == "plural of":
        addToPage2("ofp", line)
    elif tag == "present participle of":
        addToPage2("ofprp", line)
    elif tag == "pronunciation spelling of" or tag == "pron spelling of" or tag == "pron sp of" or tag == "pron sp":
        addToPage2("ofps", line)
    elif tag == "pronunciation variant of":
        addToPage2("ofpp", line)
    elif tag == "prothetic form of":
        addToPage2("ofpf", line)
    elif tag == "pseudo-acronym of":
        addToPage2("ofps", line)
    elif tag == "pt-pronoun-with-l":
        addToPage2("ofptl", line)
    elif tag == "pt-pronoun-with-n":
        addToPage2("ofptn", line)
    elif tag == "rare form of":
        addToPage2("ofrf", line)
    elif tag == "rare spelling of" or tag == "rare sp":
        addToPage2("ofrs", line)
    elif tag == "reflexive of":
        addToPage2("ofref", line)
    elif tag == "relational adjective of" or tag == "rel adj of" or tag == "rel adj":
        addToPage2("ofrel", line)
    elif tag == "rfform":
        addToPage2("ofrff", line)
    elif tag == "romanization of":
        addToPage2("ofro", line)
    elif tag == "runic spelling of":
        addToPage2("ofru", line)
    elif tag == "scribal abbreviation of" or tag == "scrib of" or tag == "scrib abbr of" or tag == "scrib abbrev of" or tag == "scribal abbr of" or tag == "scribal abbrev of":
        addToPage2("ofsc", line)
    elif tag == "short for":
        addToPage2("ofsh", line)
    elif tag == "singular of":
        addToPage2("ofsi", line)
    elif tag == "slender form of":
        addToPage2("ofsl", line)
    elif tag == "soft mutation of":
        addToPage2("ofso", line)
    elif tag == "spelling of":
        addToPage2("ofsp", line)
    elif tag == "standard form of":
        addToPage2("ofsf", line)
    elif tag == "standard spelling of" or tag == "stand sp":
        addToPage2("ofss", line)
    elif tag == "sumerogram of":
        addToPage2("ofsum", line)
    elif tag == "superlative of":
        addToPage2("ofsup", line)
    elif tag == "superseded spelling of":
        addToPage2("ofsus", line)
    elif tag == "syncopic form of":
        addToPage2("ofsyf", line)
    elif tag == "synonym of" or tag == "syn of":
        addToPage2("ofsyn", line)
    elif tag == "t-prothesis of":
        addToPage2("oft-pr", line)
    elif tag == "Tifinagh spelling of":
        addToPage2("ofti", line)
    elif tag == "topicalized form of":
        addToPage2("ofto", line)
    elif tag == "uncommon form of" or tag == "uncommon form":
        addToPage2("ofucf", line)
    elif tag == "uncommon spelling of" or tag == "uncommon sp":
        addToPage2("ofucs", line)
    elif tag == "verbal noun of":
        addToPage2("ofv", line)
    elif tag == "word-final anusvara form of":
        addToPage2("ofwfa", line)
    elif tag.find("form of")>0:
        line=currentLangCode+"|"+line.replace("{{","").replace("}}","")
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
            addToPage2("in", line)
        elif tag == "borrowed" or tag == "bor" or tag == "bor+":#included template bor+
            addToPage2("bo", line)
        elif tag == "derived" or tag == "der" or tag == "der+" or tag == "der-lite":#included template der+, der-lite
            addToPage2("de", line)
        elif tag == "undefined derivation" or tag == "uder" or tag == "der?":
            addToPage2("d?", line)
        elif tag == "calque" or tag == "cal" or tag == "clq":
            addToPage2("ca", line)
        elif tag == "semantic loan" or tag == "sl":
            addToPage2("sl", line)
        elif tag == "partial calque" or tag == "pcal" or tag == "pclq":
            addToPage2("pc", line)
        elif tag == "descendant" or tag == "desc":
            addToPage2("ds", line)
        elif tag == "descendat tree" or tag == "desctree":
            addToPage2("dt", line)
        elif tag == "cognate" or tag == "cog":
            addToPage2("cg", line)
        elif tag == "noncognate" or tag == "noncog" or tag == "ncog" or tag == "nc":
            addToPage2("ncg", line)
        elif tag == "learned borrowing" or tag == "lbor":
            addToPage2("lbo", line)
        elif tag == "orthographic borrowing" or tag == "obor":
            addToPage2("obo", line)
        elif tag == "semi-learned borrowing" or tag == "slbor":
            addToPage2("slb", line)
        elif tag == "unadapted borrowing" or tag == "ubor":
            addToPage2("ubo", line)
        elif tag == "mention" or tag == "m" or tag == "langname-mention" or tag == "m+":# included template m+
            addToPage2("m", line)
        elif tag == "affix" or tag == "af":
            addToPage2("af", line)
        elif tag == "prefix" or tag == "pre":
            addToPage2("pf", line)
        elif tag == "confix" or tag == "con":
            addToPage2("cf", line)
        elif tag == "suffix" or tag == "suf":
            addToPage2("sf", line)
        elif tag == "compound" or tag == "cp":
            addToPage2("cp", line)
        elif tag == "blend":
            addToPage2("be", line)
        elif tag == "clipping":
            addToPage2("cl", line)
        elif tag == "short for":
            addToPage2("sh4", line)
        elif tag == "back-form" or tag == "bf" or tag == "back-formation":
            addToPage2("bf", line)
        elif tag == "doublet" or tag == "dbt":
            addToPage2("2l", line)
        elif tag == "onomatopoeic" or tag == "onom":
            addToPage2("on", line)
        elif tag == "unk" or tag == "unknown":
            addToPage2("unk", line)
        elif tag == "unc" or tag == "uncertain":
            addToPage2("unc", line)
        elif tag == "rfe":
            addToPage2("rfe", line)
        elif tag == "etystub":
            addToPage2("ets", line)
        elif tag == "apocopic form":
            addToPage2("apo", line)
        elif tag == "aphetic form":
            addToPage2("aph", line)
        elif tag == "causative":
            addToPage2("cau", line)
        



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
        currentLangCode=getLangCode(currentLang)
        #print(currentLang+currentLangCode)
    newPointerMem=0
    newPointerMem2=0
    
    #If there are multiple etymologies add tags around them
    if caseN==3:
        if (headingList[-1])[:9]=="Etymology":
            if len(headingList[-1])>9:
                newPointerMem=1
                subtag1="<"+"e"+headingList[-1][11:]+">"
                subtag2="<"+"/"+"e"+headingList[-1][11:]+">"
                newPage.insert(newPointer,subtag1)
                newPointer+=1
                newPage.insert(newPointer,subtag2)
    
    for line in cutLines:
        line=re.sub(u'[\u064e\u064f\u0650\u0651\u0652\u064c\u064b\u064d\u0640\ufc62]','', line)
        if currentLangCode=="grk-mar":
            if hasCryillic(line):
                re.sub(u'[\u0301]','', line)
        elif currentLangCode=="zlw=slv":
            line=makeEntryName(line)
        else:
            replacements = [chr(0x303), chr(0x304), chr(0x307), chr(0x308), chr(0x323), chr(0x32E), chr(0x330), chr(0x331), chr(0x711), "[" + chr(0x730) + "-" + chr(0x74A) + "]"]
            for replacement in replacements:
                line = re.sub(replacement, "", line)
        tag=""
        if line.find("{{")==-1 and line.find("[[")==-1:
            if caseN!=0:
                if caseN==3 and "Etymology"==headingList[-1]:
                    pass
                else:
                    pass#print(headingList[-1])
        elif line[:2]=="{{":
            tag,hasBar=getTag(line)
            if tag == "also" and hasBar:
                if line.find("|sc=")>=0 or line.find("|uni=")>=0 or line.find("|uniN=")>=0 or line.find("|scN=")>=0:
                    print(f"@also={line}")
                else:
                    addToPage("a",line.replace("}}","").replace("{{","")[5:])#need to add parser for appendix
            elif caseN==3:

                if "Etymology"==(headingList[-1])[:9]:
                    etymTag(tag,line,hasBar)
                elif "Alternative forms"==headingList[-1]:
                    if tag == "l" or tag == "l-self" or tag == "link" or tag == "ll":
                        addToPage2("al", line)
                else:#nouns etc
                    if tag == "form of":
                        pass#get tag
                        addToPage2("ofj", line)
                    elif tag == "lb":
                        pass#dp stuff
                    else:
                        line=line#only get |1= and |2= for line, ignore rest
                        ofForm(tag, line)
                        
                #pass#Etymology
            elif caseN==4:
                line=re.sub(r'\|sort=.+?\|','|', line)
                line=re.sub(r'\|title=.+?\|','|', line)
                line=re.sub(r'\|sc=.+?\|','|', line)
                line=re.sub(r'\|collapse=.+?\|','|', line)
                if "Derived terms"==headingList[-1]:
                    if tag[:3]=="col" or tag[:3]=="der":
                        cutLines=line.split('|')
                        clLang=cutLines[1].replace("{{","").replace("}}","")
                        clI=0
                        for cutLine in cutLines:
                            if clI==1:
                                cutLine=re.sub(r'[{{].+[}}].','',cutLine).replace(r"/","")
                                cutLine=re.sub(r'\].+\[','|',cutLine)
                                cutLine=cutLine.replace("[","").replace("]","").replace("{{","").replace("}}","")
                                cutLine=[cutLine.split("|")]
                                clJ=0
                                for cutLine2 in cutLine:
                                    if len(cutLine2[clJ])>0:
                                        clmem="{{d|"+clLang+"|"+cutLine2[clJ]+"}}"
                                        addToPage2("d",clmem)
                                    clJ+=1
                            clI=1
                    elif tag == "l":
                        addToPage2("d", line)
                #elif ":
                elif "Descendants"==headingList[-1]:
                    if tag == "desc" or tag == "descendant":
                        line=re.sub(r'\|bor=.+?\|','|', line)
                        line=line.split("|")
                        if len(line)>=3:
                            clmem=line[0]+"|"+line[1]+"|"+line[2]+"}}"
                            addToPage2("v",clmem)
                elif "Translations"==headingList[-1]:
                    if tag == "t" or tag == "t+" or tag == "tt" or tag == "tt+":
                        line=re.sub(r'\|sc=.+?\|','|', line)
                        line=re.sub(r'\|alt=.+?\|','|', line)
                        line=re.sub(r'\|lit=.+?\|','|', line)
                        line=re.sub(r'\|id=.+?\|','|', line)
                        #keeping translations (tr=...)
                        line=line.split("|")
                        if len(line)==3:
                            transMem="{{t|"+line[1]+"|"+line[2]
                        elif len(line)>=4:
                            transMem="{{t|"+line[1]+"|"+line[2]+"|"+line[3]
                        addToPage2("t",transMem)
                        
                    elif tag == "trans-top":
                        line=re.sub(r'\|id=.+?\|','|', line)
                        line=re.sub(r'\|column-width=.+?\|','|', line)
                        line=line.replace("}}","").split("|")
                        if len(line)>=2:
                            newPointerMem2=1
                            transMem=line[0]+"|"+line[1]
                            subtag1="<tr><trti>"+line[1]+r"</trti>"
                            subtag2="</tr>"
                            newPage.insert(newPointer,subtag1)
                            newPointer+=1
                            newPage.insert(newPointer,subtag2)
                    elif tag == "trans-bottom":
                        newPointer+=newPointerMem2
                        newPointerMem2=0
                    any
        
        elif line[:2]=="[[":
            tag=getTag(line)
            #print(f"tag:{tag}\tinline:{line}")
            #add
        else:
            print(f"ACHTUNG: Data not declined\tline={line}")
        i+=1
    newPointer+=newPointerMem
def formatCase(subEntry,caseN):
    cutLines=[]
    newLine=[]
    mem=""
    for line in subEntry:
        line=replaceQuotes(line)
        newLine=[]
        line=[line]## I need to properly format html tags like, for example <math></math>
        while len(line)>0:
            line=lineCut(lineCut(lineCut(lineCut(line,"{{",1),"[[",1),"}}",2),"]]",2)
            newLine.append(line[0])
            line.pop(0)
        i=0
        cutLines=cutLines.copy()+newLine.copy()
    enclosers=[]
    enclosersI=[]
    enclosersJ=[]
    brackets=["{{","}}","[[","]]"]
    i=0
    i2=0
    cutLines2=[]
    for line in cutLines:
        j=0
        oldChar=""
        if not any(bracket in line for bracket in brackets):
            if len(enclosers)==0:
                line=line.replace("\t","").lower()
                cutLines2.append(line)
            else:
                mem=mem+line
        else:
            for char in line:
                sumChar=oldChar+char
                if sumChar in brackets:
                    if sumChar=="{{"or sumChar=="[[":
                        enclosers.append(sumChar)
                        enclosersI.append(i)
                        enclosersJ.append(j-1)     
                    else:
                        mem=""
                        try:
                            for i2 in range(enclosersI[-1],i+1):
                                if i2==enclosersI[-1]:
                                    if i2==i:
                                        mem=(cutLines[i2])[enclosersJ[-1]:j+1]
                                    else:
                                        mem=(cutLines[i2])[enclosersJ[-1]:]
                                elif i2==i:
                                    mem=mem+(cutLines[i2])[:j+1]
                                else:
                                    mem=mem+cutLines[i2]
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
    page2=page.split("\n")
    page2=list(filter(('').__ne__, page2))
    subEntry=[]
    j=0
    urequalN=0
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
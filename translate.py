###Copyright ©2024 Alexander Samuels
import xml.etree.ElementTree as ET
import re
import unicodedata

def returnTag(root,tag):
    counter=0
    for test in root.iter(tag):
        if counter==0:
            return test
        else:
            print("Achtung: multiple "+tag+"s!")
    print("Achtung: '"+tag+"' does not exist!")
def swapDualDelimiters(subEntry):
##    subEntry2=[]
##    if len(subEntry)>0:
##        for line in subEntry:
##            subEntry2.append(line.replace("''{{","{{<'>").replace("}}''","<'>}}").replace("''[[","[[<'>").replace("]]''","<'>]]"))
##    return subEntry2
    return subEntry
def getLangCode(inputLang):
    try:
        canonIndex=langCanon.index(inputLang)
        if canonIndex>len(langCode):
            return "?"
        else:
            return langCode[canonIndex]
    except:
        return "?"
def initnPage():
    global nPage
    global nPointer
    titletag="<ti>"+title.text+"</ti>"
    nPage=["<pa>",titletag,"</pa>"]
    nPointer=2
    #print(f"nPage={nPage}")
#def lineFind(line,Char):
 #   return len
def convertTags(line):
    a=1
    #print(nPage)
def quotRepl(line):
##    while line.find("'''")>=0:
##        line=line.replace("'''","[[<3>",1)
##        line=line.replace("'''","<3>]]",1)
##    while line.find("''")>=0:
##        line=line.replace("''","[[<2>",1)
##        line=line.replace("''","<2>]]",1)
    line=line.replace("'''","")
    line=line.replace("''","")
    return line
def addToPage(tag,line):
    #print(nPage)
    global nPointer,nPage
    #print(nPage)
    #print(nPointer)
    subtag1="<"+tag+">"
    subtag2="<"+"/"+tag+">"
    if len(line)>0:
        insert=subtag1+line+subtag2
    else:
        insert=subtag1+subtag2
    nPage.insert(nPointer,insert)
    nPointer+=1
def addToPage3(tag,line,lenTag):
    if line.count("|")>1:
        line2=line.split("|",1)
        line=line2[1]
    line=line.replace("{{","").replace("}}","")
    lenTag+=1
    addToPage(tag,line)
def addToPage2(tag,line,lenTag):
    lenTag+=1
    addToPage3(tag,line,lenTag)
    #addToPage2(tag,(line.replace("}}","").replace("{{",""))[lenTag:])
def atp(tag,line,lenTag):
    addToPage3("of"+tag,line,lenTag)
def lineCut(line,char,lineSide):
    if line[0].find(char)!=-1:
        if lineSide==1:
            lineMem=line[0][:line[0].find(char)]
        else:
            lineMem=line[0][line[0].find(char)+2:]
        if len(lineMem)>0:
            if lineSide==1:#{{,[[
                line.insert(1,(line[0])[line[0].find(char):])
                line[0]=(line[0])[:line[0].find(char)]
            elif lineSide==2:#}} , ]]
                line.insert(1,(line[0])[line[0].find(char)+2:])
                line[0]=(line[0])[:line[0].find(char)+2]
        return line.copy()
    else:
        return line.copy()
def getTag(line):
    if line.find("|")>=0:
        return line[2:].split("|",1)[0],True
    return line[:2].replace("}}","").replace("]]",""),False
def ofForm(tag,a,b):
    if tag=="adj form of":#pos improve template, with more adjectives
        atp("a",a,b)
    elif tag=="inflection of" or tag=="infl of":
        atp("i",a,b)
    elif tag=="noun form of":
        atp("n",a,b)
    elif tag=="participle of":
        atp("par",a,b)
    elif tag=="pi-nr-inflection of":
        atp("-pinf",a,b)
    elif tag=="verb form of":
        atp("vf",a,b)
    elif tag=="abbreviation of" or tag=="abbr of" or tag=="abbrev of":
        atp("abr",a,b)
    elif tag=="abstract noun of":
        atp("abn",a,b)
    elif tag=="acronym of":
        atp("acr",a,b)
    elif tag=="active participle of":
        atp("acr",a,b)
    elif tag=="agent noun of":
        atp("agn",a,b)
    elif tag=="akkadogram of":
        atp("akk",a,b)
    elif tag=="alternative case form of" or tag=="alt case form of" or tag=="alt case form" or tag=="alt case of" or tag=="alt case" or tag=="altcase":
        atp("alc",a,b)
    elif tag=="alternative form of" or tag=="altform" or tag=="alt form" or tag=="alt form of":
        atp("al",a,b)
    elif tag=="alternative plural of":
        atp("alp",a,b)
    elif tag=="alternative reconstruction of":
        atp("alr",a,b)
    elif tag=="alternative spelling of" or tag=="alt sp" or tag=="alt sp of":
        atp("als",a,b)
    elif tag=="alternative typography of" or tag=="alt typ":
        atp("alg",a,b)
    elif tag=="aphetic form of":
        atp("aph",a,b)
    elif tag=="apocopic form of" or tag=="apoc of":
        atp("apo",a,b)
    elif tag=="archaic form of":
        atp("arf",a,b)
    elif tag=="archaic inflection of":
        atp("ari",a,b)
    elif tag=="archaic spelling of" or tag=="archaic sp":
        atp("ars",a,b)
    elif tag=="aspirate mutation of":
        atp("asm",a,b)
    elif tag=="assimilated harmonic variant of":
        atp("ahv",a,b)
    elif tag=="attributive form of":
        atp("att",a,b)
    elif tag=="augmentative of":
        atp("aug",a,b)
    elif tag=="broad form of":
        atp("bf",a,b)
    elif tag=="causative of":
        atp("ca",a,b)
    elif tag=="censored spelling of" or tag=="cens sp":
        atp("csp",a,b)
    elif tag=="clipping of" or tag=="clip of":
        atp("clp",a,b)
    elif tag=="combining form of" or tag=="com form":
        atp("cmf",a,b)
    elif tag=="comparative of":
        atp("com",a,b)
    elif tag=="continuative of":
        atp("cti",a,b)
    elif tag=="contraction of" or tag=="contr of":
        atp("ctr",a,b)
    elif tag=="conversion of":
        atp("cnv",a,b)
    elif tag=="dated form of" or tag=="dated form":
        atp("da",a,b)
    elif tag=="dated spelling of" or tag=="dated sp":
        atp("ds",a,b)
    elif tag=="deliberate misspelling of":
        atp("dsp",a,b)
    elif tag=="desiderative of":
        atp("dsi",a,b)
    elif tag=="diminutive of" or tag=="dim of":
        atp("dim",a,b)
    elif tag=="eclipsis of":
        atp("ec",a,b)
    elif tag=="eggcorn of":
        atp("eg",a,b)
    elif tag=="ellipsis of":
        atp("ell",a,b)
    elif tag=="elongated form of":
        atp("elo",a,b)
    elif tag=="endearing diminutive of":
        atp("edm",a,b)
    elif tag=="endearing form of":
        atp("edf",a,b)
    elif tag=="euphemistic form of" or tag=="euph form":
        atp("euf",a,b)
    elif tag=="eye dialect of":
        atp("ey",a,b)
    elif tag=="female equivalent of" or tag=="femeq":
        atp("fq",a,b)
    elif tag=="feminine of":
        atp("f",a,b)
    elif tag=="feminine plural of":
        atp("fp",a,b)
    elif tag=="feminine plural past participle of":
        atp("f3p",a,b)
    elif tag=="feminine singular of":
        atp("fs",a,b)
    elif tag=="feminine singular past participle of":
        atp("fsp",a,b)
    elif tag=="former name of":
        atp("fn",a,b)
    elif tag=="frequentative of":
        atp("frq",a,b)
    elif tag=="gerund of":
        atp("g",a,b)
    elif tag=="h-prothesis of":
        atp("h-",a,b)
    elif tag=="hard mutation of":
        atp("hm",a,b)
    elif tag=="harmonic variant of":
        atp("hv",a,b)
    elif tag=="hiatus-filler form of" or tag=="hf form":
        atp("hf",a,b)
    elif tag=="honorific alternative case form of" or tag=="honor alt case" or tag=="honour alt case":
        atp("ho",a,b)
    elif tag=="imperfective form of":
        atp("im",a,b)
    elif tag=="informal form of":
        atp("if",a,b)
    elif tag=="informal spelling of":
        atp("is",a,b)
    elif tag=="initialism of" or tag=="init of":
        atp("int",a,b)
    elif tag=="iterative of":
        atp("ite",a,b)
    elif tag=="IUPAC-1":
        atp("i1",a,b)
    elif tag=="IUPAC-3":
        atp("i3",a,b)
    elif tag=="lenition of":
        atp("le",a,b)
    elif tag=="literary form of":
        atp("li",a,b)
    elif tag=="masculine noun of":
        atp("mn",a,b)
    elif tag=="masculine of":
        atp("m",a,b)
    elif tag=="masculine plural of":
        atp("mp",a,b)
    elif tag=="masculine plural past participle of":
        atp("m3p",a,b)
    elif tag=="medieval spelling of":
        atp("med",a,b)
    elif tag=="men's speech form of":
        atp("msf",a,b)
    elif tag=="misconstruction of":
        atp("msc",a,b)
    elif tag=="misromanization":
        atp("msr",a,b)
    elif tag=="misspelling of" or tag=="missp":
        atp("msp",a,b)
    elif tag=="mixed mutation of":
        atp("mm",a,b)
    elif tag=="momentane of":
        atp("mo",a,b)
    elif tag=="nasal mutation of":
        atp("na",a,b)
    elif tag=="negative of":
        atp("ng",a,b)
    elif tag=="neuter equivalent of" or tag=="neuteq":
        atp("nq",a,b)
    elif tag=="neuter plural of":
        atp("np",a,b)
    elif tag=="neuter singular of":
        atp("nes",a,b)
    elif tag=="neuter singular past participle of":
        atp("n2p",a,b)
    elif tag=="nomen sacrum form of":
        atp("nsf",a,b)
    elif tag=="nominalization of" or tag=="nom of":
        atp("nm",a,b)
    elif tag=="nonstandard form of" or tag=="nonstandard form" or tag=="nonst form" or tag=="ns form":
        atp("nsf",a,b)
    elif tag=="nonstandard spelling of" or tag=="nonst sp" or tag=="ns sp":
        atp("nsp",a,b)
    elif tag=="nuqtaless form of":
        atp("nqf",a,b)
    elif tag=="ny-obs in Malawi":
        atp("ny-",a,b)
    elif tag=="obsolete form of" or tag=="obs form":
        atp("of",a,b)
    elif tag=="obsolete spelling of" or tag=="obs sp":
        atp("os",a,b)
    elif tag=="obsolete typography of" or tag=="obs typ":
        atp("ot",a,b)
    elif tag=="paragogic form of":
        atp("par",a,b)
    elif tag=="passive participle of":
        atp("pss",a,b)
    elif tag=="past participle of":
        atp("pst",a,b)
    elif tag=="pejorative of":
        atp("pej",a,b)
    elif tag=="perfective form of":
        atp("prf",a,b)
    elif tag=="plural of":
        atp("p",a,b)
    elif tag=="present participle of":
        atp("prp",a,b)
    elif tag=="pronunciation spelling of" or tag=="pron spelling of" or tag=="pron sp of" or tag=="pron sp":
        atp("ps",a,b)
    elif tag=="pronunciation variant of":
        atp("pp",a,b)
    elif tag=="prothetic form of":
        atp("pf",a,b)
    elif tag=="pseudo-acronym of":
        atp("ps",a,b)
    elif tag=="pt-pronoun-with-l":
        atp("ptl",a,b)
    elif tag=="pt-pronoun-with-n":
        atp("ptn",a,b)
    elif tag=="rare form of":
        atp("rf",a,b)
    elif tag=="rare spelling of" or tag=="rare sp":
        atp("rs",a,b)
    elif tag=="reflexive of":
        atp("ref",a,b)
    elif tag=="relational adjective of" or tag=="rel adj of" or tag=="rel adj":
        atp("rel",a,b)
    elif tag=="rfform":
        atp("rff",a,b)
    elif tag=="romanization of":
        atp("ro",a,b)
    elif tag=="runic spelling of":
        atp("ru",a,b)
    elif tag=="scribal abbreviation of" or tag=="scrib of" or tag=="scrib abbr of" or tag=="scrib abbrev of" or tag=="scribal abbr of" or tag=="scribal abbrev of":
        atp("sc",a,b)
    elif tag=="short for":
        atp("sh",a,b)
    elif tag=="singular of":
        atp("si",a,b)
    elif tag=="slender form of":
        atp("sl",a,b)
    elif tag=="soft mutation of":
        atp("so",a,b)
    elif tag=="spelling of":
        atp("sp",a,b)
    elif tag=="standard form of":
        atp("sf",a,b)
    elif tag=="standard spelling of" or tag=="stand sp":
        atp("ss",a,b)
    elif tag=="sumerogram of":
        atp("sum",a,b)
    elif tag=="superlative of":
        atp("sup",a,b)
    elif tag=="superseded spelling of":
        atp("sus",a,b)
    elif tag=="syncopic form of":
        atp("syf",a,b)
    elif tag=="synonym of" or tag=="syn of":
        atp("syn",a,b)
    elif tag=="t-prothesis of":
        atp("t-pr",a,b)
    elif tag=="Tifinagh spelling of":
        atp("ti",a,b)
    elif tag=="topicalized form of":
        atp("to",a,b)
    elif tag=="uncommon form of" or tag=="uncommon form":
        atp("ucf",a,b)
    elif tag=="uncommon spelling of" or tag=="uncommon sp":
        atp("ucs",a,b)
    elif tag=="verbal noun of":
        atp("v",a,b)
    elif tag=="word-final anusvara form of":
        atp("wfa",a,b)
###code for 
def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))    
def remove_diacritics(text):
    return ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')

def make_entry_name(text):
    # Remove diacritics from vowels and consonants
    text = re.sub(r'[aeɛioɵuʉt̪s̪]+[\u0300-\u036F]*', lambda match: remove_diacritics(match.group()), text)

    return text
##
def etymTag(tag,line,lT,hasBar):
    if hasBar:
        if tag=="inh" or tag=="inherited" or tag=="inh" or tag=="inh-lite":#included template inh+, inh-lite
            addToPage2("in",line,lT)
        elif tag=="borrowed" or tag=="bor" or tag=="bor+":#included template bor+
            addToPage2("bo",line,lT)
        elif tag=="derived" or tag=="der" or tag=="der+" or tag=="der-lite":#included template der+, der-lite
            addToPage2("de",line,lT)
        elif tag=="undefined derivation" or tag=="uder" or tag=="der?":
            addToPage2("d?",line,lT)
        elif tag=="calque" or tag=="cal" or tag=="clq":
            addToPage2("ca",line,lT)
        elif tag=="semantic loan" or tag=="sl":
            addToPage2("sl",line,lT)
        elif tag=="partial calque" or tag=="pcal" or tag=="pclq":
            addToPage2("pc",line,lT)
        elif tag=="descendant" or tag=="desc":
            addToPage2("ds",line,lT)
        elif tag=="descendat tree" or tag=="desctree":
            addToPage2("dt",line,lT)
        elif tag=="cognate" or tag=="cog":
            addToPage2("cg",line,lT)
        elif tag=="noncognate" or tag=="noncog" or tag=="ncog" or tag=="nc":
            addToPage2("ncg",line,lT)
        elif tag=="learned borrowing" or tag=="lbor":
            addToPage2("lbo",line,lT)
        elif tag=="orthographic borrowing" or tag=="obor":
            addToPage2("obo",line,lT)
        elif tag=="semi-learned borrowing" or tag=="slbor":
            addToPage2("slb",line,lT)
        elif tag=="unadapted borrowing" or tag=="ubor":
            addToPage2("ubo",line,lT)
        elif tag=="mention" or tag=="m" or tag=="langname-mention" or tag=="m+":# included template m+
            addToPage2("m",line,lT)
        elif tag=="affix" or tag=="af":
            addToPage2("af",line,lT)
        elif tag=="prefix" or tag=="pre":
            addToPage2("pf",line,lT)
        elif tag=="confix" or tag=="con":
            addToPage2("cf",line,lT)
        elif tag=="suffix" or tag=="suf":
            addToPage2("sf",line,lT)
        elif tag=="compound" or tag=="cp":
            addToPage2("cp",line,lT)
        elif tag=="blend":
            addToPage2("be",line,lT)
        elif tag=="clipping":
            addToPage2("cl",line,lT)
        elif tag=="short for":
            addToPage2("sh4",line,lT)
        elif tag=="back-form" or tag=="bf" or tag=="back-formation":
            addToPage2("bf",line,lT)
        elif tag=="doublet" or tag=="dbt":
            addToPage2("2l",line,lT)
        elif tag=="onomatopoeic" or tag=="onom":
            addToPage2("on",line,lT)
        elif tag=="unk" or tag=="unknown":
            addToPage2("unk",line,lT)
        elif tag=="unc" or tag=="uncertain":
            addToPage2("unc",line,lT)
        elif tag=="rfe":
            addToPage2("rfe",line,lT)
        elif tag=="etystub":
            addToPage2("ets",line,lT)
        elif tag=="apocopic form":
            addToPage2("apo",line,lT)
        elif tag=="aphetic form":
            addToPage2("aph",line,lT)
        elif tag=="causative":
            addToPage2("cau",line,lT)
        #elif tag=="



            ## add tag==acronomyn
    else:
        pass
def inputData(cutLines,caseN,header):
    i=0
    global nPage
    global nPointer
    if len(headingList)>0:
        currentLang=headingList[0]
        currentLangCode=getLangCode(currentLang)
        #print(currentLang+currentLangCode)
    nPointMem=0
    nPointMem2=0
    currentLangCode=""
    transList=[]
    #print(headingList)
    if caseN==3:
        if (headingList[-1])[:9]=="Etymology":
            if len(headingList[-1])>9:
                nPointMem=1
                subtag1="<"+"e"+headingList[-1][11:]+">"
                subtag2="<"+"/"+"e"+headingList[-1][11:]+">"
                nPage.insert(nPointer,subtag1)
                nPointer+=1
                nPage.insert(nPointer,subtag2)
    
    for line in cutLines:
        #print(f"line1|{line}")
        line=re.sub(u'[\u064e\u064f\u0650\u0651\u0652\u064c\u064b\u064d\u0640\ufc62]','',line)
        if currentLangCode=="grk-mar":
            if has_cryillic(line):
                re.sub(u'[\u0301]','',line)
        elif currentLangCode=="zlw=slv":
            line=make_entry_name(line)
        else:
            replacements = [chr(0x303), chr(0x304), chr(0x307), chr(0x308), chr(0x323), chr(0x32E), chr(0x330), chr(0x331), chr(0x711), "[" + chr(0x730) + "-" + chr(0x74A) + "]"]
            for replacement in replacements:
                line = re.sub(replacement, "", line)
        tag=""
        if line.find("{{")==-1 and line.find("[[")==-1:
            if caseN!=0:
                a=1
                if caseN==3 and "Etymology"==headingList[-1]:
                    pass
                else:
                    pass#print(headingList[-1])
        elif line[:2]=="{{":
            tag,hasBar=getTag(line)
            #print(f"tag={tag}")
            lT=len(tag)
            #print(f"line2|{line}")
            #print(f"tag:{tag}\tinline:{line}")
            if tag=="also" and hasBar:
                if line.find("|sc=")>=0 or line.find("|uni=")>=0 or line.find("|uniN=")>=0 or line.find("|scN=")>=0:
                    print(f"@also={line}")
                else:
                    addToPage("a",line.replace("}}","").replace("{{","")[5:])#need to add parser for appendix
            elif caseN==3:
                #print(headingList[-1])
                if "Etymology"==(headingList[-1])[:9]:
                    etymTag(tag,line,lT,hasBar)
                elif "Alternative forms"==headingList[-1]:
                    if tag=="l" or tag=="l-self" or tag=="link" or tag=="ll":
                        addToPage2("al",line,lT)
                else:#nouns etc
                    if tag=="form of":
                        pass#get tag
                    elif tag=="lb":
                        pass#dp stuff
                    else:
                        line=line#only get |1= and |2= for line, ignore rest
                        ofForm(tag,line,lT)
                        
                #pass#Etymology
            elif caseN==4:
                #print("casen woo")
                #print(f"line3|{line}")
                line=re.sub(r'\|sort=.+?\|','|',line)
                line=re.sub(r'\|title=.+?\|','|',line)
                line=re.sub(r'\|sc=.+?\|','|',line)
                line=re.sub(r'\|collapse=.+?\|','|',line)
                #print(f"line4|{line}")
                if "Derived terms"==headingList[-1]:
                    if tag[:3]=="col" or tag[:3]=="der":
                        #print(f"tag={tag}\tline={line}")
                        cutLines=line.split('|')
                        clLang=cutLines[1].replace("{{","").replace("}}","")
                        clI=0
                        #print("lolop"+str(cutLines))
                        #print(f"clLang={clLang}")
                        for cutLine in cutLines:
                            if clI==1:
                                #print(cutLine)
                                cutLine=re.sub(r'[{{].+[}}].','',cutLine).replace(r"/","")
                                cutLine=re.sub(r'\].+\[','|',cutLine)
                                cutLine=cutLine.replace("[","").replace("]","").replace("{{","").replace("}}","")
                                cutLine=[cutLine.split("|")]
                                #print(cutLine)
                                clJ=0
                                for cutLine2 in cutLine:
                                    if len(cutLine2[clJ])>0:
                                        clmem="{{d|"+clLang+"|"+cutLine2[clJ]+"}}"
                                        #print(clmem)
                                        addToPage2("d",clmem,1)
                                    clJ+=1
                            clI=1
                    elif tag=="l":
                        addToPage2("d",line,lT)
                #elif ":
                elif "Descendants"==headingList[-1]:
                    if tag=="desc" or tag=="descendant":
                        line=re.sub(r'\|bor=.+?\|','|',line)
                        line=line.split("|")
                        #print(f"desc?{line}")
                        if len(line)>=3:
                            clmem=line[0]+"|"+line[1]+"|"+line[2]+"}}"
                            addToPage2("v",clmem,lT)
                elif "Translations"==headingList[-1]:
                    if tag=="t" or tag=="t+" or tag=="tt" or tag=="tt+":
                        line=re.sub(r'\|sc=.+?\|','|',line)
                        #line=re.sub(r'\|tr=.+?\|','|',line)
                        line=re.sub(r'\|alt=.+?\|','|',line)
                        line=re.sub(r'\|lit=.+?\|','|',line)
                        line=re.sub(r'\|id=.+?\|','|',line)
                        line=line.split("|")
                        #print(line)
                        if len(line)==3:
                            transMem="{{t|"+line[1]+"|"+line[2]
                        elif len(line)>=4:
                            transMem="{{t|"+line[1]+"|"+line[2]+"|"+line[3]
                        addToPage2("t",transMem,1)
                        
                    elif tag=="trans-top":
                        line=re.sub(r'\|id=.+?\|','|',line)
                        line=re.sub(r'\|column-width=.+?\|','|',line)
                        if len(transList)>1:
                            raise Exception("Error len(transList)>1")
                        line=line.replace("}}","").split("|")
                        if len(line)>=2:
                            nPointMem=1
                            transMem=line[0]+"|"+line[1]
                            subtag1="<tr><trti>"+line[1]+r"</trti>"
                            subtag2="</tr>"
                            nPage.insert(nPointer,subtag1)
                            nPointer+=1
                            nPage.insert(nPointer,subtag2)
                            
                            
                        else:
                            raise Exception("Error on len(line), transmem")
                    elif tag=="trans-bottom":
                        nPointer+=nPointMem2
                        nPointMem2=0
                    any
        
        elif line[:2]=="[[":
            tag=getTag(line)
            #print(f"tag:{tag}\tinline:{line}")
            #add
        else:
            print(f"ACHTUNG: Data not declined\tline={line}")
        i+=1
    nPointer+=nPointMem
def formatCase(subEntry,caseN,header):
    openBracket=0
    #if len(subEntry)>0:
        #print(f"subEntry={subEntry}")
    cutLines=[]
    newLine=[]
    mem=""
    for line in subEntry:
        #print(f"1:{line}")
        line=quotRepl(line)
        newLine=[]
        line=[line]## I need to properly format html tags like, for example <math></math>
        while len(line)>0:
            line=lineCut(lineCut(lineCut(lineCut(line,"{{",1),"[[",1),"}}",2),"]]",2)
            newLine.append(line[0])
            line.pop(0)
        i=0
##        for line2 in newLine:
##            brackets=[line2.count("{{"),line2.count("[["),line2.count("}}"),line2.count("]]")]
##            brackets[0]
        cutLines=cutLines.copy()+newLine.copy()
    
    #if len(newLine)>0:
       # print(f"cutLines={cutLines}")
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
                #print(f"line={line}")
                cutLines2.append(line)
            else:
                mem=mem+line
                #print(f"line'{line}")
        else:
            for char in line:
                #print(oldChar+","+char)
                sumChar=oldChar+char
                if sumChar in brackets:
                    #print(f"sumChar{sumChar}")
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
                                        #print("kurzschnitt")
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
                            print(f"i=({i}),i2=({i2}) ,j=({j}) \n line={line}\n cutLines={cutLines}\n enclosers={enclosers}\n enclosersI={enclosersI}\n enclosersJ={enclosersJ}") 
##                        enclosers.pop()
##                        enclosersI.pop()
##                        enclosersJ.pop()
##                        cutLines2.append(mem)
                        #print(f"mem={mem}")
                oldChar=char
                j+=1
        i+=1
    #print("\n")
    #print(cutLines2)
    inputData(cutLines2,caseN,header)
def loopThruPage(page):
    #print(f"loopThruPage{nPage}")
    page2=page.split("\n")
    page2=list(filter(('').__ne__, page2))
    #print(page2)
    subEntry=[]
    lineX=0
    j=0
    urequalN=0
    mode=""
    urmode=""
    equalN2=0
    initnPage()
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
                else:
                    print("Error["+str(a)+"=]:"+line)
        if equalN>0:
            #print("urmode="+str(urmode)+"\t("+str(urequalN)+")")
            match urequalN:
                case 0:
                    #print("\t\t\t\t\n\n\n\nHelloworld\n\n\n\n")
                    #print(f"case{urequalN}:{subEntry}\turmode:{urmode}")
                    subEntry=swapDualDelimiters(subEntry)
                    formatCase(subEntry,urequalN,"")
                case 1:
                    print("error")
                case 2:
                    #print("lang2:"+str(subEntry)+"\turmode:"+str(urmode))
                    lang=getLangCode(urmode)
                    #print(lang)
                    #if len(str(subEntry))>2:
                     #   print("lang2:"+str(subEntry)+"\turmode:"+str(urmode))
                    subEntry=swapDualDelimiters(subEntry)
                    headingList=[urmode]
                    formatCase(subEntry,urequalN,urmode)
                case _:
                    #print(f"case{urequalN}:{subEntry}+\turmode:+{urmode}")
                    subEntry=swapDualDelimiters(subEntry)
                    headingList.append(urmode)
                    formatCase(subEntry,urequalN,"")

            
            subEntry=[]#do not comment/delete out

        else:
            subEntry.append(line)
    #necessary to print
    #print("lol")
    #print(subEntry)
    #print("@end@")
    folderName=(title.text+"_")[:2]
def importLangData():
    global langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars
    langCode,langCanon,langCategory,langType,langFamilycode,langFamily,langSortkey,langAutodetect,langExceptional,langScriptCodes,langAltName,langStandardChars=([] for i in range(12))
    with open("lang.txt",encoding="utf8") as langFile:
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
                #print(lL)
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

#def parse#
##def returnHeader(line,n):
##    if line[:2]=="==" and line[2]!="=":
##        if line.count("=")==4:
##            line=line.replace("=","")
##            print(line)
##            language=line
##        else:
##            print("Error[2=]:"+line)
#def

## Import Language data ##
nPage=[]
nPointer=""
importLangData()
succeeded=False
mode=input("Type search:\t")
if mode=="search":
    term=input("Type input:\t")
show=(str(input("Show percent complete Y/N:\t").upper())+"N")[0]
x=0
webpage=[];
with open(r"xml//text.txt",encoding='utf8') as file:
    for line in file:
        x+=1
        if "<page>" in line:
            webpage = []
            webpage.append(line)
        elif "</page>" in line:
            #print(webpage)
            #webpage is now finished to analyse
            webpage.append(line)
            webpage='\n'.join(webpage)
            #print(webpage)
            tree = ET.fromstring(webpage)
            title=returnTag(tree,"title")
            if mode=="search":
                title=returnTag(tree,"title")
                if title.text.upper()==term.upper():
                    revision=returnTag(tree,"revision")
                    page=returnTag(revision,"text").text #different variable name since text is too vague + converted to string so it is easier
                    #print(page)
            else:
                ns=returnTag(tree,"ns")
                revision=returnTag(tree,"revision")
                #print(title.text+"\t"+ns.text)
                if (ns.text)=='0': #if not a special nor talk page
                    print("Title:\t\t"+title.text)
                    #for child in revision:
                     #   print(child.tag, child.attrib)
                    #username=returnTag(contributor,"username") #doesn't work all the time since sometimes edits are made by IPs and have an IP xml tag instead of ID+username  \nprint(username.text)
                    page=returnTag(revision,"text").text #different variable name since text is too vague + converted to string so it is easier
                    initnPage()
                    #print(f"nPage2={nPage}")

                    loopThruPage(page)
                    #print(f"nPage{nPage}")
                    with open('xml//translate.txt', 'a', encoding="utf-8") as f:
                        for fileLine in nPage:
                            f.write(f"{fileLine}\n")
        else:
            webpage.append(line)
        if x%100000==0:
            if show=="Y":
                print(str(x)+"\t"+str(round((x/100000)/219*100))+str("%"))#21871733    329477303
        #print(line.rstrip())

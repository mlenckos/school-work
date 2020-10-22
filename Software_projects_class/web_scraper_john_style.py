import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

# -- Regex List -- 
education_list = ["Bachelor","Masters","PHD","Associate","Doctorate",'Boot.{,10}Camp']
programming_language_list =['Python', ' R ', ' SQL ', ' C/+/+ ', ' C ', ' java ', ' javascript ',' matlab ', 'scala', 'swift', 'julia']
#[' 1 ','1C:Enterprise programming language','A# .NET','A-0 System',r'A\+',r'A\+\+',' ABAP ',' ABC ','ABC ALGOL',' ACC ',' Accent ','Ace DASL (Distributed Application Specification Language)',' Action! ',' ActionScript ',' Actor ',' Ada ',' Adenine ',' Agda ',' Agilent VEE','Agora','AIMMS','Aldor','Alef','ALF','ALGOL 58','ALGOL 60','ALGOL 68','ALGOL W','Alice','Alma-0','AmbientTalk','Amiga E','AMOS','AMPL','AngelScript','Apex','APL','App Inventor for Android\'s visual block language','AppleScript','APT','Arc','ARexx','Argus','Assembly language','AutoHotkey','AutoLISP / Visual LISP','Averest','AWK','Axum','Active Server Pages','B ','Babbage','Ballerina','Bash','BASIC','bc','BCPL','BeanShell','Batch file (Windows/MS-DOS)','Bertrand','BETA','BLISS','Blockly','BlooP','Boo','Boomerang','Bourne shell (including bash and ksh)',r' C ','C--','C\+\+ (C plus plus) – ISO/IEC 14882',' C\* ',' C# ','C/AL','Caché ObjectScript','C Shell (csh)','Caml','Cayenne','CDuce','Cecil','Cesil','Céu','Ceylon','CFEngine',' Cg ',' Ch ','Chapel','Charity','Charm','CHILL','CHIP-8','chomski','ChucK','Cilk','Citrine','CL (IBM)','Claire','Clarion','Clean','Clipper','CLIPS','CLIST','Clojure','CLU','CMS-2','COBOL – ISO/IEC 1989','CobolScript – COBOL Scripting language','Cobra','CoffeeScript','ColdFusion','COMAL','Combined Programming Language (CPL)','COMIT','Common Intermediate Language (CIL)','Common Lisp (also known as CL)','COMPASS','Component Pascal','Constraint Handling Rules (CHR)','COMTRAN','Cool','Coq','Coral 66','CorVision','COWSEL','CPL','Cryptol','Crystal','Csound','Cuneiform','Curl','Curry','Cybil','Cyclone','Cython',' D ','DASL (Datapoint\'s Advanced Systems Language)','Dart','Darwin','DataFlex','Datalog','DATATRIEVE','dBase',' dc ','DCL','DinkC','DIBOL','Dog','Draco','DRAKON','Dylan','DYNAMO','DAX (Data Analysis Expressions)','E ','Ease','Easy PL/I','EASYTRIEVE PLUS','eC','ECMAScript','Edinburgh IMP','EGL','Eiffel','ELAN','Elixir','Elm','Emacs Lisp','Emerald','Epigram','EPL (Easy Programming Language)','EPL (Eltron Programming Language)','Erlang','es','Escher','ESPOL','Esterel','Etoys','Euclid','Euler','Euphoria','EusLisp Robot Programming Language','CMS EXEC (EXEC)','EXEC 2','Executable UML','Ezhil','F','F#','F* ','Factor','Fantom','FAUST','FFP','fish','Fjölnir','FL','Flavors','Flex','FlooP','FLOW-MATIC','FOCAL','FOCUS','FOIL','FORMAC','@Formula','Forth','Fortran – ISO/IEC 1539','Fortress','FP','Franz Lisp','Futhark','F-Script','Game Maker Language','GameMonkey Script','GAMS','GAP','G-code','GDScript','Genie','GDL','GEORGE','GLSL','GNU E','Go','Go!','GOAL','Gödel','Golo','GOM (Good Old Mad)','Google Apps Script','Gosu','GOTRAN','GPSS','GraphTalk','GRASS','Grasshopper','Groovy','H','Hack','HAGGIS','HAL/S','Halide (programming language)','Hamilton C shell','Harbour','Hartmann pipelines','Haskell','Haxe','Hermes','High Level Assembly','HLSL','Hollywood','HolyC','Hop','Hopscotch','Hope','Hugo','Hume','HyperTalk','I','Io','Icon','IBM Basic assembly language','IBM HAScript','IBM Informix-4GL','IBM RPG','Irineu','IDL','Idris','Inform','J ','J#','J\+\+','JADE','JAL','Janus (concurrent constraint programming language)','Janus (time-reversible computing programming language)','JASS','Java','JavaFX Script','JavaScript','Jess (programming language)','JCL','JEAN','Join Java','JOSS','Joule','JOVIAL','Joy','JScript','JScript .NET','Julia','Jython','K','Kaleidoscope','Karel','KEE','Kixtart','Klerer-May System','KIF','Kojo','Kotlin','KRC','KRL','KRL (KUKA Robot Language)','KRYPTON','Korn shell (ksh)','Kodu','Kv','L','LabVIEW','Ladder','LANSA','Lasso','Lava','LC-3','Legoscript','LIL','LilyPond','Limbo','Limnor','LINC','Lingo','LINQ','LIS','LISA','Lisp – ISO/IEC 13816','Lite-C','Lithe','Little b','LLL','Logo','Logtalk','LotusScript','LPC','LSE','LSL','LiveCode','LiveScript','Lua','Lucid','Lustre','LYaPAS','Lynx','M','M2001','M4','M#','Machine code','MAD (Michigan Algorithm Decoder)','MAD/I','Magik','Magma','Maude system','Máni','Maple','MAPPER (now part of BIS)','MARK-IV (now VISION:BUILDER)','Mary','MASM Microsoft Assembly x86','MATH-MATIC','Mathematica','MATLAB','Maxima (see also Macsyma)','Max (Max Msp – Graphical Programming Environment)','MaxScript internal language 3D Studio Max','Maya (MEL)','MDL','Mercury','Mesa','Metafont','MHEG-5 (Interactive TV programming language)','Microcode','MicroScript','MIIS','Milk (programming language)','MIMIC','Mirah','Miranda','MIVA Script','Mixal','ML','Model 204','Modelica','Modula','Modula-2','Modula-3','Mohol','MOO','Mortran','Mouse','MPD','Mathcad','MSL','MUMPS','MuPAD','Mutan','Mystic Programming Language (MPL)','N','NASM','Napier88','Neko','Nemerle','NESL','Net.Data','NetLogo','NetRexx','NewLISP','NEWP','Newspeak','NewtonScript','Next Generation Shell','Nial','Nice','Nickle (NITIN)','Nim','NPL','Not eXactly C (NXC)','Not Quite C (NQC)','NSIS','Nu','NWScript','NXT-G','O','o:XML','Oak','Oberon','OBJ2','Object Lisp','ObjectLOGO','Object REXX','Object Pascal','Objective-C','Objective-J','Obliq','OCaml','occam','occam-π','Octave','OmniMark','Onyx','Opa','Opal','OpenCL','OpenEdge ABL','OPL','OpenVera','OPS5','OptimJ','Orc','ORCA/Modula-2','Oriel','Orwell','Oxygene','Oz','P','P4','P′′','ParaSail (programming language)','PARI/GP','Pascal – ISO 7185','Pascal Script','PCASTL','PCF','PEARL','PeopleCode','Perl','PDL','Pharo','PHP','Pico','Picolisp','Pict','Pig (programming tool)','Pike','PILOT','Pipelines','Pinecone','Pizza','PL-11','PL/0','PL/B','PL/C','PL/I – ISO 6160','PL/M','PL/P','PL/SQL','PL360','PLANC','Plankalkül','Planner','PLEX','PLEXIL','Plus','Pony','POP-11','POP-2','PostScript','PortablE','POV-Ray SDL','Powerhouse','PowerBuilder – 4GL GUI application generator from Sybase','PowerShell','PPL','Processing','Processing.js','Prograph','PROIV','Prolog','PROMAL','Promela','PROSE modeling language','PROTEL','ProvideX','Pro*C','Pure','Pure Data','PureScript','Python','Q','Q (programming language from Kx Systems)','Q# (Microsoft programming language)','Qalb','QtScript','QuakeC','QPL','Qbasic','R','R\+\+','Racket','Raku','RAPID','Rapira','Ratfiv','Ratfor','rc','Reason','REBOL','Red','Redcode','REFAL','REXX','Rlab','ROOP','RPG','RPL','RSL','RTL/2','Ruby','Rust','S','S2','S3','S-Lang','S-PLUS','SA-C','SabreTalk','SAIL','SAM76','SAS','SASL','Sather','Sawzall','Scala','Scheme','Scilab','Scratch','Script.NET','Sed','Seed7','Self','SenseTalk','SequenceL','Serpent','SETL','SIMPOL','SIGNAL','SiMPLE','SIMSCRIPT','Simula','Simulink','Singkong','Singularity','SISAL','SLIP','SMALL','Smalltalk','SML','Strongtalk','Snap!','SNOBOL (SPITBOL)','Snowball','SOL','Solidity','SOPHAEROS','Source','SPARK','Speakeasy','Speedcode','SPIN','SP/k','SPS','SQL','SQR','Squeak','Squirrel','SR','S/SL','Starlogo','Strand','Stata','Stateflow','Subtext','SBL','SuperCollider','SuperTalk','Swift (Apple programming language)','Swift (parallel scripting language)','SYMPL','SystemVerilog','T','TACL','TACPOL','TADS','TAL','Tcl','Tea','TECO','TELCOMP','TeX','TIE','TMG, compiler-compiler','Tom','Toi','Topspeed','TPU','Trac','TTM','T-SQL','Transcript','TTCN','Turing','TUTOR','TXL','TypeScript','Tynker','U','Ubercode','UCSD Pascal','Umple','Unicon','Uniface','UNITY','Unix shell','UnrealScript','V','Vala','Verilog','VHDL','Vim script','Viper','Visual Basic','Visual Basic .NET','Visual DataFlex','Visual DialogScript','Visual Fortran','Visual FoxPro','Visual J\+\+','Visual LISP','Visual Objects','Visual Prolog','VSXu','W ','WATFIV, WATFOR','WebAssembly','WebDNA','Whiley','Winbatch','Wolfram Language','Wyvern','X','X\+\+','X10','xBase','xBase\+\+','XBL','XC (targets XMOS architecture)','xHarbour','XL','Xojo','XOTcl','XOD (programming language)','XPath','XPL','XPL0','XQuery','XSB','XSharp','XSLT','Xtend','Y','Yorick','YQL','Yoix','YUI','Z','Z notation','Zebra, ZPL, ZPL2','Zeno','ZetaLisp','ZOPL','Zsh','ZPL','Z\+\+']
soft_skills_list = ['Presentation',"Leadership",'Communication',"Remote","Team Player","Cross-cultural","Travel",'Flexible','Dependable','Open minded','Conversationalist','Salesperson','Visionary']
keywords_list = ['Machine Learning','Deep Learning','Artificial Intelligence','Neural Network']
benefits_list = ['401K','Retirement','Healthcare','Loan Repayment','Dental','Vision']
state_list = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','Abbreviation:','DC','MH','Abbreviation:','AE','AA','AE','AE','AE','AP']
allist =[education_list, programming_language_list, soft_skills_list, keywords_list, benefits_list, state_list]

big_found_list=[]       



def add2list (lst, ist):
    try:
        lst.append(ist)
    except:
        lst.append('')

def elemAssign (elem):
    try: 
        return [elem.text.strip()]
    except:
        return []

max_postings = 100

url_list = ['https://www.indeed.com/jobs?q=Data+Scientist&l=']
company_list_found_final = []
location_list_found_final = []
title_list_found_final = []
salary_list_found_final = []
education_list_found_final = []
programming_language_list_found_final = []
soft_skills_list_found_final = []
keywords_list_found_final = []
benefits_list_found_final = []
state_list_found_final = []
allist3 = [company_list_found_final, location_list_found_final, title_list_found_final, education_list_found_final, programming_language_list_found_final, soft_skills_list_found_final, keywords_list_found_final, benefits_list_found_final, state_list_found_final]
           
for counter in range(10,max_postings,10):
    URL_test = requests.get('https://www.indeed.com/jobs?q=Data+Scientist&start='+str(counter))
    url_list.append('https://www.indeed.com/jobs?q=Data+Scientist&start='+str(counter))
        
for URL in url_list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='resultsCol')
    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
    print("Loaded: ",URL," urls")
    for job_elem in job_elems:
        # Each job_elem is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
        title_elem = job_elem.find('div', class_='title')
        company_elem = job_elem.find('span', class_='company')
        location_elem = job_elem.find('div', class_='location')
        salary_elem = job_elem.find('span', class_='salaryText')
        getInthere_url = job_elem.find('a').get('href')
        if None in (title_elem, company_elem, location_elem):
            continue

        #Get in there part
        elems = [location_elem, title_elem, salary_elem]
        getInThere_actualurl = "https://www.indeed.com"+getInthere_url.strip()
        git_soup = BeautifulSoup(requests.get(str(getInThere_actualurl)).content, 'html.parser')
        #print(getInThere_actualurl)
        results_git = git_soup.find(id='jobDescriptionText')

         # -- Found List -- 
        location_list_found = []
        title_list_found = []
        salary_list_found = []
        education_list_found = []
        programming_language_list_found = []
        soft_skills_list_found = []
        keywords_list_found = []
        benefits_list_found = []
        state_list_found = []
        allist2 = [location_list_found, title_list_found, salary_list_found, education_list_found, programming_language_list_found, soft_skills_list_found, keywords_list_found, benefits_list_found, state_list_found]
        
        for i in range (0, len(elems)):
            allist2[i]=elemAssign(elems[i])     

        # -- Start adding stuff to found list -- 
        if results_git == None:
            #print("NoneType Object for the url (aka no actual description page)")
            continue
        else:
            print(allist)
            for i in allist:
                for j in range(3,len(i)):
                    if re.search(re.compile(i[j],re.IGNORECASE),results_git.text):
                        allist2[j].append(i)

        count=0
        for i in range(0, len(allist3)):
            if(count<4 or count==8):
                add2list(allist3[i], allist2[i][0])
            else:
                add2list(allist3[i], allist2[i])


df = pd.DataFrame(data = allist3).T
df.columns = ["company_list","location","title","salary",'education','programming_languages','soft_skills','keywords','benefits','state']
print(df)
print(url_list)
df.to_csv("output.csv")

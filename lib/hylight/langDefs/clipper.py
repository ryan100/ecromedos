# -*- coding: UTF-8 -*-
# Clipper language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''announce begin break case declare do elseif else endif enddo end
endcase exit external field for if local loop memvar next otherwise parameters
private public recover request return sequence step static using while with
accept append all alternate box blank bell call cancel clear close commit
continue copy count create century color confirm console cursor delete dir
display date decimals default deleted delimiters device eject erase extended
epoch escape exact exclusive file find form from filter fixed format function
get gets go index init input intensity join keyboard key label list locate
memory menu margin message note order pack procedure prompt path printer quit
read recall reindex release rename replace report restore run relation say
screen structure save seek select set scoreboard softseek skip sort store sum
to typeahead text total type unique unlock update use wrap wait zap'''

KW_LIST['kwb'] = '''aadd abs achoice aclone acopy adel adir aeval afields afill ains
alert alias alltrim altd array asc ascan asize asort at atail average bin2i
bin2l bin2w bof browse cdow chr cmonth col colorselect ctod curdir day dbappend
dbclearfilter dbclearindex dbclearrelation dbcloseall dbclosearea dbcommit
dbcommitall dbcreate dbcreateindex dbdelete dbedit dbeval dbf dbfilter
dbgobottom dbgoto dbgotop dbrecall dbreindex dbrelation dbrselect dbseek
dbselectarea dbsetdriver dbsetfilter dbsetindex dbsetorder dbsetrelation dbskip
dbstruct dbunlock dbunlockall dbusearea descend devout devoutpict devpos
directory diskspace dispbegin dispbox dispcount dispend dispout doserror dow
dtoc dtos empty eof errorblock errorlevel eval exp fclose fcount fcreate ferase
ferror fieldblock fieldget fieldname  fieldpos fieldput fieldwblock fklabel
fkmax flock fopen found fread freadstr frename fseek fwrite getenv hardcr
header i2bin indexext indexkey indexord inkey int isalpha iscolor isdigit
islower isprinter isupper l2bin lastkey lastrec left len log lower ltrim
lupdate max maxcol maxrow memoedit memoline memoread memotran memowrit
memvarblock min mlcount mlctopos mlpos mod month mpostolc neterr netname
nextkey nosnow os outerr outstd pad pcol pcount procline procname prow qout rat
readexit readinsert readkey readmodal readvar reccount recno recsize replicate
restscreen right rlock round row rtrim savescreen scroll seconds setblink
setcancel setcolor setcursor setkey setmode setpos setprc soundex space sqrt
str strtran stuff substr time tone transform  updated upper  val valtype
version word year'''

STRINGDELIMITERS = "\" \'"

ESCCHAR = "\\"

SL_COMMENT = "// *"

ML_COMMENT = "/* */"

IGNORECASE = True

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = /   %  + -"



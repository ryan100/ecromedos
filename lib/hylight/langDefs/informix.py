# -*- coding: UTF-8 -*-
# INFORMIX language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''add after all allowing and any arg_val array arr_count arr_curr
as asc at attribute attributes auto autonext average avg before between bottom
by call case check clear clipped close column columns command comment comments
commit composites connect construct continue correct count current cursor
database declare default defer define delimiters desc describe display
displayonly distinct do down downshift else end entry every execute exists exit
extern false fetch field finish first for foreach form format formonly found
from function globals group having header help if in include input insert
instructions into is joining key label last lenght let line lineno lines log
main margin master matches max mdy menu message min mode name need next
nextfield no normal not notfound null num_args of on open option options or
order otherwise outer output page pageno prepare previous print printer
privileges program prompt query queryclear quit record register report resource
return returning reverse right row rowid run screen scroll scr_line select set
set_count share sizeof skip some sqlca start startlog static statistics status
step stop sum switch synonym systables then through thru to top trailer true
union unique unlock up upshift user using validate value values verify view
waiting warning when whenever where while with without work wrap'''

KW_LIST['kwb'] = '''alter break create delete drop editadd editupdate error errorlog err_get
err_print err_quit exclusive exitnow goto grant initialize interrupt lock
modify pause pipe public recover remove rename revoke rollback rollforward
sleep sqlerrd table tables temp update char date day dba decimal double dec
float index int integer like long lookup money month noentry noupdate percent
picture required short smallfloat smallint struct serial space spaces time
today type typedef unsigned weekday year zerofill'''

STRINGDELIMITERS="\" \'"

SL_COMMENT = "# --"

ML_COMMENT = "{ }"

ESCCHAR = "\\"

SYMBOLS = "( ) [ ] , ; : & | < > !  = / *  %  + -"

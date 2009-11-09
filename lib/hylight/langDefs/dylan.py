# -*- coding: UTF-8 -*-
# Dylan language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}
TAG_DELIM = {}

KW_LIST['kwa'] = '''interface library macro method class function cleanup block afterwards
end  constant variable generic primary begin method above below from by in instance
local  slot subclass then to virtual if when select case else elseif unless finally
otherwise  then for until while from to define let otherwise finally exception
handler signal import rename create use export exclude abstract concrete primary
inherited inline open sealed domain singleton'''

TAG_DELIM['kwa'] = "< >"

KW_LIST['kwb'] = '''module synopsis author copyright'''

KW_RE['kwd'] = "regex((\\w+?)\\s*(?=\\())"

STRINGDELIMITERS = "\" \'"

SL_COMMENT = "//"

ML_COMMENT = "/* */"

ALLOWNESTEDCOMMENTS = False

ESCCHAR = "\\"

SYMBOLS = "( ) [ ] { } , ; : & | !  = / *  %  + -"

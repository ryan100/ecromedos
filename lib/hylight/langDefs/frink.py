# -*- coding: UTF-8 -*-
# Frink language definition file *PROPOSAL*
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''if then else for to step next use while var class interface
return mod div conforms square sq cubic cu squared cube is  true TRUE false
FALSE  and AND or OR NOT not nand NAND nor NOR xor XOR implies IMPLIES dict
println sin cos tan sec csc cot arcsin arccos arcsin arccsc arcsec arccot
arctan floor ceil round round int trunc inv recip sqrt log ln abs format format
random randomBits bitLength modPow binary ternary trinary quaternary quinary
senary sexenary septenary octal oct octonary nonary decimal denary undenary
duodecimal duodenary tridecimal quattuordecimal quindecimal hexadecimal
sexadecimal hex septendecimal octodecimal nonadecimal vigesimal char uppercase
uc lowercase lc substr substring substrLen substringLen timezone timezones now
deltaT subst split join lines read stripHTML url urlHost urlProtocol select
sort  newJava callJava staticJava English en German Deutsch de Spanish Espanol
Espa�ol es French Francais Fran�ais fr Italian Italiano it Portuguese pt Korean
ko SimplifiedChinese zh TraditionalChinese Chinese zt Russian ru Japanese jp
Dutch Nederlands nl FromEnglish from_en FromGerman from_de FromSpanish from_es
FromFrench from_fr FromItalian from_it FromPortuguese from_pt FromJapanese
from_ja FromKorean from_ko FromRussian from_ru Default	FromSimplifiedChinese
from_zh FromTraditionalChinese FromChinese from_zt FromDutch from_nl
EnglishToGerman en_de EnglishToSpanish en_es EnglishToFrench en_fr
EnglishToItalian en_it EnglishToPortuguese en_pt EnglishToKorean en_ko
EnglishToJapanese en_ja EnglishToRussian en_ru EnglishToSimplifiedChinese en_zh
EnglishToTraditionalChinese en_zt EnglishToDutch en_nl GermanToEnglish Englisch
de_en GermanToFrench franzoesisch Franzoesisch franz�sisch Franz�sisch de_fr
SpanishToEnglish Ingl�s Ingles es_en SpanishToFrench frances Frances franc�s
Franc�s es_fr FrenchToEnglish Anglais fr_en FrenchToGerman Allemand allemand
fr_de FrenchToSpanish Espagnol espagnol fr_es FrenchToPortuguese Portugais
portugais fr_pt FrenchToItalian Italien italien fr_it ItalianToEnglish Inglese
it_en ItalianToFrench Francese francese it_fr PortugueseToEnglish Ingl�s pt_en
PortugueseToFrench franc�s Franc�s pt_fr JapaneseToEnglish ja_en
KoreanToEnglish ko_en RussianToEnglish ru_en SimplifiedChineseToEnglish zh_en
TraditionalChineseToEnglish ChineseToEnglish zt_en DutchToEnglish Engels nl_en'''

STRINGDELIMITERS = "\"\"\" \""

SL_COMMENT = "//"

ALLOWNESTEDCOMMENTS = False

IGNORECASE = False

ESCCHAR = "\\"

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = / * %  + -"

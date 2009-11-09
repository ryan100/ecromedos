# -*- coding: UTF-8 -*-
# AMPL language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''and arc by check cross close diff difference div data display drop
else exists end forall fix function if in inter intersection interval include
less let maximize minimize min max mod model node not or objective option param
prod product print printf quit reset restore set setof subject subj s.t.
symdiff sum shell solution then to union update unfix var write binary circular
coeff coef cover dimen dimension default display_1col display_eps
display_max_2d_cols display_precison display_round display_transpose
display_width from gutter_width integer Infinity ordered obj
objective_precision omit_zero_cols omit_zero_rows output_precision
print_precision print_round print_seperator symbolic within'''

KW_LIST['kwb'] = '''abs acos acosh alias asin asinh atan atan2 atanh Beta ceil cos
card Cauchy exp Exponential floor first Gamma Irand224 int log log10 last
member Normal next nextw ord ord0 Poisson precision prev prevw round sin sinh
sqrt tan tanh trunc Uniform Uniform01'''

STRINGDELIMITERS = "\" \'"

SL_COMMENT = "#"

ML_COMMENT = "/* */"

IGNORECASE = False

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = / *  %  + -"



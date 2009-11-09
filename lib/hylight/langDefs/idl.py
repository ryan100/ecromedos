# -*- coding: UTF-8 -*-
# IDL language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''case coclass  dispinterface enum interface library module pipe struct
switch typedef union'''

KW_LIST['kwb'] = '''auto boolean bstr byte char double error_status_t float handle_t
hbitmap henhmetafile hglobal hmetafile hmetafile_pict hpalette hresult hyper
int long safearray short signed small unsigned variant variant_bool void
wchar_t aggregatable appobject  bindable broadcast callback const
context_handle control custom default defaultbind defaultcollelem defaultvalue
defaultvtable displaybind dllname dual endpoint entry first_is handle
helpcontext helpfile helpstring helpstringcontext helpstringdll hidden id
idempotentent ignore iid_is immediatebind in last_is lcid length_is licensed
local max_is maybe message ms_union nonbrowsable noncreatable nonextensible
object oleautomation optional out pointer_default propget propput propputref
ptr public range readonly ref requestedit restricted retval size_is source
string switch_is switch_type transmit_as uidefault unique user_marshal
usesgetlasterror uuid v1_enum vararg version wire_marshal'''

STRINGDELIMITERS = "\""

SL_COMMENT = "//"

ML_COMMENT = "/* */"

IGNORECASE = True

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = / * %  + -"

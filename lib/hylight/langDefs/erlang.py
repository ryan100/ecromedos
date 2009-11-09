# -*- coding: UTF-8 -*-
# Erlang language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''after begin case catch cond end fun if let of query receive when'''

KW_LIST['kwb'] = '''abs alive apply atom_to_list binary_to_list binary_to_term concat_binary date disconnect_node element
erase exit float float_to_list get get_keys group_leader halt hd integer_to_list is_alive length link list_to_atom
list_to_binary list_to_float list_to_integer list_to_pid list_to_tuple load_module make_ref monitor_node node nodes
now open_port pid_to_list process_flag process_info process put register registered round self setelement size spawn
spawn_link split_binary statistics term_to_binary throw time tl trunc tuple_to_list unlink unregister whereis
atom binary constant function integer list number pid ports port_close port_info reference record
check_process_code delete_module get_cookie hash math module_loaded preloaded processes purge_module set_cookie set_node
acos asin atan atan2 cos cosh exp log log10 pi pow power sin sinh sqrt tan tanh'''

KW_RE['kwd'] = "regex((\\w+?)\\s*(?=\\())"

STRINGDELIMITERS = "\" \'"

SL_COMMENT = "%"

IGNORECASE = False

ESCCHAR = "\\"

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = / * + -"

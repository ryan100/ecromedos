# -*- coding: UTF-8 -*-
# BM Script language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''advance aggregate_member action base_model commit commit_zero computed_item computed_member
cycle conversion hange_model dimension dynamic_span decommission delete delete_task delete_job
end_command files item join_model job load_conversion_data load_items load_time load_cycles
load_dimension load_model member model nullify period queue_job route_file run_task specials spans
start_job_queue stop_job_queue span time task unit'''

KW_LIST['kwb'] = '''aggregation average aggregate_members additive_only ascii_extractor accumulator break_time
bad_outputs cycles consolidation computed_members consolidation commit_version cycle_dimension
converter displays dynamic_spans dimensions default dimension_only display_set uplicator
end_transformer expander exclude full flatten fixed_extractor fielder good_outputs gdl history
hierarchic_subtractive hierarchic_only holder items item_hierarchy include_all include inverted
incremental item_dimension incycle_dimension include_only joiner keyed limited load_model_incremental
logger members models name normal no non_keyed none normal new_version nullify_current nullify_from
precompute periods pivot qualifier retained restated repeated run_task_step synoyms subtractive_only
service sql_extractor stripper target time_latest time_dimension top_incycle transformer timer yes
across_field by_field copy cycle_field data default_allowed error file fields field_or_unit field
input_0 input_1 ignore item_specifier level meta numeric outputs output_0 output_1 password prepend
period_field query separator short_records source to text user    value warning business end exclusive
new shared sp'''

STRINGDELIMITERS = "\""

SL_COMMENT = "#"

IGNORECASE = True

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = / *  %  + -"

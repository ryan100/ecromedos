# -*- coding: UTF-8 -*-
# MSSQL,  Microsoft SQL Server TSQL language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = """absolute action after all all_constraints all_errormsgs
all_indexes all_levels alter and any ansi_defaults ansi_null_dflt_off
ansi_null_dflt_on ansi_nulls ansi_padding ansi_warnings append
arithabort arithignore as asc attach authorization auto backup begin
between break browse bulk by cascade case check checkalloc checkcatalog
checkconstraints checkdb checkfilegroup checkident checkpoint checktable
cleantable close clustered collate commit committed compute concat
concat_null_yields_null concurrencyviolation constraint contains
containstable context_info continue count_rows create cross cube current
cursor cursor_close_on_commit database datefirst dateformat dbcc
dbrepair dbreindex deadlock_priority deallocate declare default delay
delete deny desc disable_def_cnst_chk disk display distinct distributed
drop drop_existing dropcleanbuffers dump dynamic elements else emptyfile
encryption end entry escape estimateonly exec execute exists explicit
fast fast_forward fastfirstrow fetch filegroup filegrowth file
filelistonly filename fillfactor fips_flagger first fmtonly for force
forceplan foreign forward_only free freeproccache freetext from full
fullscan function global grant group go goto hash having headeronly help
holdlock identity identity_insert if ignore_dup_key
implicit_transactions in intermediate into index indexdefrag inner
inputbuffer insert instead intensive into io is isolation join keep
keep_replication key keyset kill labelonly language last left level like
load loadhistory local lock_timeout log logspace loop low maxdop maxsize
medianame mediapassword merge move name newalloc next no_infomsgs
nocount noexec nonclustered noindex nolock norecompute norecovery
noreseed noreset norewind normal not notruncate nounload nowait null
numeric_roundabort of off offsets on only open opentran optimistic
option or order outer output outputbuffer override pad_index paglock
parse_only partial password percent physical_only primary prior pintable
plan print privileges proc proccache procedure profile
query_governor_cost_limit quoted_identifier raw read read_only
readcommited readpast readtext readuncommited recompile reconfigure
recovery references relative remote_proc_transactions
repair_allow_data_loss repair_fast repair_rebuild repeatable
repeatableread replace replication reseed reset restart restore
restricted_user return returns revoke rewind right robust rollback
rollup rowcount rowguidcol rowlock rows rule sample save schema
schemabinding scroll scroll_locks select serializable set setuser
showcontig show_statistics showplan_all showplan_text shrinkdatabase
shrinkfile shutdown size some sqlperf standby startlog static statistics
statistics_norecompute stats statusonly stopat stopatmark stopbefore
stoplog some sort_in_tempdb table tableresults tablock tablockx tape
textimage_on textsize then time to top traceoff traceon tracestatus tran
transaction trigger truncate truncateonly type_warning uncommitted union
unique unlimited unload unpintable update updatetext updateusage updlock
use useoptions values varying verifyonly view view_metadata waitfor when
where while with work xact_abort xml xmldata"""

KW_LIST['kwb'] = """bigint binary bit char character datetime dec decimal
double float image int integer money national nchar numeric nvarchar
ntext precision real rowversion smalldatetime smallint smallmoney
sql_variant text timestamp tinyint uniqueidetifier varbinary varchar
varying"""

KW_LIST['kwc'] = """@@connections @@cpu_busy @@cursor_rows @@datefirst @@dbts
@@error @@fetch_status @@identity @@idle @@io_busy @@langid @@language
@@lock_timeout @@max_connections @@max_precision @@nestlevel @@options
@@pack_received @@pack_sent @@packet_errors @@procid @@remserver
@@rowcount @@servername @@servicename @@spid @@textsize @@timeticks
@@total_errors @@total_read @@total_write @@trancount @@version abs acos
app_name ascii asin atan atn2 avg binary_checksum cast convert ceiling
charindex checksum checksum_agg coalesce collationproperty col_length
col_name columnproperty columns_updated cos cot count count_big
current_timestamp current_user cursor_status databaseproperty
databasepropertyex datalength dateadd datediff datename datepart day
db_id db_name degrees difference exp file_id file_name filegroup_id
filegroup_name filegroupproperty fileproperty floor formatmessage
freetext freetexttable fulltextcatalogproperty fulltextserviceproperty
getansinull getdate getutcdate grouping has_dbaccess host_id host_name
ident_current ident_incr ident_seed indexkey_property indexproperty
index_col is_member is_srvrolemember isdate isnull isnumeric left len
log lower ltrim max min month newid nullif object_id object_name
objectproperty opendatasource openquery openrowset openxml parsename
patindex permissions pi power quotename radians raiseerror rand
replicate reverse right round rowcount_big rtrim scope_identity
serverproperty session_user sessionproperty sign sin soundex space
sql_variant_property square sqrt stats_date stdev sdevp str stuff
substring sum suser_id suser_name suser_sid suser_sname system_user tan
textptr textvalid trigger_nestlevel typeproperty unicode upper user
user_id user_name var varp year"""

STRINGDELIMITERS = "\'"

SL_COMMENT = "--"

ML_COMMENT = "/* */"

IGNORECASE = True

SYMBOLS = "( ) [ ] , ; : & | < > ! = / * % + - ^ ~"

IDENTIFIER = "regex(@?@?[a-zA-Z_][\\w]*)"


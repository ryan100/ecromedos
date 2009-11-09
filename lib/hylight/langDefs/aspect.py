# -*- coding: UTF-8 -*-
# Abstract language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''addfilename alarm ansitokey ansitooem atof atoi atol beep bitmap
bitmapbkg break breakpoint call capture capturestr case ceil chain chdir
checkbox clear clearxoff cliptofile cliptostr combobox comgetc commandmode
compile computc comread comwrite connect connectmanual copyfile crc16 ddeadvise
ddeexecute ddeinit ddepoke dderequest ddeterminate ddeunadvise decrypt default
delfile dial dialadd dialcancel dialclass dialcount dialcreate dialdelete
dialfind dialinsert dialload dialname dialnumber dialogbox  dialsave dialstats
dir dirlistbox dirpath disable disconnect diskfree dlgctrlwin dlgdestroy
dlgevent dlgexists dlglist dlgsave dlgshow dlgupdate dlgwin dlgwinctrl dllcall
dllfree dllload dllobject dllobjfile dllobjupdt dos editbox elifdef has failed.
else elseif enable encrypt endcase enddialog endfor endfunc endgroup endif
endproc endswitch endwhile errormsg execute exit exitfor exitswitch exitwhile
exitwindows faxcancel faxlist faxmodem faxpoll faxprint faxremove faxsend
faxstatus faxview fclear fclose fcombobox fdelblock feditbox feof ferror fetch
fflush fgetc fgets fileget fileset filetoclip fileview findfirst findnext
finsblock firsttask flength flistbox float floor fopen for  fputc fputs fread
fseek fstrfmt ftell ftext ftoa ftp ftruncate fullpath func fwrite getcur getdir
getenv getfile getfilename getpathname getvolume goto groupbox halt hangup help
hotspot icon iconbutton if integer intsltime isfile itemcount itemcreate
itemfind itemname itemremove itoa kermserve keyflush keyget keystate keytoansi
keytooem listbox locate long longjmp loopfor loopwhile ltimeelapsed ltimeints
ltimemisc ltimestring ltimestrs ltoa makepath mapisend mciexec mcisend
memaddress memalloc memavail memchr memcmp memfree memgetc memicmp memmove
memputc memread memrealloc memset memsize memwrite menubar menucheck menuitem
menuitemcount menupopup menupopupid menuselect menushow menushowpopup menustate
metafile metafilebkg metakey mkdir monthstr mspause nexttask nullstr numtostr
objcoord objhide objmove objpaint objpointid objremove objshow oemtoansi
oemtokey param pastetext pause pkmode pkrecv pksend playback printalign
printattr printcapture printchar printer printfit printfont printmargin
printstr printtabs printtabstr proc  profilerd profilewr pushbutton putenv
pwexit pwmode pwtitlebar radiobutton radiogroup  rand rename return rewind rget
rmdir rstrcmp run rxflush sbsave screentowin sdlgfopen sdlginput sdlgmsgbox
sdlgsaveas sendfile sendkey sendkeystr sendvkey set setjmp setpointer setup
shell shortpath snapshot splitpath statclear statmsg strcat strchr strcmp
strcpy strcspn strdelete strextract strfind strfmt strgetc stricmp string
strinsert strlen strlwr strncmp strnicmp strputc strquote strrchr strread
strreplace strrev strright strsearch strset strsltime strspn strtoclip strtok
strtonum strupdt strupr strwrite substr switch taskactivate taskexists taskexit
taskname taskpath taskwin termgetc termgets termkey termmsg termputc termputs
termreadc termreads termreset termvkey termwritec termwrites text transmit
txflush usermsg uwincreate uwinpaint uwinremove uwutowin waitfor waitquiet
waituntil weekdaystr when while winactivate winclose wincoord winenabled
winexists winfocus winhide winmaximize winminimize winmove winowner winrestore
winshow winsize winstate wintask wintext wintoscreen wintouwu winvisible wizard
xfercancel xlatin xlatout xlatstr'''

KW_LIST['kwb'] = '''abortdnld abortretry access action actionbar adaptive19200
adaptiveans addcallinfo address adds60 adds90 adm31 adm3a adm5 alarmtime alt
altctrl altctrlshift alternate altshift always anonymouslogon ansibbs ansrings
append areacode ascii asciixlat aspdebug aspect aspectpath aspfile aspline
aspmenu aspversion att4410 att605 attribute auto autoansoff autoanswer autobaud
autodnld autologon autoreliable autosize autostart background backspace
baudrate begin betweencalls binary binarymode bit8mode bit8quote blankexpand
blinkrate block blockcheck blockcursor blockmode blockstart bold bottom
breaklen by callerid calleridoff calltype callwaiting callwaitoff cancel
cardnum cdinxfer cellular center character charpace charset chatmode cisb class
class1 class2 clipboard clipchar clipfilermv close closed cmdsuffix cnctmsg
code codepage colors columns com1 com2 com3 com4 com5 com6 com7 com8 com9
company complete completed connectall connected connection contents control
conventional converter countrycode coversheet cr crashrecover crc crc32 create
crlfxlat crlf_etx cr_lf cslipcompress ctrl ctrlquote ctrlshift current
cursorkeyapp cursorpos data database databits datafax datakey date dblclick dec
decimal declinewrap delay delete delline delpages dest device dgd100 dgd200
dgd210 dialacalways dialacforld dialcmd dialdir dialed dialentry dialingbox
dialog dialspeed dim direct disabled disk display distinctring dlgctrl dnld
dnldpath dnldprompt dnsaddress downto dropdown dropdownlist dropdtr duplex
dynamic echo ecm editor elapsed endsequence enquiry enquirystr entercrlf
enterkey entry entrynum environment eolchar eolconvert eolstr eot errorcorrect
errordetect escapem esprit3 etx even exact exclamation expand extended f0 f1 f2
f3 f4 f5 f6 f7 f8 f9 failure fast fax faxnumber file filelist filetype filexfer
filexferbox filter filtered finish first fixed flowcontrol flush font fontname
fontsize footer forever frame full global group half hardflow hardware header
heath19 helpfile hidden high hold homepage host hostdir hostprint hosttype
hotkeys hscroll html i0 i1 i2 i3 i4 i5 i6 i7 i8 i9 ibm3101 ibm3161 ibm3270
ibmpc iconflash iconpath inbox incnctlist incremental ind$file information init
insert internal internet intl intlprefix into ipaddress ipaddresstype ipport
iskey iso italic item keep kermit keyboardfile keypadapp keys l0 l1 l2 l3 l4 l5
l6 l7 l8 l9 landscape ldlineout ldprefix left length lf linepace linetype
linewrap lmouse local localdir locked loclineout logging logonname logontimeout
logout longdistance longfilename low lrecl ltime mail manager margins mark
masked matchcase maximized maxlength medium memload memo memory memtotal menu
metakeyfile metakeys method minimized misc miscnum mnp4 mnp5 mode modem
mousecoord multiline multiple multipleconnect music mvs_tso nameprefix
negotiate negotiation never newer news next no nocnctmsg noerrorcorrect
noncontig nondest none nopaint normal not notes notesfile notespath
nullsuppress numberprefix odd off offdial offset ok okcancel on once onuntilcd
onverify open options organization orientation origtime other outbox overwrite
pacechar pacelines pacing packetsize padchar padnum pagenumbers pageupdate
paging parent parity passivemode password path pattern pausechar permanent
phonecard phonenumber physical pinnum pixels playbackpace popup port portrait
ppp prefix print program prompt proprietary protect protectattr protocol pulse
pwmenu query question quickoption quickselect quiet raw rawascii rawprint read
readappend readwrite reboot receive received receiver recfm recordmode recvbaud
recvcmd recvprint recvview recycle relaxed remote remotecmd remove repaint
replyaddress reset restart restore resume retainfiles retries retrycancel
retrydelay reverse reversebit rgetchar right ringmsg rip rmouse rmvpolled rows
rxcr rxdata s0 s1 s2 s3 s4 s5 s6 s7 s7cmd s8 s9 save sbbuffer sbpages scale
scheduled screen scriptfile scriptpath scriptstart scroll scrollmethod search
security select send sendcmd sendcr sender sendpolled sent separator
serveraddress servicenum shared shift short showfaxstatus sierra signaturefile
simple single size skip slip slow softflow software sort space spawn speaker
stationid statusattr statusline stop stopbits streaming strip stripbit8 style
subnetmask success suffix suspend tabexpand tabkey tabstops target telnet
termcolors termfont terminal terminalid tight tiled time timeout timestamp
timing tone tooltips top topic translate tty turnchar tvi910 tvi912 tvi920
tvi922 tvi925 tvi950 tvi955 txmethod txpace type underline unselect until
update upld upldpace upldpath upto uselrecl usepacechar usephonecard userecfm
userexit userid username userwin us_cr uwus v23 v42 variable vidtex viewcursor
viewgif viewgraphics virtual visual vm_cms voice voicenumber volume vt100 vt102
vt220 vt320 vt52 waitcnct wavefile whensuspend whentarget wincolors window with
word write wyse100 wyse50 wyse60 wyse75 xfermode xferyield xmitbaud xmodem xoff
xwindow yes yesno yesnocancel ymodem ymodemg zmodem'''

KW_RE['kwb'] = "regex(\\$\\w+)"

STRINGDELIMITERS = "\" \'"

SL_COMMENT = ";"

ML_COMMENT = "#comment  #endcomment"

IGNORECASE = True

DIRECTIVE = "#"

ESCCHAR = "`"

SYMBOLS = "( ) [ ] { } , : & | < > !  = / *  %  + -"

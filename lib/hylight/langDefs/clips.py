# -*- coding: UTF-8 -*-
# Clips language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''and bind break defglobal deffunction evenp else eq floatpfloatp false
if integerp lexemep loop-for-count multifieldp neq not numberp or oddp pointerp
progn progn$ return stringp switch symbolp then true while'''

KW_LIST['kwb'] = '''acos acosh acot acoth acsc acsch asec asech asin asinh atan atanh
abs assert assert-string build create cos cosh cot coth csc csch close
call-next-method call-specific-method class class-abstractp class-existp
class-reactivep class-slots class-subclasses class-superclasses
call-next-handler delete deg-grad deg-rad div defgeneric-module duplicate
deftemplate-module defrule-module defglobal-module deffunction-module
dynamic-get dynamic-put direct-slot-delete direct-slot-insert
direct-slot-replace defclass-module definstances-module delete-instance eval
explode exp expand first float format fact-index
get-sequence-operator-recognition gensym get-function_restrictions grad-deg
get-defgeneric-list get-defmethod-list get-method-restrictions
get-deftemplate-list get-defrule-list get-defmodule-list get-defglobal-list
get-deffunction-list get-focus get-focus-stack get-defclass-list
get-defmessage-handler-list get-definstances-list implode insert integer
instance-addressp instance-existp instance-namep instancep init-slots
instance-address instance-name instance-name-to-symbol lowcase length length
log log10 member mod max min modify message-handler-existp nth next-handlerp
next-methodp open override-next-handler override-next-method pi printout
pop-focus replace rest random rad-deg round read readline remove rename retract
str-length sub-string sym-cat str-cat str-compare str-index
set-sequence-operator-recognition subseq subsetp seed setgen sec sech sin sinh
sec sech sin sinh sqrt slot-delete slot-insert slot-replace
symbol-to-instance-name slot-allowed-values slot-cardinality
slot-direct-accessp slot-existp slot-facets slot-initablep slot-publicp
slot-range slot-sources slot-types slot-writablep subclassp superclassp time
tan tanh type upcase unmake-instance app-create app-get-show-frame-on-init
app-on-init app-set-show-frame-on-init arc-annotation-get-name
arc-image-change-attachment arc-image-control-point-add
arc-image-control-point-count arc-image-control-point-move
arc-image-control-point-remove arc-image-control-point-x
arc-image-control-point-y arc-image-create arc-image-get-alignment-type
arc-image-get-attachment-from arc-image-get-attachment-to
arc-image-get-image-from arc-image-get-image-to arc-image-is-leg
arc-image-is-spline arc-image-is-stem arc-image-set-alignment-type
arc-image-set-spline batch begin-busy-cursor bell brush-create brush-delete
button-create button-create-from-bitmap bitmap-create bitmap-delete
bitmap-get-colourmap bitmap-get-height bitmap-get-width bitmap-load-from-file
canvas-scroll canvas-set-scroll-page-y canvas-set-scroll-pos-x
canvas-set-scroll-pos-y canvas-set-scroll-range-x canvas-set-scroll-range-y
canvas-view-start-x canvas-view-start-y card-create card-delete
card-deselect-all card-find-by-title card-get-canvas card-get-first-item
card-get-frame card-get-height card-get-next-item card-get-special-item
card-get-string-attribute card-get-toolbar card-get-width card-get-x card-get-y
card-iconize card-is-modified card-is-shown card-is-valid card-move card-quit
card-select-all card-send-command card-set-icon card-set-modified
card-set-status-text card-set-string-attribute card-show chdir clean-windows
clear-ide-window clear-resources copy-file cursor-create cursor-delete
cursor-load-from-file connection-advise connection-execute
connection-disconnect connection-poke connection-request
connection-start-advise connection-stop-advise client-create colour-create
colour-red colour-green colour-blue client-make-connection choice-create
choice-append choice-find-string choice-clear choice-get-selection
choice-get-string-selection choice-set-selection choice-set-string-selection
choice-get-string check-box-create check-box-set-value check-box-get-value
canvas-create canvas-get-dc canvas-get-scroll-page-x canvas-get-scroll-page-y
canvas-get-scroll-pos-x canvas-get-scroll-pos-y canvas-get-scroll-range-x
canvas-get-scroll-range-y canvas-get-scroll-pixels-per-unit-x
canvas-get-scroll-pixels-per-unit-x canvas-on-char canvas-on-scroll
canvas-set-scrollbars canvas-set-scroll-page-x container-region-add-node-image
container-region-remove-node-image convert-bitmap-to-rtf
convert-metafile-to-rtf database-close database-create database-delete
database-error-occurred database-get-data-source database-get-database-name
database-get-error-code database-get-error-message database-get-error-number
database-is-open database-open date-add-days date-add-months date-add-self
date-add-weeks date-add-years date-create date-create-julian date-create-string
date-delete date-eq date-format date-ge date-geq date-get-day
date-get-day-of-week date-get-day-of-week-name date-get-day-of-year
date-get-days-in-month date-get-first-day-of-month date-get-julian-date
date-get-month date-get-month-end date-get-month-name date-get-month-start
date-get-week-of-month date-get-week-of-year date-get-year date-get-year-end
date-get-year-start date-is-leap-year date-l date-leq date-neq
date-set-current-date date-set-date date-set-format date-set-julian
date-set-option date-subtract date-subtract-days date-subtract-self
dc-begin-drawing dc-blit dc-clear dc-delete dc-destroy-clipping-region
dc-draw-ellipse dc-draw-line dc-draw-lines dc-draw-point dc-draw-polygon
dc-draw-rectangle dc-draw-rounded-rectangle dc-draw-spline dc-draw-text
dc-end-doc dc-end-drawing dc-end-page dc-get-max-x dc-get-max-y dc-get-min-x
dc-get-min-y dc-get-text-extent-height dc-get-text-extent-width dc-ok
dc-set-background dc-set-background-mode dc-set-brush dc-set-clipping-region
dc-set-colourmap dc-set-font dc-set-logical-function dc-set-pen
dc-set-text-background dc-set-text-foreground dc-start-doc dc-start-page
dde-advise-global debug-msg diagram-card-clear-canvas diagram-card-copy
diagram-card-create diagram-card-create-expansion diagram-card-cut
diagram-card-delete-all-images diagram-card-find-root
diagram-card-get-first-arc-image diagram-card-get-first-arc-object
diagram-card-get-first-descendant diagram-card-get-first-node-image
diagram-card-get-first-node-object diagram-card-get-grid-spacing
diagram-card-get-next-arc-image diagram-card-get-next-arc-object
diagram-card-get-next-descendant diagram-card-get-next-node-image
diagram-card-get-next-node-object diagram-card-get-parent-card
diagram-card-get-parent-image diagram-card-get-print-height
diagram-card-get-print-width diagram-card-get-scale diagram-card-layout-graph
diagram-card-layout-tree diagram-card-load-file diagram-card-paste
diagram-card-popup-menu diagram-card-print-hierarchy diagram-card-redraw
diagram-card-save-bitmap diagram-card-save-file diagram-card-save-metafile
diagram-card-set-grid-spacing diagram-card-set-layout-parameters
diagram-card-set-scale diagram-image-add-annotation
diagram-image-annotation-get-drop-site
diagram-image-annotation-get-logical-name diagram-image-annotation-get-name
diagram-image-delete diagram-image-delete-annotation diagram-image-draw
diagram-image-draw-text diagram-image-erase diagram-image-get-brush-colour
diagram-image-get-card diagram-image-get-first-annotation
diagram-image-get-first-expansion diagram-image-get-height
diagram-image-get-item diagram-image-get-next-annotation
diagram-image-get-next-expansion diagram-image-get-object
diagram-image-get-pen-colour diagram-image-get-text-colour
diagram-image-get-width diagram-image-get-x diagram-image-get-y
diagram-image-is-shown diagram-image-move diagram-image-pending-delete
diagram-image-put-to-front diagram-image-resize diagram-image-select
diagram-image-selected diagram-image-set-brush-colour
diagram-image-set-pen-colour diagram-image-set-shadow-mode
diagram-image-set-text-colour diagram-image-show diagram-item-get-image
diagram-object-add-attribute diagram-object-delete-attribute
diagram-object-format-text diagram-object-get-first-attribute
diagram-object-get-first-image diagram-object-get-next-attribute
diagram-object-get-next-image diagram-object-get-string-attribute
diagram-object-set-format-string diagram-object-set-string-attribute
diagram-palette-get-arc-selection diagram-palette-get-arc-selection-image
diagram-palette-get-first-annotation-selection
diagram-palette-get-next-annotation-selection
diagram-palette-get-node-selection diagram-palette-set-annotation-selection
diagram-palette-set-arc-selection diagram-palette-set-node-selection
diagram-palette-show dialog-box-create dialog-box-create-from-resource
dialog-box-is-modal dialog-box-set-modal dir-exists end-busy-cursor
event-get-event-type execute file-exists file-selector find-window-by-label
find-window-by-name float-to-string font-create font-delete frame-create
frame-create-status-line frame-iconize frame-on-size frame-set-icon
frame-set-menu-bar frame-set-status-text frame-set-title frame-set-tool-bar
gauge-create gauge-set-bezel-face gauge-set-shadow-width gauge-set-value
get-active-window get-choice get-elapsed-time get-ide-window get-os-version
get-platform get-resource get-text-from-user grid-adjust-scrollbars
grid-append-cols grid-append-rows grid-clear-grid grid-create grid-create-grid
grid-delete-cols grid-delete-rows grid-get-cell-alignment
grid-get-cell-background-colour grid-get-cell-bitmap grid-get-cell-text-colour
grid-get-cell-value grid-get-cols grid-get-column-width grid-get-cursor-column
grid-get-cursor-row grid-get-editable grid-get-label-alignment
grid-get-label-background-colour grid-get-label-size grid-get-label-text-colour
grid-get-label-value grid-get-row-height grid-get-rows grid-get-scroll-pos-x
grid-get-scroll-pos-y grid-get-text-item grid-insert-cols grid-insert-rows
grid-on-activate grid-on-paint grid-on-size grid-set-cell-alignment
grid-set-cell-background-colour grid-set-cell-bitmap grid-set-cell-text-colour
grid-set-cell-text-font grid-set-cell-value grid-set-column-width
grid-set-divider-pen grid-set-editable grid-set-grid-cursor
grid-set-label-alignment grid-set-label-background-colour grid-set-label-size
grid-set-label-text-colour grid-set-label-text-font grid-set-label-value
grid-set-row-height grid-update-dimensions group-box-create hardy-clear-index
hardy-command-int-to-string hardy-command-string-to-int
hardy-diagram-definition-get-first-arc-type
hardy-diagram-definition-get-first-node-type
hardy-diagram-definition-get-next-arc-type
hardy-diagram-definition-get-next-node-type hardy-get-browser-frame
hardy-get-first-card  hardy-get-first-diagram-definition hardy-get-next-card 
hardy-get-next-diagram-definition hardy-get-top-card  hardy-get-top-level-frame
hardy-get-version hardy-help-display-block hardy-help-display-contents
hardy-help-display-section hardy-help-keyword-search hardy-help-load-file
hardy-load-index  hardy-path-search hardy-preview-all
hardy-preview-diagram-card hardy-print-all hardy-print-diagram-card
hardy-print-diagram-in-box hardy-print-diagram-page
hardy-print-get-header-footer hardy-print-get-info hardy-print-header-footer
hardy-print-set-header-footer hardy-print-set-info hardy-print-set-title
hardy-print-text-in-box hardy-save-index hardy-send-command
hardy-set-about-string hardy-set-author hardy-set-custom-help-file
hardy-set-help-file hardy-set-name hardy-set-title help-create help-delete
help-display-block help-display-contents help-display-section
help-keyword-search help-load-file html-back html-cancel html-clear-cache
html-create html-get-current-url html-on-size html-open-file html-open-url
html-resize html-save-file hwnd-find hwnd-iconize hwnd-move hwnd-quit
hwnd-refresh hwnd-send-message hwnd-show hypertext-block-add
hypertext-block-clear hypertext-block-get-item hypertext-block-get-text
hypertext-block-get-type hypertext-block-selected hypertext-block-set-type
hypertext-card-create hypertext-card-get-current-char
hypertext-card-get-current-line hypertext-card-get-first-selection
hypertext-card-get-line-length hypertext-card-get-next-selection
hypertext-card-get-no-lines hypertext-card-get-offset-position
hypertext-card-get-span-text hypertext-card-insert-text
hypertext-card-load-file hypertext-card-save-file hypertext-card-string-search
hypertext-card-translate hypertext-card-translator-close-file
hypertext-card-translator-open-file hypertext-card-translator-output
hypertext-item-get-block icon-create icon-delete icon-get-height icon-get-width
icon-load-from-file instance-table-add-entry instance-table-delete-entry
instance-table-get-instance item-get-first-link item-get-kind
item-get-next-link item-get-type item-goto item-set-kind key-event-alt-down
key-event-control-down key-event-get-key-code key-event-position-x
key-event-position-y key-event-shift-down link-cards link-get-card-from
link-get-card-to link-get-item-from link-get-item-to link-get-kind
link-get-type link-items link-set-kind list-box-append list-box-clear
list-box-create list-box-delete list-box-find-string
list-box-get-first-selection list-box-get-next-selection list-box-get-selection
list-box-get-string list-box-get-string-selection list-box-number
list-box-set-selection list-box-set-string-selection load-resource-file
long-to-string make-metafile-placeable mci-send-string media-block-create
media-block-get-item media-block-get-position media-block-get-type
media-block-set-type media-card-append-text media-card-apply-family
media-card-apply-foreground-colour media-card-apply-point-size
media-card-apply-style media-card-apply-underline media-card-apply-weight
media-card-clear media-card-clear-all-blocks media-card-copy media-card-create
media-card-cut media-card-delete media-card-find-string
media-card-get-character media-card-get-first-block
media-card-get-last-position media-card-get-line-for-position
media-card-get-line-length media-card-get-next-block
media-card-get-number-of-lines media-card-get-position-for-line
media-card-get-selection-end media-card-get-selection-start media-card-get-text
media-card-insert-image media-card-insert-text media-card-load-file
media-card-paste media-card-redo media-card-save-file
media-card-scroll-to-position media-card-select-block media-card-set-selection
media-card-undo media-item-get-block memory-dc-create memory-dc-select-object
menu-append menu-append-separator menu-bar-append menu-bar-check
menu-bar-checked menu-bar-create menu-bar-enable menu-break menu-check
menu-create menu-enable message-box message-create message-create-from-bitmap
metafile-dc-close metafile-dc-create metafile-delete metafile-set-clipboard
mkdir mouse-event-button mouse-event-button-down mouse-event-control-down
mouse-event-dragging mouse-event-is-button mouse-event-left-down
mouse-event-left-up mouse-event-middle-down mouse-event-middle-up
mouse-event-position-x mouse-event-position-y mouse-event-right-down
mouse-event-right-up mouse-event-shift-down multi-text-copy multi-text-create
multi-text-cut multi-text-get-insertion-point multi-text-get-last-position
multi-text-get-line-length multi-text-get-line-length
multi-text-get-number-of-lines multi-text-get-value multi-text-paste
multi-text-position-to-char multi-text-position-to-line multi-text-remove
multi-text-replace multi-text-set-insertion-point multi-text-set-selection
multi-text-set-value multi-text-show-position multi-text-write
multi-text-xy-to-position node-image-create node-image-duplicate
node-image-get-container node-image-get-container-parent
node-image-get-first-arc-image node-image-get-first-child
node-image-get-first-container-region node-image-get-next-arc-image
node-image-get-next-child node-image-get-next-container-region
node-image-get-parent node-image-is-composite node-image-is-container
node-image-is-junction node-image-order-arcs node-object-get-first-arc-object
node-object-get-next-arc-object now object-get-type object-is-valid
object-type-get-first-attribute-name object-type-get-next-attribute-name
panel-create panel-create-from-resource panel-item-get-command-event
panel-item-get-label panel-item-set-default panel-item-set-label panel-new-line
panel-set-button-font panel-set-label-font panel-set-label-position pen-create
pen-delete postscript-dc-create printer-dc-create quit radio-box-create
radio-box-get-selection radio-box-set-selection read-string recordset-create
recordset-delete recordset-execute-sql recordset-get-char-data
recordset-get-col-name recordset-get-col-type recordset-get-columns
recordset-get-data-sources recordset-get-database recordset-get-error-code
recordset-get-filter recordset-get-float-data recordset-get-foreign-keys
recordset-get-int-data recordset-get-number-cols recordset-get-number-fields
recordset-get-number-params recordset-get-number-records
recordset-get-primary-keys recordset-get-result-set recordset-get-table-name
recordset-get-tables recordset-goto recordset-is-bof recordset-is-col-nullable
recordset-is-eof recordset-is-field-dirty recordset-is-field-null
recordset-is-open recordset-move recordset-move-first recordset-move-last
recordset-move-next recordset-move-prev recordset-query
recordset-set-table-name register-event-handler return-result rmdir
server-create set-work-proc show-ide-window sleep slider-create
slider-get-value slider-set-value start-timer string-sort string-to-float
string-to-long string-to-symbol symbol-to-string text-card-load-file
text-create text-get-value text-set-value text-window-clear text-window-copy
text-window-create text-window-cut text-window-discard-edits
text-window-get-contents text-window-get-insertion-point
text-window-get-last-position text-window-get-line-length
text-window-get-line-length text-window-get-number-of-lines
text-window-load-file text-window-modified text-window-on-char
text-window-paste text-window-position-to-char text-window-position-to-line
text-window-remove text-window-replace text-window-save-file
text-window-set-editable text-window-set-insertion-point
text-window-set-selection text-window-show-position text-window-write
text-window-xy-to-position timer-create timer-delete timer-start timer-stop
toolbar-add-separator toolbar-add-tool toolbar-clear-tools toolbar-create
toolbar-create-tools toolbar-enable-tool toolbar-get-max-height
toolbar-get-max-width toolbar-get-tool-client-data toolbar-get-tool-enabled
toolbar-get-tool-long-help toolbar-get-tool-short-help toolbar-get-tool-state
toolbar-layout toolbar-on-paint toolbar-set-default-size toolbar-set-margins
toolbar-set-tool-long-help toolbar-set-tool-short-help toolbar-toggle-tool
window-add-callback window-centre window-close window-delete window-enable
window-fit window-get-client-height window-get-client-width window-get-height
window-get-name window-get-next-child window-get-parent window-get-width
window-get-x window-get-y window-is-shown window-make-modal window-popup-menu
window-refresh window-remove-callback window-set-client-size window-set-cursor
window-set-focus window-set-size window-set-size-hints window-show
write-resource wxclips-object-exists yield carddelete carddeletealllinks
carddeletelink cardeditfilename cardedittitle cardgotocontrolwindow
cardlinknewcard cardlinktoselection cardopenfile cardorderlinks cardquit
cardsavefile cardsavefileas cardselectitem cardtogglelinkpanel
diagramaddannotation diagramaddcontrol diagramapplydefinition diagrambrowse
diagramchangefont diagramclearall diagramcopy diagramcopydiagram
diagramcopyselection diagramcopytoclipboard diagramcut diagramdeleteannotation
diagramdeletecontrol diagramdeselectall diagramduplicateselection
diagrameditoptions diagramformatgraph diagramformattext diagramformattree
diagramgotoroot diagramhelp diagramhorizontalalign diagramhorizontalalignbottom
diagramhorizontalaligntop diagramnewexpansion diagrampaste diagramprint
diagramprintall diagramprinteps diagramprintpreview diagramrefresh
diagramsavebitmap diagramsavemetafile diagramselectall diagramstraighten
diagramtoback diagramtofront diagramtogglepalette diagramtoggletoolbar
diagramverticalalign diagramverticalalignleft diagramverticalalignright
diagramzoom100 diagramzoom30 diagramzoom40 diagramzoom50 diagramzoom60
diagramzoom70 diagramzoom80 diagramzoom90 hardybrowsefiles hardyclearindex
hardyconfigure hardydeselectallitems hardydrawtree hardyexit hardyfindorphans
hardyhelpabout hardyhelpcontents hardyhelpsearch hardyloadapplication
hardyloadfile hardyprint hardyprintpreview hardyprintsetup hardysavefile
hardysavefileas hardysearchcards hardyshowarcsymboleditor
hardyshowdevelopmentwindow hardyshowdiagrammanager hardyshowhypertextmanager
hardyshownodesymboleditor hardyshowpackagetool hardyshowsymbollibrarian
hardyviewtopcard create cos cosh cot coth csc csch close call-next-method
call-specific-method class class-abstractp class-existp class-reactivep
class-slots class-subclasses class-superclasses call-next-handler delete
deg-grad deg-rad div defgeneric-module duplicate deftemplate-module
defrule-module defglobal-module deffunction-module dynamic-get dynamic-put
direct-slot-delete direct-slot-insert direct-slot-replace defclass-module
definstances-module delete-instance eval explode exp expand first float format
fact-index get-sequence-operator-recognition gensym get-function_restrictions
grad-deg get-defgeneric-list get-defmethod-list get-method-restrictions
get-deftemplate-list get-defrule-list get-defmodule-list get-defglobal-list
get-deffunction-list get-focus get-focus-stack get-defclass-list
get-defmessage-handler-list get-definstances-list implode insert integer
instance-addressp instance-existp instance-namep instancep init-slots
instance-address instance-name instance-name-to-symbol lowcase length length
log log10 member mod max min modify message-handler-existp nth next-handlerp
next-methodp open override-next-handler override-next-method pi printout
pop-focus replace rest random rad-deg round read readline remove rename retract
str-length sub-string sym-cat str-cat str-compare str-index
set-sequence-operator-recognition subseq subsetp seed setgen sec sech sin sinh
sec sech sin sinh sqrt slot-delete slot-insert slot-replace
symbol-to-instance-name slot-allowed-values slot-cardinality
slot-direct-accessp slot-existp slot-facets slot-initablep slot-publicp
slot-range slot-sources slot-types slot-writablep subclassp superclassp time
tan tanh type upcase unmake-instance app-create app-get-show-frame-on-init
app-on-init app-set-show-frame-on-init arc-annotation-get-name
arc-image-change-attachment arc-image-control-point-add
arc-image-control-point-count arc-image-control-point-move
arc-image-control-point-remove arc-image-control-point-x
arc-image-control-point-y arc-image-create arc-image-get-alignment-type
arc-image-get-attachment-from arc-image-get-attachment-to
arc-image-get-image-from arc-image-get-image-to arc-image-is-leg
arc-image-is-spline arc-image-is-stem arc-image-set-alignment-type
arc-image-set-spline batch begin-busy-cursor bell brush-create brush-delete
button-create button-create-from-bitmap bitmap-create bitmap-delete
bitmap-get-colourmap bitmap-get-height bitmap-get-width bitmap-load-from-file
canvas-scroll canvas-set-scroll-page-y canvas-set-scroll-pos-x
canvas-set-scroll-pos-y canvas-set-scroll-range-x canvas-set-scroll-range-y
canvas-view-start-x canvas-view-start-y card-create card-delete
card-deselect-all card-find-by-title card-get-canvas card-get-first-item
card-get-frame card-get-height card-get-next-item card-get-special-item
card-get-string-attribute card-get-toolbar card-get-width card-get-x card-get-y
card-iconize card-is-modified card-is-shown card-is-valid card-move card-quit
card-select-all card-send-command card-set-icon card-set-modified
card-set-status-text card-set-string-attribute card-show chdir clean-windows
clear-ide-window clear-resources copy-file cursor-create cursor-delete
cursor-load-from-file connection-advise connection-execute
connection-disconnect connection-poke connection-request
connection-start-advise connection-stop-advise client-create colour-create
colour-red colour-green colour-blue client-make-connection choice-create
choice-append choice-find-string choice-clear choice-get-selection
choice-get-string-selection choice-set-selection choice-set-string-selection
choice-get-string check-box-create check-box-set-value check-box-get-value
canvas-create canvas-get-dc canvas-get-scroll-page-x canvas-get-scroll-page-y
canvas-get-scroll-pos-x canvas-get-scroll-pos-y canvas-get-scroll-range-x
canvas-get-scroll-range-y canvas-get-scroll-pixels-per-unit-x
canvas-get-scroll-pixels-per-unit-x canvas-on-char canvas-on-scroll
canvas-set-scrollbars canvas-set-scroll-page-x container-region-add-node-image
container-region-remove-node-image convert-bitmap-to-rtf
convert-metafile-to-rtf database-close database-create database-delete
database-error-occurred database-get-data-source database-get-database-name
database-get-error-code database-get-error-message database-get-error-number
database-is-open database-open date-add-days date-add-months date-add-self
date-add-weeks date-add-years date-create date-create-julian date-create-string
date-delete date-eq date-format date-ge date-geq date-get-day
date-get-day-of-week date-get-day-of-week-name date-get-day-of-year
date-get-days-in-month date-get-first-day-of-month date-get-julian-date
date-get-month date-get-month-end date-get-month-name date-get-month-start
date-get-week-of-month date-get-week-of-year date-get-year date-get-year-end
date-get-year-start date-is-leap-year date-l date-leq date-neq
date-set-current-date date-set-date date-set-format date-set-julian
date-set-option date-subtract date-subtract-days date-subtract-self
dc-begin-drawing dc-blit dc-clear dc-delete dc-destroy-clipping-region
dc-draw-ellipse dc-draw-line dc-draw-lines dc-draw-point dc-draw-polygon
dc-draw-rectangle dc-draw-rounded-rectangle dc-draw-spline dc-draw-text
dc-end-doc dc-end-drawing dc-end-page dc-get-max-x dc-get-max-y dc-get-min-x
dc-get-min-y dc-get-text-extent-height dc-get-text-extent-width dc-ok
dc-set-background dc-set-background-mode dc-set-brush dc-set-clipping-region
dc-set-colourmap dc-set-font dc-set-logical-function dc-set-pen
dc-set-text-background dc-set-text-foreground dc-start-doc dc-start-page
dde-advise-global debug-msg diagram-card-clear-canvas diagram-card-copy
diagram-card-create diagram-card-create-expansion diagram-card-cut
diagram-card-delete-all-images diagram-card-find-root
diagram-card-get-first-arc-image diagram-card-get-first-arc-object
diagram-card-get-first-descendant diagram-card-get-first-node-image
diagram-card-get-first-node-object diagram-card-get-grid-spacing
diagram-card-get-next-arc-image diagram-card-get-next-arc-object
diagram-card-get-next-descendant diagram-card-get-next-node-image
diagram-card-get-next-node-object diagram-card-get-parent-card
diagram-card-get-parent-image diagram-card-get-print-height
diagram-card-get-print-width diagram-card-get-scale diagram-card-layout-graph
diagram-card-layout-tree diagram-card-load-file diagram-card-paste
diagram-card-popup-menu diagram-card-print-hierarchy diagram-card-redraw
diagram-card-save-bitmap diagram-card-save-file diagram-card-save-metafile
diagram-card-set-grid-spacing diagram-card-set-layout-parameters
diagram-card-set-scale diagram-image-add-annotation
diagram-image-annotation-get-drop-site
diagram-image-annotation-get-logical-name diagram-image-annotation-get-name
diagram-image-delete diagram-image-delete-annotation diagram-image-draw
diagram-image-draw-text diagram-image-erase diagram-image-get-brush-colour
diagram-image-get-card diagram-image-get-first-annotation
diagram-image-get-first-expansion diagram-image-get-height
diagram-image-get-item diagram-image-get-next-annotation
diagram-image-get-next-expansion diagram-image-get-object
diagram-image-get-pen-colour diagram-image-get-text-colour
diagram-image-get-width diagram-image-get-x diagram-image-get-y
diagram-image-is-shown diagram-image-move diagram-image-pending-delete
diagram-image-put-to-front diagram-image-resize diagram-image-select
diagram-image-selected diagram-image-set-brush-colour
diagram-image-set-pen-colour diagram-image-set-shadow-mode
diagram-image-set-text-colour diagram-image-show diagram-item-get-image
diagram-object-add-attribute diagram-object-delete-attribute
diagram-object-format-text diagram-object-get-first-attribute
diagram-object-get-first-image diagram-object-get-next-attribute
diagram-object-get-next-image diagram-object-get-string-attribute
diagram-object-set-format-string diagram-object-set-string-attribute
diagram-palette-get-arc-selection diagram-palette-get-arc-selection-image
diagram-palette-get-first-annotation-selection
diagram-palette-get-next-annotation-selection
diagram-palette-get-node-selection diagram-palette-set-annotation-selection
diagram-palette-set-arc-selection diagram-palette-set-node-selection
diagram-palette-show dialog-box-create dialog-box-create-from-resource
dialog-box-is-modal dialog-box-set-modal dir-exists end-busy-cursor
event-get-event-type execute file-exists file-selector find-window-by-label
find-window-by-name float-to-string font-create font-delete frame-create
frame-create-status-line frame-iconize frame-on-size frame-set-icon
frame-set-menu-bar frame-set-status-text frame-set-title frame-set-tool-bar
gauge-create gauge-set-bezel-face gauge-set-shadow-width gauge-set-value
get-active-window get-choice get-elapsed-time get-ide-window get-os-version
get-platform get-resource get-text-from-user grid-adjust-scrollbars
grid-append-cols grid-append-rows grid-clear-grid grid-create grid-create-grid
grid-delete-cols grid-delete-rows grid-get-cell-alignment
grid-get-cell-background-colour grid-get-cell-bitmap grid-get-cell-text-colour
grid-get-cell-value grid-get-cols grid-get-column-width grid-get-cursor-column
grid-get-cursor-row grid-get-editable grid-get-label-alignment
grid-get-label-background-colour grid-get-label-size grid-get-label-text-colour
grid-get-label-value grid-get-row-height grid-get-rows grid-get-scroll-pos-x
grid-get-scroll-pos-y grid-get-text-item grid-insert-cols grid-insert-rows
grid-on-activate grid-on-paint grid-on-size grid-set-cell-alignment
grid-set-cell-background-colour grid-set-cell-bitmap grid-set-cell-text-colour
grid-set-cell-text-font grid-set-cell-value grid-set-column-width
grid-set-divider-pen grid-set-editable grid-set-grid-cursor
grid-set-label-alignment grid-set-label-background-colour grid-set-label-size
grid-set-label-text-colour grid-set-label-text-font grid-set-label-value
grid-set-row-height grid-update-dimensions group-box-create hardy-clear-index
hardy-command-int-to-string hardy-command-string-to-int
hardy-diagram-definition-get-first-arc-type
hardy-diagram-definition-get-first-node-type
hardy-diagram-definition-get-next-arc-type
hardy-diagram-definition-get-next-node-type hardy-get-browser-frame
hardy-get-first-card  hardy-get-first-diagram-definition hardy-get-next-card 
hardy-get-next-diagram-definition hardy-get-top-card  hardy-get-top-level-frame
hardy-get-version hardy-help-display-block hardy-help-display-contents
hardy-help-display-section hardy-help-keyword-search hardy-help-load-file
hardy-load-index  hardy-path-search hardy-preview-all
hardy-preview-diagram-card hardy-print-all hardy-print-diagram-card
hardy-print-diagram-in-box hardy-print-diagram-page
hardy-print-get-header-footer hardy-print-get-info hardy-print-header-footer
hardy-print-set-header-footer hardy-print-set-info hardy-print-set-title
hardy-print-text-in-box hardy-save-index hardy-send-command
hardy-set-about-string hardy-set-author hardy-set-custom-help-file
hardy-set-help-file hardy-set-name hardy-set-title help-create help-delete
help-display-block help-display-contents help-display-section
help-keyword-search help-load-file html-back html-cancel html-clear-cache
html-create html-get-current-url html-on-size html-open-file html-open-url
html-resize html-save-file hwnd-find hwnd-iconize hwnd-move hwnd-quit
hwnd-refresh hwnd-send-message hwnd-show hypertext-block-add
hypertext-block-clear hypertext-block-get-item hypertext-block-get-text
hypertext-block-get-type hypertext-block-selected hypertext-block-set-type
hypertext-card-create hypertext-card-get-current-char
hypertext-card-get-current-line hypertext-card-get-first-selection
hypertext-card-get-line-length hypertext-card-get-next-selection
hypertext-card-get-no-lines hypertext-card-get-offset-position
hypertext-card-get-span-text hypertext-card-insert-text
hypertext-card-load-file hypertext-card-save-file hypertext-card-string-search
hypertext-card-translate hypertext-card-translator-close-file
hypertext-card-translator-open-file hypertext-card-translator-output
hypertext-item-get-block icon-create icon-delete icon-get-height icon-get-width
icon-load-from-file instance-table-add-entry instance-table-delete-entry
instance-table-get-instance item-get-first-link item-get-kind
item-get-next-link item-get-type item-goto item-set-kind key-event-alt-down
key-event-control-down key-event-get-key-code key-event-position-x
key-event-position-y key-event-shift-down link-cards link-get-card-from
link-get-card-to link-get-item-from link-get-item-to link-get-kind
link-get-type link-items link-set-kind list-box-append list-box-clear
list-box-create list-box-delete list-box-find-string
list-box-get-first-selection list-box-get-next-selection list-box-get-selection
list-box-get-string list-box-get-string-selection list-box-number
list-box-set-selection list-box-set-string-selection load-resource-file
long-to-string make-metafile-placeable mci-send-string media-block-create
media-block-get-item media-block-get-position media-block-get-type
media-block-set-type media-card-append-text media-card-apply-family
media-card-apply-foreground-colour media-card-apply-point-size
media-card-apply-style media-card-apply-underline media-card-apply-weight
media-card-clear media-card-clear-all-blocks media-card-copy media-card-create
media-card-cut media-card-delete media-card-find-string
media-card-get-character media-card-get-first-block
media-card-get-last-position media-card-get-line-for-position
media-card-get-line-length media-card-get-next-block
media-card-get-number-of-lines media-card-get-position-for-line
media-card-get-selection-end media-card-get-selection-start media-card-get-text
media-card-insert-image media-card-insert-text media-card-load-file
media-card-paste media-card-redo media-card-save-file
media-card-scroll-to-position media-card-select-block media-card-set-selection
media-card-undo media-item-get-block memory-dc-create memory-dc-select-object
menu-append menu-append-separator menu-bar-append menu-bar-check
menu-bar-checked menu-bar-create menu-bar-enable menu-break menu-check
menu-create menu-enable message-box message-create message-create-from-bitmap
metafile-dc-close metafile-dc-create metafile-delete metafile-set-clipboard
mkdir mouse-event-button mouse-event-button-down mouse-event-control-down
mouse-event-dragging mouse-event-is-button mouse-event-left-down
mouse-event-left-up mouse-event-middle-down mouse-event-middle-up
mouse-event-position-x mouse-event-position-y mouse-event-right-down
mouse-event-right-up mouse-event-shift-down multi-text-copy multi-text-create
multi-text-cut multi-text-get-insertion-point multi-text-get-last-position
multi-text-get-line-length multi-text-get-line-length
multi-text-get-number-of-lines multi-text-get-value multi-text-paste
multi-text-position-to-char multi-text-position-to-line multi-text-remove
multi-text-replace multi-text-set-insertion-point multi-text-set-selection
multi-text-set-value multi-text-show-position multi-text-write
multi-text-xy-to-position node-image-create node-image-duplicate
node-image-get-container node-image-get-container-parent
node-image-get-first-arc-image node-image-get-first-child
node-image-get-first-container-region node-image-get-next-arc-image
node-image-get-next-child node-image-get-next-container-region
node-image-get-parent node-image-is-composite node-image-is-container
node-image-is-junction node-image-order-arcs node-object-get-first-arc-object
node-object-get-next-arc-object now object-get-type object-is-valid
object-type-get-first-attribute-name object-type-get-next-attribute-name
panel-create panel-create-from-resource panel-item-get-command-event
panel-item-get-label panel-item-set-default panel-item-set-label panel-new-line
panel-set-button-font panel-set-label-font panel-set-label-position pen-create
pen-delete postscript-dc-create printer-dc-create quit radio-box-create
radio-box-get-selection radio-box-set-selection read-string recordset-create
recordset-delete recordset-execute-sql recordset-get-char-data
recordset-get-col-name recordset-get-col-type recordset-get-columns
recordset-get-data-sources recordset-get-database recordset-get-error-code
recordset-get-filter recordset-get-float-data recordset-get-foreign-keys
recordset-get-int-data recordset-get-number-cols recordset-get-number-fields
recordset-get-number-params recordset-get-number-records
recordset-get-primary-keys recordset-get-result-set recordset-get-table-name
recordset-get-tables recordset-goto recordset-is-bof recordset-is-col-nullable
recordset-is-eof recordset-is-field-dirty recordset-is-field-null
recordset-is-open recordset-move recordset-move-first recordset-move-last
recordset-move-next recordset-move-prev recordset-query
recordset-set-table-name register-event-handler return-result rmdir
server-create set-work-proc show-ide-window sleep slider-create
slider-get-value slider-set-value start-timer string-sort string-to-float
string-to-long string-to-symbol symbol-to-string text-card-load-file
text-create text-get-value text-set-value text-window-clear text-window-copy
text-window-create text-window-cut text-window-discard-edits
text-window-get-contents text-window-get-insertion-point
text-window-get-last-position text-window-get-line-length
text-window-get-line-length text-window-get-number-of-lines
text-window-load-file text-window-modified text-window-on-char
text-window-paste text-window-position-to-char text-window-position-to-line
text-window-remove text-window-replace text-window-save-file
text-window-set-editable text-window-set-insertion-point
text-window-set-selection text-window-show-position text-window-write
text-window-xy-to-position timer-create timer-delete timer-start timer-stop
toolbar-add-separator toolbar-add-tool toolbar-clear-tools toolbar-create
toolbar-create-tools toolbar-enable-tool toolbar-get-max-height
toolbar-get-max-width toolbar-get-tool-client-data toolbar-get-tool-enabled
toolbar-get-tool-long-help toolbar-get-tool-short-help toolbar-get-tool-state
toolbar-layout toolbar-on-paint toolbar-set-default-size toolbar-set-margins
toolbar-set-tool-long-help toolbar-set-tool-short-help toolbar-toggle-tool
window-add-callback window-centre window-close window-delete window-enable
window-fit window-get-client-height window-get-client-width window-get-height
window-get-name window-get-next-child window-get-parent window-get-width
window-get-x window-get-y window-is-shown window-make-modal window-popup-menu
window-refresh window-remove-callback window-set-client-size window-set-cursor
window-set-focus window-set-size window-set-size-hints window-show
write-resource wxclips-object-exists yield carddelete carddeletealllinks
carddeletelink cardeditfilename cardedittitle cardgotocontrolwindow
cardlinknewcard cardlinktoselection cardopenfile cardorderlinks cardquit
cardsavefile cardsavefileas cardselectitem cardtogglelinkpanel
diagramaddannotation diagramaddcontrol diagramapplydefinition diagrambrowse
diagramchangefont diagramclearall diagramcopy diagramcopydiagram
diagramcopyselection diagramcopytoclipboard diagramcut diagramdeleteannotation
diagramdeletecontrol diagramdeselectall diagramduplicateselection
diagrameditoptions diagramformatgraph diagramformattext diagramformattree
diagramgotoroot diagramhelp diagramhorizontalalign diagramhorizontalalignbottom
diagramhorizontalaligntop diagramnewexpansion diagrampaste diagramprint
diagramprintall diagramprinteps diagramprintpreview diagramrefresh
diagramsavebitmap diagramsavemetafile diagramselectall diagramstraighten
diagramtoback diagramtofront diagramtogglepalette diagramtoggletoolbar
diagramverticalalign diagramverticalalignleft diagramverticalalignright
diagramzoom100 diagramzoom30 diagramzoom40 diagramzoom50 diagramzoom60
diagramzoom70 diagramzoom80 diagramzoom90 hardybrowsefiles hardyclearindex
hardyconfigure hardydeselectallitems hardydrawtree hardyexit hardyfindorphans
hardyhelpabout hardyhelpcontents hardyhelpsearch hardyloadapplication
hardyloadfile hardyprint hardyprintpreview hardyprintsetup hardysavefile
hardysavefileas hardysearchcards hardyshowarcsymboleditor
hardyshowdevelopmentwindow hardyshowdiagrammanager hardyshowhypertextmanager
hardyshownodesymboleditor hardyshowpackagetool hardyshowsymbollibrarian
hardyviewtopcard'''

STRINGDELIMITERS = "\""

ESCCHAR = "\\"

SL_COMMENT = ";"

ML_COMMENT = "/* */"

IGNORECASE = True

IDENTIFIER = "regex([a-zA-Z_][\\w\\-]*)"

SYMBOLS = "( ) [ ] { } , ; : & | < > !  = / *  %  + -"



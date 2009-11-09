# -*- coding: UTF-8 -*-
# Blitz Basic 3D language definition file
#
# This file was taken from Andre Simon's fantastic
# syntax-highlighter "highlight" (www.andre-simon.de).

KW_LIST = {}
KW_RE = {}

KW_LIST['kwa'] = '''after and before case const data default delete dim each else elseif end endif
exit false field first for forever function global gosub goto handle if include insert
last local new next not null object or read repeat restore return select step then to
true type until wend while'''

KW_LIST['kwb'] = '''acos asin atan atan2 abs accepttcpstream apptitle asc
automidhandle availvidmem backbuffer banksize bin ceil changedir channelpan channelpitch
channelplaying channelvolume chr closedir closefile closetcpserver closetcpstream cls
clscolor color colorblue colorgreen colorred commandline copybank copyfile copyimage
copypixel copypixelfast copyrect copystream cos countgfxdrivers countgfxmodes createbank
createdir createimage createnetplayer createtcpserver createtimer currentdate currentdir
currenttime debuglog delay deletedir deletefile deletenetplayer drawblock drawblockrect
drawimage drawimagerect eof execfile exp filepos filesize filetype flip float floor
flushjoy flushkeys flushmouse fontheight fontwidth freebank freefont freeimage freesound
freetimer frontbuffer getcolor getjoy getkey getmouse gfxdrivername gfxmodedepth
gfxmodeexists gfxmodeheight gfxmodewidth grabimage graphics graphicsbuffer graphicsdepth
graphicsheight graphicswidth handleimage hex hidepointer hostnetgame imagebuffer
imageheight imagerectcollide imagerectoverlap imagewidth imagexhandle imageyhandle
imagescollide imagesoverlap input instr int joinnetgame joyhit joytype joyx joyy joyz
keydown keyhit left len line loadanimimage loadbuffer loadfont loadimage loadsound
lockbuffer log log10 loopsound lower lset maskimage mid midhandle millisecs mod
mousedown mousehit mousex mousexspeed mousey mouseyspeed mousez mousezspeed movemouse
netmsgdata netmsgfrom netmsgto netmsgtype netplayerlocal netplayername nextfile openfile
opentcpstream origin oval pausechannel peekbyte peekfloat peekint peekshort pi
playcdtrack playmusic playsound plot pokebyte pokefloat pokeint pokeshort print rset
rand readavail readbyte readbytes readdir readfile readfloat readint readline readpixel
readpixelfast readshort readstring rect rectsoverlap recvnetmsg replace resizebank
resizeimage resumechannel right rnd rotateimage runtimeerror sar savebuffer saveimage
scaleimage scanline seedrand seekfile setbuffer setfont setgfxdriver setnetmsg sgn shl
showpointer shr sin soundpan soundpitch soundvolume sqr startnetgame stop stopchannel
stopnetgame str string stringheight stringwidth tcptimeouts tformfilter tformimage tan
text tileblock tileimage totalvidmem trim unlockbuffer upper vwait viewport waitjoy
waitkey waitmouse waittimer write writebyte writebytes writefile writefloat writeint
writeline writepixel writepixelfast writeshort writestring xor addanimseq addtriangle
addvertex aligntovector ambientlight animate animatemd2 animating animlength animseq
animtime antialias brushalpha brushblend brushcolor brushfx brushshininess brushtexture
cameraclscolor cameraclsmode camerafogcolor camerafogmode camerafogrange camerapick
cameraproject camerarange cameraviewport camerazoom captureworld clearcollisions
clearsurface cleartexturefilters clearworld collisionentity collisionnx collisionny
collisionnz collisions collisionsurface collisiontime collisiontriangle collisionx
collisiony collisionz copyentity countchildren countcollisions countsurfaces
counttriangles countvertices createbrush createcamera createcone createcube
createcylinder createlight createlistener createmesh createmirror createpivot
createplane createsphere createsprite createsurface createterrain createtexture dither
emitsound entityalpha entityanimating entityanimtime entityautofade entityblend
entitybox entitycollided entitycolor entitydistance entityfx entityinview entityname
entityorder entityparent entitypick entitypickmode entitypitch entityradius entityroll
entityshininess entitytexture entitytype entityvisible entityx entityy entityyaw entityz
findchild findsurface fitmesh flipmesh freebrush freeentity freetexture getchild
getentitytype getparent getsurface gfxdriver3d gfxmode3d graphics3d handlesprite
hideentity hwmultitex lightcolor lightconeangles lightmesh lightrange linepick
load3dsound loadanimmesh loadanimseq loadanimtexture loadbrush loadermatrix loadmd2
loadmesh loadsprite loadterrain loadtexture md2animating md2animlength md2animtime
meshdepth meshesintersect meshheight meshwidth modifyterrain moveentity nameentity
paintentity paintmesh paintsurface pickedentity pickednx pickedny pickednz pickedsurface
pickedtime pickedtriangle pickedx pickedy pickedz pointentity positionentity
positionmesh positiontexture projectedx projectedy projectedz renderworld resetentity
rotateentity rotatemesh rotatesprite rotatetexture scaleentity scalemesh scalesprite
scaletexture setanimkey showentity spriteviewmode terraindetail terrainheight
terrainshading terrainsize terrainx terrainy terrainz textureblend texturebuffer
texturecoords texturefilter textureheight texturewidth tformedx tformedy tformedz
tformnormal tformpoint tformvector translateentity trianglevertex turnentity
updatenormals updateworld vertexblue vertexcolor vertexcoords vertexgreen vertexnormal
vertexnx vertexny vertexnz vertexred vertextexcoords vertexu vertexv vertexw vertexx
vertexy vertexz wbuffer windowed3d wireframe'''

STRINGDELIMITERS = "\""

SL_COMMENT = ";"

IGNORECASE = True

SYMBOLS = "( ) [ ] { } ,  : & | < > !  = / *  %  + -"





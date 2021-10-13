import builtins
import pygame
import numpy as np

pygame.init()

###PARAMETERS###
#PIXEL DISPLAY
screen = pygame.display.set_mode([240,136],pygame.SCALED)

pygame.display.set_caption("Pygame-80 by Kyuchumimo v211012")
clock = pygame.time.Clock()

#MUSIC CHANNELS
pygame.mixer.set_num_channels(4)

#####################################

#TIC-80'S BTN() FUNCTION, https://github.com/nesbox/TIC-80/wiki/btn
"""
id : id (0..7) of the key we want to interrogate (see the key map for reference)
"""
def btn(id):
    return pygame.key.get_pressed()[list([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_z, pygame.K_x, pygame.K_a, pygame.K_s])[id]]

#TIC-80'S CLS() FUNCTION, https://github.com/nesbox/TIC-80/wiki/cls
"""
color : RGB list or HEX color
"""
def cls(color=[0x1a,0x1c,0x2c]):
    screen.fill(color)

#TIC-80'S CIRC() FUNCTION, https://github.com/nesbox/TIC-80/wiki/circ
"""
x, y : the coordinates of the circle's center
radius : the radius of the circle in pixels
color: the RGB list or HEX color of the desired color
"""
def circ(x,y,radius,color):
    pygame.draw.circle(screen,color,[x,y],radius)

#TIC-80'S CIRCB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/circ
"""
x, y : the coordinates of the circle's center
radius : the radius of the circle in pixels
color: the RGB list or HEX color of the desired color
"""
def circb(x,y,radius,color):
    pygame.draw.circle(screen,color,[x,y],radius,1)

#TIC-80'S ELLI() FUNCTION
"""
x, y : the coordinates of the ellipse's center
a : the horizontal radius of the ellipse in pixels
b : the vertical radius of the ellipse in pixels
color: the RGB list or HEX color of the desired color
"""
def elli(x,y,a,b,color):
    pygame.draw.ellipse(screen,color,[x-a,y-b,a*2,b*2])

#TIC-80'S ELLIB() FUNCTION
"""
x, y : the coordinates of the ellipse's center
a : the horizontal radius of the ellipse in pixels
b : the vertical radius of the ellipse in pixels
color: the RGB list or HEX color of the desired color
"""
def ellib(x,y,a,b,color):
    pygame.draw.ellipse(screen,color,[x-a,y-b,a*2,b*2],1)

#TIC-80'S EXIT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/exit
"""
exit
"""
def exit():
    pygame.quit()
    raise SystemExit

#TIC-80'S FONT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/font
"""
text : the string to be printed
x : x coordinate of print position
y : y coordinate of print position
colorkey : the RGB list or HEX color of the color that will be used as transparent color. Not setting this parameter will make the map opaque.
w : distance between characters, in pixels
h : vertical distance between characters, in pixels, when printing multi-line text.
fixed : indicates whether the font is fixed width (defaults to false ie variable width)
scale : font scaling (defaults to 1)
"""
def font(text,x,y,colorkey=-1,w=9,h=8,fixed=False,scale=1):
    ts = pygame.image.load_basic("path/file.bmp")
    text = text.encode('ascii')
    
    if scale is not 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    if colorkey is not -1: ts.set_colorkey(colorkey)
    
    if fixed==False:
        w=9
    i_line_offset = 0
    for i in range(len(text)):
        if text[i]==10:
            i_line_offset = i + 1
            y += h
        else:
            screen.blit(ts.subsurface([text[i]%16*(8*scale),text[i]%256//16*(8*scale),(8*scale),(8*scale)]),[(x+((i-i_line_offset)*w))*scale,y*scale])

#TIC-80'S LINE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/line
"""
x0, y0 : the coordinates of the start of the line
x1, y1 : the coordinates of the end of the line
color: the RGB list or HEX color of the desired color
"""
def line(x0,y0,x1,y1,color):
    pygame.draw.line(screen,color,[x0,y0],[x1,y1])

#TIC-80'S MAP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/map
"""
x : The leftmost map cell to be drawn.
y : The uppermost map cell to be drawn.
w : The number of cells to draw horizontally.
h : The number of cells to draw vertically.
sx : The screen x coordinate where drawing of the map section will start.
sy : The screen y coordinate where drawing of the map section will start.
colorkey : RGB list or HEX color that will be used as transparent color. Not setting this parameter will make the map opaque.
scale : Map scaling.
remap [PARTIAL] : An optional function called before every tile is drawn. Using this callback function you can show or hide tiles, create tile animations or flip/rotate tiles during the map rendering stage: callback [tile [x y] ] -> [tile [flip [rotate] ] ] 
"""
def map(x=0,y=0,w=30,h=17,sx=0,sy=0,colorkey=-1,scale=1,remap=None):
    #if m==0: ts = pygame.image.load_basic("assets/map/0.bmp") #[PATTERN TABLE]
    
    PPU=np.copy(VRAM)
    if remap is not None: exec(remap)
    #if remap==None: remap=(VRAM,VRAM,VRAM)
    
    if scale is not 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    if colorkey is not -1: ts.set_colorkey(colorkey)
    
    #TILE BASED BACKGROUND
    for i in range(y,y+h): #ROWS
        for j in range(x,x+w): #COLUMNS
            
            screen.blit(ts.subsurface([PPU[i][j]%16*(8*scale),PPU[i][j]%256//16*(8*scale),(8*scale),(8*scale)]),[(sx+(j*(8*scale)))-(x*(8*scale)),(sy+(i*(8*scale)))-(y*(8*scale))]) #DRAW A MAP FROM A SPRITE SHEET/TILESET (FASTEST) (NEEDS 3 ARRAYS)
            #screen.blit(ts.subsurface([(np.where(*remap))[i,j]%16*8,(np.where(*remap))[i,j]%256//16*8,8,8]),[(sx+(j*8))-(x*8),sy+(i*8)]) #DRAW A MAP FROM A SPRITE SHEET/TILESET WITH NUMPY ARRAYS (FAST) (NEEDS 2 ARRAYS)
            #screen.blit(chr[m0[i][j]],[(j*16)-xm,(i*16)+ym]) #DRAW A MAP THROUGH A LIST OF INDEPENDENT IMAGES (MEDIUM)
            #spr(m0[i][j],(sx+(j*8))-(x*8),sy+(i*8),'#FFFFFF',1,0,0,1,1) #DRAW A MAP FROM A SPRITE SHEET/TILESET WITH SPR

#TIC-80'S MGET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mget
"""
x, y : tilemap coordinates
"""
def mget(x,y):
    return VRAM[y,x]

#TIC-80'S MSET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mget
"""
x, y : tilemap coordinates
tile_id : The background tile (0-255) to place in map at specified coordinates.
"""
def mset(x,y,tile_id):
    VRAM[y,x] = tile_id

#TIC-80'S PIX() FUNCTION, https://github.com/nesbox/TIC-80/wiki/pix
"""
x, y : coordinates of the pixel
color : the the RGB list color to draw
"""
def pix(x,y,color=None):
    scn = pygame.surfarray.pixels3d(screen)
    if color==None:
        return str(scn[x,y])
    else:
        scn[x,y] = color

#TIC-80'S PRINT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/print
"""
text : any string to be printed to the screen
x, y : coordinates for printing the text
color : the RGB list or HEX color to use to draw the text to the screen
fixed [UNUSED] : a flag indicating whether fixed width printing is required
scale : font scaling
smallfont [UNUSED] : use small font if true
"""
def print(text,x=0,y=0,color=[0xf4,0xf4,0xf4],fixed=None,scale=1):
    screen.blit(pygame.font.Font("assets/tic-80 regular.ttf", 8*scale).render(str(text.splitlines()[0]),False,color),[x,y]) #SYSTEM FONT
    
    for i in range(1,len(text.splitlines())):
        y += 6*scale
        screen.blit(pygame.font.Font("assets/tic-80 regular.ttf", 8*scale).render(str(text.splitlines()[i]),False,color),[x,y]) #SYSTEM FONT

#TIC-80'S RECT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/rect
"""
x, y : coordinates of the top left corner of the rectangle
w : the width the rectangle in pixels
h : the height of the rectangle in pixels
color : the RGB list or HEX color that will be used to fill the rectangle
"""
def rect(x,y,w,h,color):
    pygame.draw.rect(screen,color,[x,y,w,h])

#TIC-80'S RECTB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/rect
"""
x, y : coordinates of the top left corner of the rectangle
w : the width the rectangle in pixels
h : the height of the rectangle in pixels
color : the RGB list or HEX color that will be used to color the rectangle's border.
"""
def rectb(x,y,w,h,color):
    pygame.draw.rect(screen,color,[x,y,w,h],1)

#TIC-80'S SFX() FUNCTION, https://github.com/nesbox/TIC-80/wiki/sfx
"""
id : the SFX id (0..n), or -1 to stop playing
note [UNSUPPORTED]: the note number (0..95) or name (ex: C#3)
duration [UNSUPPORTED]: the duration (number of frames) (-1 by default, which plays continuously)
channel : the audio channel to use (0..n)
volume : the volume (0..1) (defaults to 1)
speed [UNSUPPORTED]: the speed (-4..3) (defaults to 0)
"""
def sfx(id,note=None,duration=None,channel=0,volume=1,speed=None):
    if id is not -1:
        snd = pygame.mixer.Sound("assets/sfx/{}.ogg".format(id))
        snd.set_volume(volume)
        pygame.mixer.Channel(channel).play(snd)
    else:
        pygame.mixer.Channel(channel).stop()

#TIC-80'S SPR() FUNCTION, https://github.com/nesbox/TIC-80/wiki/spr
"""
id : index of the sprite (0..n)
x : x coordinate where the sprite will be drawn, starting from top left corner.
y : y coordinate where the sprite will be drawn, starting from top left corner.
colorkey : RGB list or HEX color in the sprite that will be used as transparent color. Use -1 if you want an opaque sprite.
scale : scale factor applied to sprite.
flip : flip the sprite vertically or horizontally or both.
rotate : rotate the sprite by 0, 90, 180 or 270 degrees.
w : width of composite sprite
h : height of composite sprite
"""
def spr(id,x,y,colorkey=-1,scale=1,flip=0,rotate=0,w=1,h=1):
    ts = pygame.image.load_basic("assets/spr/0.bmp") #[PATTERN TABLE]
    
    if scale is not 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    
    obj = pygame.Surface([w*(8*scale),h*(8*scale)])
    
    for i in range(0,h): #ROWS
        for j in range(0,w): #COLUMNS
            obj.blit(ts.subsurface([(id+((i*16)+j))%16*(8*scale),(id+((i*16)+j))%256//16*(8*scale),scale*8,scale*8]),[j*(8*scale),i*(8*scale)])
            
    if flip is not 0: obj = pygame.transform.flip(obj,((flip >> 0 & 1) != 0),((flip >> 1 & 1) != 0))
    if rotate is not 0: obj = pygame.transform.rotate(obj,rotate*-90)
    if colorkey is not -1: obj.set_colorkey(colorkey)
    
    screen.blit(obj,[x,y])

#TIC-80'S TRACE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/trace
"""
message : the message to print in the console. Can be a 'string' or variable.
color : the RGB list of a color
"""
def trace(message,color=[0xf4,0xf4,0xf4]):
    builtins.print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(color[0],color[1],color[2], message))

#TIC-80'S TRI() FUNCTION, https://github.com/nesbox/TIC-80/wiki/tri
"""
x1, y1 : the coordinates of the first triangle corner
x2, y2 : the coordinates of the second corner
x3, y3 : the coordinates of the third corner
color: the RGB list or HEX color of the desired color
"""
def tri(x1,y1,x2,y2,x3,y3,color):
    pygame.draw.polygon(screen,color,[(x1, y1), (x2, y2), (x3, y3)])

#TIC-80'S TRIB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/trib
"""
x1, y1 : the coordinates of the first triangle corner
x2, y2 : the coordinates of the second corner
x3, y3 : the coordinates of the third corner
color: the RGB list or HEX color of the desired color
"""
def trib(x1,y1,x2,y2,x3,y3,color):
    pygame.draw.polygon(screen,color,[(x1, y1), (x2, y2), (x3, y3)],1)

#####################################

t=0
x=96
y=24

while True:
    
    if btn(0): y=y-1
    if btn(1): y=y+1
    if btn(2): x=x-1
    if btn(3): x=x+1
    
    cls([0x94,0xb0,0xc2])
    spr(1+t%60//30*2,x,y,[0x56,0x6c,0x86],3,0,0,2,2)
    print("HELLO WORLD!",84,84)
    t = t+1

#####################################
    if pygame.event.get(pygame.QUIT): exit()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]: pygame.quit(); exit()
    
    pygame.display.flip()
    clock.tick(60)

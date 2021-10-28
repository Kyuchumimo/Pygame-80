import pygame
import numpy as np

pygame.init()

###PARAMETERS###
#WINDOW
pygame.display.set_icon(pygame.image.load_basic('assets/icon.bmp'))
pygame.display.set_caption("Pygame-80 by Kyuchumimo v211012")
screen = pygame.display.set_mode([240,136],pygame.SCALED)
clock = pygame.time.Clock()

#MUSIC CHANNELS
pygame.mixer.set_num_channels(4)

#####################################

#TIC-80'S BTN() FUNCTION, https://github.com/nesbox/TIC-80/wiki/btn
def btn(id):
    """
    Usage:
            btn [id] -> pressed
    Parameters:
            id : id (0..7) of the key we want to interrogate (see the key map for reference)
    Description:
            This function allows you to read the status of one of the buttons attached to TIC. The function returns true if the key with the supplied id is currently in the pressed state. It remains true for as long as the key is held down.
    """
    keymap = [[pygame.K_UP], [pygame.K_DOWN], [pygame.K_LEFT], [pygame.K_RIGHT], [pygame.K_z], [pygame.K_x], [pygame.K_a], [pygame.K_s]]
    return any(pygame.key.get_pressed()[i] for i in keymap[id])

#TIC-80'S CLS() FUNCTION, https://github.com/nesbox/TIC-80/wiki/cls
def cls(color=[0x1a,0x1c,0x2c]):
    """
    Usage:
            cls [color=[0x1a,0x1c,0x2c]]
    Parameters:
            color : RGB list or HEX color
    Description:
            This function clears/fills the entire screen using color. If no parameter is passed, [0x1a,0x1c,0x2c] RGB list color is used.
    """
    screen.fill(color)

#TIC-80'S CIRC() FUNCTION, https://github.com/nesbox/TIC-80/wiki/circ
def circ(x,y,radius,color):
    """
    Usage:
            circ x y radius color
    Parameters:
            x, y : the coordinates of the circle's center
            radius : the radius of the circle in pixels
            color: the RGB list or HEX color of the desired color
    Description:
            This function draws a filled circle of the desired radius and color with its center at x, y.
    """
    pygame.draw.circle(screen,color,[x,y],radius)

#TIC-80'S CIRCB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/circ
def circb(x,y,radius,color):
    """
    Usage:
            circb x y radius color
    Parameters:
            x, y : the coordinates of the circle's center
            radius : the radius of the circle in pixels
            color: the RGB list or HEX color of the desired color
    Description:
            Draws the circumference of a circle with its center at x, y using the radius and color requested.
    """
    pygame.draw.circle(screen,color,[x,y],radius,1)

#TIC-80'S ELLI() FUNCTION
def elli(x,y,a,b,color):
    """
    Usage:
            elli x y a b color
    Parameters:
            x, y : the coordinates of the ellipse's center
            a : the horizontal radius of the ellipse in pixels
            b : the vertical radius of the ellipse in pixels
            color: the RGB list or HEX color of the desired color
    Description:
            This function draws a filled ellipse of the desired radiuses a b and color with its center at x, y.
    """
    pygame.draw.ellipse(screen,color,[x-a,y-b,a*2,b*2])

#TIC-80'S ELLIB() FUNCTION
def ellib(x,y,a,b,color):
    """
    Usage:
            ellib x y a b color
    Parameters:
            x, y : the coordinates of the ellipse's center
            a : the horizontal radius of the ellipse in pixels
            b : the vertical radius of the ellipse in pixels
            color: the RGB list or HEX color of the desired color
    Description:
            This function draws an ellipse border with the desired radiuses a b and color with its center at x, y.
    """
    pygame.draw.ellipse(screen,color,[x-a,y-b,a*2,b*2],1)

#TIC-80'S EXIT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/exit
def exit():
    """
    Usage:
            exit
    Description:
            This function causes program execution to be interrupted.
    """
    import sys
    sys.exit()

#TIC-80'S FONT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/font
def font(text,x,y,colorkey=-1,w=9,h=8,fixed=False,scale=1):
    """
    Usage:
            font text, x, y, [transcolor], [char width], [char height], [fixed=false], [scale=1] -> text width
    Parameters:
            text : the string to be printed
            x : x coordinate of print position
            y : y coordinate of print position
            colorkey : the RGB list or HEX color of the color that will be used as transparent color. Not setting this parameter will make the font opaque.
            w : distance between characters, in pixels
            h : vertical distance between characters, in pixels, when printing multi-line text.
            fixed : indicates whether the font is fixed width (defaults to false ie variable width)
            scale : font scaling (defaults to 1)
    Description:
            This function will draw text to the screen using the foreground spritesheet as the font. Sprite #256 is used for ASCII code 0, #257 for code 1 and so on. The character 'A' has the ASCII code 65 so will be drawn using the sprite with sprite #321 (256+65).
    """
    ts = pygame.image.load_basic("assets/spr/{}.bmp".format(1))
    text = text.encode('ascii')
    
    if scale != 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    if colorkey != -1: ts.set_colorkey(colorkey)
    
    if fixed==False:
        w=9
    i_line_offset = 0
    for i in range(len(text)):
        if text[i]==10:
            i_line_offset = i + 1
            y += h*scale
        else:
            screen.blit(ts.subsurface([text[i]%16*(8*scale),text[i]%256//16*(8*scale),(8*scale),(8*scale)]),[x+((i-i_line_offset)*w)*scale,y])

#TIC-80'S KEY() FUNCTION, https://github.com/nesbox/TIC-80/wiki/key
def key(code):
    """
    Usage:
            key [code] -> pressed
    Parameters:
            code : the key code we want to check (1..65)
    Description:
            The function returns true if the key denoted by keycode is pressed.
    """
    keycodes = [[None], [pygame.K_a], [pygame.K_b], [pygame.K_c], [pygame.K_d], [pygame.K_e], [pygame.K_f], [pygame.K_g], [pygame.K_h], [pygame.K_i], [pygame.K_j], [pygame.K_k], [pygame.K_l], [pygame.K_m], [pygame.K_n], [pygame.K_o], [pygame.K_p], [pygame.K_q], [pygame.K_r], [pygame.K_s], [pygame.K_t], [pygame.K_u], [pygame.K_v], [pygame.K_w], [pygame.K_x], [pygame.K_y], [pygame.K_z], [pygame.K_0], [pygame.K_1], [pygame.K_2], [pygame.K_3], [pygame.K_4], [pygame.K_5], [pygame.K_6], [pygame.K_7], [pygame.K_8], [pygame.K_9], [pygame.K_MINUS], [pygame.K_EQUALS], [pygame.K_LEFTBRACKET], [pygame.K_RIGHTBRACKET], [pygame.K_BACKSLASH], [pygame.K_SEMICOLON], [None], [pygame.K_BACKQUOTE], [pygame.K_COMMA], [pygame.K_PERIOD], [pygame.K_SLASH], [pygame.K_SPACE], [pygame.K_TAB], [pygame.K_RETURN], [pygame.K_BACKSPACE], [pygame.K_DELETE], [pygame.K_INSERT], [pygame.K_PAGEUP], [pygame.K_PAGEDOWN], [pygame.K_HOME], [pygame.K_END], [pygame.K_UP], [pygame.K_DOWN], [pygame.K_LEFT], [pygame.K_RIGHT], [pygame.K_CAPSLOCK], [pygame.K_LCTRL, pygame.K_RCTRL], [pygame.K_LSHIFT, pygame.K_RSHIFT], [pygame.K_LALT]]
    return any(pygame.key.get_pressed()[i] for i in keycodes[code])

#TIC-80'S LINE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/line
def line(x0,y0,x1,y1,color):
    """
    Usage:
            line x0 y0 x1 y1 color
    Parameters:
            x0, y0 : the coordinates of the start of the line
            x1, y1 : the coordinates of the end of the line
            color: the RGB list or HEX color of the desired color
    Description:
            Draws a straight line from point (x0,y0) to point (x1,y1) in the specified color.
    """
    pygame.draw.line(screen,color,[x0,y0],[x1,y1])

#TIC-80'S MAP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/map
VRAM = np.copy(np.loadtxt("assets/map/{}.csv".format(0),dtype='int',delimiter=','))
def map(x=0,y=0,w=30,h=17,sx=0,sy=0,colorkey=-1,scale=1,remap=None):
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
    ts = pygame.image.load_basic("assets/map/{}.bmp".format(0)) #[PATTERN TABLE]
    
    PPU = np.copy(VRAM)
    if remap is not None: exec(remap)
    #if remap==None: remap=(VRAM,VRAM,VRAM)
    
    if scale != 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    if colorkey != -1: ts.set_colorkey(colorkey)
    
    #TILE BASED BACKGROUND
    for i in range(y,y+h): #ROWS
        for j in range(x,x+w): #COLUMNS
            
            screen.blit(ts.subsurface([PPU[i][j]%16*(8*scale),PPU[i][j]%256//16*(8*scale),(8*scale),(8*scale)]),[(sx+(j*(8*scale)))-(x*(8*scale)),(sy+(i*(8*scale)))-(y*(8*scale))]) #DRAW A MAP FROM A SPRITE SHEET/TILESET (FASTEST) (NEEDS 3 ARRAYS)
            #screen.blit(ts.subsurface([(np.where(*remap))[i,j]%16*8,(np.where(*remap))[i,j]%256//16*8,8,8]),[(sx+(j*8))-(x*8),sy+(i*8)]) #DRAW A MAP FROM A SPRITE SHEET/TILESET WITH NUMPY ARRAYS (FAST) (NEEDS 2 ARRAYS)
            #screen.blit(chr[m0[i][j]],[(j*16)-xm,(i*16)+ym]) #DRAW A MAP THROUGH A LIST OF INDEPENDENT IMAGES (MEDIUM)
            #spr(m0[i][j],(sx+(j*8))-(x*8),sy+(i*8),'#FFFFFF',1,0,0,1,1) #DRAW A MAP FROM A SPRITE SHEET/TILESET WITH SPR

#TIC-80'S MGET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mget
def mget(x,y):
    """
    Usage:
            mget x y -> tile_id
    Parameters:
            x, y : tilemap coordinates
    Description:
            This function returns the tile at the specified TILEMAP coordinates, the top left cell of the tilemap being (0, 0).
    """
    return VRAM[y,x]

#TIC-80'S MSET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mget
def mset(x,y,tile_id):
    """
    Usage:
            mset x y tile_id
    Parameters:
            x, y : tilemap coordinates
            tile_id : The background tile (0-255) to place in map at specified coordinates.
    Description:
            This function will change the tile at the specified TILEMAP coordinates. By default, changes made are only kept while the current game is running.
    """
    VRAM[y,x] = tile_id

#TIC-80'S PIX() FUNCTION, https://github.com/nesbox/TIC-80/wiki/pix
def pix(x,y,color=None):
    """
    Usage:
            pix x y color Draw a pixel in the specified color
            pix x y -> color Retrieve a pixel's color
    Parameters:
            x, y : coordinates of the pixel
            color : the the RGB list color to draw
    Description:
            This function can read or write individual pixel color values. When called with a color argument , the pixel at the specified coordinates is set to that color. When called with only x y arguments, the color of the pixel at the specified coordinates is returned.
    """
    scn = pygame.surfarray.pixels3d(screen)
    if color==None:
        return (scn[x,y]).tolist() #FASTER
        #return list(scn[x,y])
    else:
        scn[x,y] = color

#TIC-80'S PMEM() FUNCTION, https://github.com/nesbox/TIC-80/wiki/pmem
def pmem(index,val=None):
    """
    Usage:
            pmem index -> val Retrieve data from persistent memory
            pmem index val -> val Save data to persistent memory
    Parameters:
            index : an index (0..255) into the persistent memory file.
            val : the value you want to store. Omit this parameter to read vs write.
    Output:
             val : when the function is call with only an index parameter, it returns the current value saved in that memory slot.
            
    """
    import os, sys, json
    if val==None:
        try:
            with open("{}.sav".format(os.path.splitext(sys.argv[1])[0]), 'r') as file:
                data = json.load(file)
                return data["{}".format(int(index)%256)]
        except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError) as error:
            pass
    else:
        try:
            with open("{}.sav".format(os.path.splitext(sys.argv[1])[0]), 'r') as file:
                data = json.load(file)
                data[str(int(index%256))] = int(val)%2**32
            with open("{}.sav".format(os.path.splitext(sys.argv[1])[0]), 'w') as file:
                json.dump(data,file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as error:
            with open("{}.sav".format(os.path.splitext(sys.argv[1])[0]), 'w') as file:
                data = dict()
                data["{}".format(int(index)%256)] = int(val)%2**32
                json.dump(data,file)

#TIC-80'S PRINT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/print
def print(text,x=0,y=0,color=[0xf4,0xf4,0xf4],fixed=None,scale=1,smallfont=False):
    """
    Usage:
            print text [x=0 y=0] [color=12] [fixed=false] [scale=1] [smallfont=false] -> text width
    Parameters:
            text : any string to be printed to the screen
            x, y : coordinates for printing the text
            color : the RGB list or HEX color to use to draw the text to the screen
            fixed [UNUSED] : a flag indicating whether fixed width printing is required
            scale : font scaling
            smallfont : use small font if true
    Output:
            text width : returns the width of the text in pixels.
    
    """
    for i in range(0,len(str(text).splitlines())):
        if i>0: y += 6*scale
        if smallfont==False:
            screen.blit(pygame.font.Font("assets/tic-80 regular.ttf", 8*scale).render(str(text).splitlines()[i],False,color),[x,y]) #SYSTEM FONT
        else:
            screen.blit(pygame.font.Font("assets/tic-80 narrow.ttf", 8*scale).render(str(text).splitlines()[i],False,color),[x,y]) #SYSTEM SMALLFONT
    
    if smallfont==False:
        return pygame.font.Font("assets/tic-80 regular.ttf", 8*scale).size(max(str(text).splitlines()))[0]
    else:
        return pygame.font.Font("assets/tic-80 narrow.ttf", 8*scale).size(max(str(text).splitlines()))[0]

#TIC-80'S RECT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/rect
def rect(x,y,w,h,color):
    """
    Usage:
            rect x y w h color
    Parameters:
            x, y : coordinates of the top left corner of the rectangle
            w : the width the rectangle in pixels
            h : the height of the rectangle in pixels
            color : the RGB list or HEX color that will be used to fill the rectangle
    Description:
            This function draws a filled rectangle of the desired size and color at the specified position.
    """
    pygame.draw.rect(screen,color,[x,y,w,h])

#TIC-80'S RECTB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/rect
def rectb(x,y,w,h,color):
    """
    Usage:
            rectb x y w h color
    Parameters:
            x, y : coordinates of the top left corner of the rectangle
            w : the width the rectangle in pixels
            h : the height of the rectangle in pixels
            color : the RGB list or HEX color that will be used to color the rectangle's border.
    Descripion:
            This function draws a one pixel thick rectangle border at the position requested.
    """
    pygame.draw.rect(screen,color,[x,y,w,h],1)

#TIC-80'S SFX() FUNCTION, https://github.com/nesbox/TIC-80/wiki/sfx
def sfx(id,note=None,duration=0,channel=0,volume=15,speed=None):
    """
    Usage:
            sfx id [note](Not supported) [duration=0] [channel=0] [volume=15] [speed=0](Not supported)
    Parameters:
            id : the SFX id (0..n), or -1 to stop playing
            note [NOT SUPPORTED]: the note number (0..95) or name (ex: C#3)
            duration : the duration (number of frames) (0 by default, which plays continuously)
            channel : the audio channel to use (0..defaults to 3)
            volume : the volume (0..15) (defaults to 15)
            speed [NOT SUPPORTED]: the speed (-4..3) (defaults to 0)
    Description:
            This function will play the sound with id in assets/sfx filepath. Calling the function with an id of -1 will stop playing the channel.

            The duration specifies how many ticks to play the sound for; since TIC-80 runs at 60 frames per second, a value of 30 represents half a second. A value of 0 will play the sound continuously.

            The channel parameter indicates which of the channels to use. Allowed values are 0 to defaults to 3.

            Volume can be between 0 and 15.
    """
    if id != -1:
        snd = pygame.mixer.Sound("assets/sfx/{}.ogg".format(id))
        snd.set_volume((volume%16)/15)
        pygame.mixer.Channel(channel).play(snd,0,duration*(1000/60))
    else:
        pygame.mixer.Channel(channel).stop()

#TIC-80'S SPR() FUNCTION, https://github.com/nesbox/TIC-80/wiki/spr
def spr(id,x,y,colorkey=-1,scale=1,flip=0,rotate=0,w=1,h=1):
    """
    id : index of the sprite (0..255)
    x : x coordinate where the sprite will be drawn, starting from top left corner.
    y : y coordinate where the sprite will be drawn, starting from top left corner.
    colorkey : RGB list or HEX color in the sprite that will be used as transparent color. Use -1 if you want an opaque sprite.
    scale : scale factor applied to sprite.
    flip : flip the sprite vertically or horizontally or both.
    rotate : rotate the sprite by 0, 90, 180 or 270 degrees.
    w : width of composite sprite
    h : height of composite sprite
    """
    ts = pygame.Surface([128,256])
    ts.blit(pygame.image.load_basic("assets/map/{}.bmp".format(0)),[0,0])
    ts.blit(pygame.image.load_basic("assets/spr/{}.bmp".format(0)),[0,128])
    
    if scale != 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    
    obj = pygame.Surface([w*(8*scale),h*(8*scale)])
    
    for i in range(0,h): #ROWS
        for j in range(0,w): #COLUMNS
            obj.blit(ts.subsurface([(id+((i*16)+j))%16*(8*scale),(id+((i*16)+j))%512//16*(8*scale),scale*8,scale*8]),[j*(8*scale),i*(8*scale)])
            
    if flip != 0: obj = pygame.transform.flip(obj,((flip >> 0 & 1) != 0),((flip >> 1 & 1) != 0))
    if rotate != 0: obj = pygame.transform.rotate(obj,rotate*-90)
    if colorkey != -1: obj.set_colorkey(colorkey)
    
    screen.blit(obj,[x,y])

#TIC-80'S TIME() FUNCTION, https://github.com/nesbox/TIC-80/wiki/time
def time():
    """
    Usage:
            time -> ticks elapsed since game start
    Parameters:
            ticks : the number of milliseconds elapsed since the game was started
    Description:
            This function returns the number of milliseconds elapsed since the game began execution. Useful for keeping track of time, animating items and triggering events.
    """
    return pygame.time.get_ticks()

#TIC-80'S TSTAMP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/tstamp
def tstamp():
    """
    Usage:
            tstamp -> timestamp
    Parameters:
            timestamp : the current Unix timestamp in seconds
    Description:
            This function returns the number of seconds elapsed since January 1st, 1970. This can be quite useful for creating persistent games which evolve over time between plays.
    """
    import time
    return time.time()//1

#TIC-80'S TRACE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/trace
def trace(message,color=[0xf4,0xf4,0xf4]):
    """
    Usage:
            trace message [color]
    Parameters:
            message : the message to print in the console. Can be a 'string' or variable.
            color : the RGB list of a color
    Description:
            This is a service function, useful for debugging your code. It prints the message parameter to the console in the (optional) color specified.
    """
    import builtins
    builtins.print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(color[0],color[1],color[2], message))

#TIC-80'S TRI() FUNCTION, https://github.com/nesbox/TIC-80/wiki/tri
def tri(x1,y1,x2,y2,x3,y3,color):
    """
    Usage:
            tri x1 y1 x2 y2 x3 y3 color
    Parameters:
            x1, y1 : the coordinates of the first triangle corner
            x2, y2 : the coordinates of the second corner
            x3, y3 : the coordinates of the third corner
            color: the RGB list or HEX color of the desired color
    Description:
            This function draws a triangle filled with color, using the supplied vertices.
    """
    pygame.draw.polygon(screen,color,[(x1, y1), (x2, y2), (x3, y3)])

#TIC-80'S TRIB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/trib
def trib(x1,y1,x2,y2,x3,y3,color):
    """
    Usage:
            trib x1 y1 x2 y2 x3 y3 color
    Parameters:
            x1, y1 : the coordinates of the first triangle corner
            x2, y2 : the coordinates of the second corner
            x3, y3 : the coordinates of the third corner
            color: the RGB list or HEX color of the desired color
    Description:
            This function draws a triangle border with color, using the supplied vertices.
    """
    pygame.draw.polygon(screen,color,[(x1, y1), (x2, y2), (x3, y3)],1)

#####################################

sw16=[[0x1a,0x1c,0x2c], [0x5d,0x27,0x5d], [0xb1,0x3e,0x53], [0xef,0x7d,0x57], [0xff,0xcd,0x75], [0xa7,0xf0,0x70], [0x38,0xb7,0x64], [0x25,0x71,0x79], [0x29,0x36,0x6f], [0x3b,0x5d,0xc9], [0x41,0xa6,0xf6], [0x73,0xef,0xf7], [0xf4,0xf4,0xf4], [0x94,0xb0,0xc2], [0x56,0x6c,0x86], [0x33,0x3c,0x57]]
t=0
x=96
y=24

while True:
    
    if btn(0): y=y-1
    if btn(1): y=y+1
    if btn(2): x=x-1
    if btn(3): x=x+1
    
    cls(sw16[13])
    spr(1+t%60//30*2,x,y,sw16[14],3,0,0,2,2)
    print("HELLO WORLD!",84,84)
    t=t+1

#####################################
    if pygame.event.get(pygame.QUIT): exit()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]: pygame.quit(); exit()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

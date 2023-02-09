# title:  game title
# author: game developer
# desc:   short description
# script: python

import pygame
from pygame.locals import *
import numpy as np
import os, sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # running in a PyInstaller bundle
    _ASSET_PATH = os.path.join(sys._MEIPASS, 'assets')
else:
    # running in a normal Python process
    _ASSET_PATH = 'assets'

pygame.init()

###PARAMETERS###
# WINDOW
pygame.display.set_icon(pygame.image.load(os.path.join(_ASSET_PATH, 'icon.png')))
pygame.display.set_caption("Pygame-80 by Kyuchumimo v230115")
_SCREEN = pygame.display.set_mode([240, 136], pygame.SCALED)

# MUSIC CHANNELS
pygame.mixer.set_num_channels(4)

_TIC = {"TILES":pygame.image.load(os.path.join(_ASSET_PATH, 'map', '0.png')), "SPRITES":pygame.image.load(os.path.join(_ASSET_PATH, 'spr', '0.png')), "MAP":np.loadtxt(os.path.join(_ASSET_PATH, 'map', '0.csv'),dtype='int',delimiter=','), "PALETTE":[[0x1a,0x1c,0x2c], [0x5d,0x27,0x5d], [0xb1,0x3e,0x53], [0xef,0x7d,0x57], [0xff,0xcd,0x75], [0xa7,0xf0,0x70], [0x38,0xb7,0x64], [0x25,0x71,0x79], [0x29,0x36,0x6f], [0x3b,0x5d,0xc9], [0x41,0xa6,0xf6], [0x73,0xef,0xf7], [0xf4,0xf4,0xf4], [0x94,0xb0,0xc2], [0x56,0x6c,0x86], [0x33,0x3c,0x57]], "FONT":(pygame.font.Font(os.path.join(_ASSET_PATH, 'tic-80_regular.ttf'), 8), pygame.font.Font(os.path.join(_ASSET_PATH, 'tic-80_narrow.ttf'), 8), pygame.font.Font(os.path.join(_ASSET_PATH, 'tic-80_regular-mono.ttf'), 8), pygame.font.Font(os.path.join(_ASSET_PATH, 'tic-80_narrow-mono.ttf'), 8)), "CLOCK":pygame.time.Clock()}
_SAVEFILE = "pygame80"

#####################################

# TIC-80'S BTN() FUNCTION, https://github.com/nesbox/TIC-80/wiki/btn
def btn(id):
    """
    Usage:
            btn [id] -> pressed
    Parameters:
            id : id (0..7) of the key we want to interrogate (see the key map for reference)
    Description:
            This function allows you to read the status of one of the buttons attached to TIC. The function returns True if the key with the supplied id is currently in the pressed state. It remains True for as long as the key is held down.
    """
    keymap = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_z, pygame.K_x, pygame.K_a, pygame.K_s)
    
    return pygame.key.get_pressed()[keymap[id]]

# TIC-80'S BTNP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/btnp
def btnp(id):
    """
    Usage:
            btnp [[id, [hold][NOT SUPPORTED], [period][NOT SUPPORTED] ] -> pressed
    Parameters:
            id : the id (0..7) of the button we wish to interrogate
            hold [NOT SUPPORTED]
            period [NOT SUPPORTED]
    Description:
            This function allows you to read the status of one of the buttons. It returns True only if the key has been pressed since the last frame.
    """
    global _KEY
    
    keymap = ("up", "down", "left", "right", "z", "x", "a", "s")
            
    return _KEY == keymap[id]

# TIC-80'S CIRC() FUNCTION, https://github.com/nesbox/TIC-80/wiki/circ
def circ(x, y, radius, color):
    """
    Usage:
            circ x y radius color
    Parameters:
            x, y : the coordinates of the circle's center
            radius : the radius of the circle in pixels
            color: the index of the desired color in the current palette
    Description:
            This function draws a filled circle of the desired radius and color with its center at x, y.
    """
    pygame.draw.circle(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x, y], radius)

# TIC-80'S CIRCB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/circ
def circb(x, y, radius, color):
    """
    Usage:
            circb x y radius color
    Parameters:
            x, y : the coordinates of the circle's center
            radius : the radius of the circle in pixels
            color: the index of the desired color in the current palette
    Description:
            Draws the circumference of a circle with its center at x, y using the radius and color requested.
    """
    pygame.draw.circle(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x, y], radius, 1)

# TIC-80'S CLIP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/clip
def clip(*args):
    """
    Usage:
            clip Unsets the clipping region (draws to the full screen)
            clip x y width height Sets the clipping region
    Parameters:    
            x, y : coordinates of the top left of the clipping region
            width : width of the clipping region in pixels
            height : height of the clipping region in pixels
    Description:
            This function limits drawing to a clipping region or 'viewport' defined by x,y, width, and height. Any pixels falling outside of this area will not be drawn.

            Calling clip() with no parameters will reset the drawing area to the entire screen.
    """
    if len(args) == 0:
        _SCREEN.set_clip(0, 0, pygame.Surface.get_size(_SCREEN)[0], pygame.Surface.get_size(_SCREEN)[1])
    elif len(args) == 4:
        _SCREEN.set_clip([args[0], args[1], args[2], args[3]])
    else:
        raise Exception("invalid parameters, use clip(x, y, w, h) or clip()\n")

# TIC-80'S CLS() FUNCTION, https://github.com/nesbox/TIC-80/wiki/cls
def cls(color=0):
    """
    Usage:
            cls [color=0]
    Parameters:
            color : index (0..n) of a color in the current palette (defaults to 0)
    Description:
            This function clears/fills the entire screen using color. If no parameter is passed, index 0 of the palette is used.
    """
    _SCREEN.fill(_TIC["PALETTE"][color%len(_TIC["PALETTE"])])

# TIC-80'S ELLI() FUNCTION
def elli(x, y, a, b, color):
    """
    Usage:
            elli x y a b color
    Parameters:
            x, y : the coordinates of the ellipse's center
            a : the horizontal radius of the ellipse in pixels
            b : the vertical radius of the ellipse in pixels
            color: the index of the desired color in the current palette
    Description:
            This function draws a filled ellipse of the desired radiuses a b and color with its center at x, y.
    """
    pygame.draw.ellipse(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x-a, y-b, a*2, b*2])

# TIC-80'S ELLIB() FUNCTION
def ellib(x, y, a, b, color):
    """
    Usage:
            ellib x y a b color
    Parameters:
            x, y : the coordinates of the ellipse's center
            a : the horizontal radius of the ellipse in pixels
            b : the vertical radius of the ellipse in pixels
            color: the index of the desired color in the current palette
    Description:
            This function draws an ellipse border with the desired radiuses a b and color with its center at x, y.
    """
    pygame.draw.ellipse(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x-a, y-b, a*2, b*2], 1)

# TIC-80'S EXIT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/exit
def exit():
    """
    Usage:
            exit
    Description:
            This function causes program execution to be interrupted.
    """
    pygame.quit()
    sys.exit()

# TIC-80'S FONT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/font
def font(text, x, y, transcolor=-1, w=9, h=8, fixed=False, scale=1):
    """
    Usage:
            font text, x, y, [transcolor], [char width], [char height], [fixed=False], [scale=1] -> text width
    Parameters:
            text : the string to be printed
            x : x coordinate of print position
            y : y coordinate of print position
            transcolor : the palette index to use for transparency
            w : distance between characters, in pixels
            h : vertical distance between characters, in pixels, when printing multi-line text.
            fixed : indicates whether the font is fixed width (defaults to False ie variable width)
            scale : font scaling (defaults to 1)
    Description:
            This function will draw text to the screen using the foreground spritesheet as the font. Sprite #256 is used for ASCII code 0, #257 for code 1 and so on. The character 'A' has the ASCII code 65 so will be drawn using the sprite with sprite #321 (256+65).
    """
    ts = pygame.Surface([128, 128])
    ts.blit(_TIC["SPRITES"], [0, 0])
    
    text = str(text).encode('ascii')
    
    if scale != 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    if transcolor != -1: ts.set_colorkey(_TIC["PALETTE"][transcolor%len(_TIC["PALETTE"])])
    
    if fixed==False:
        w=9
    i_line_offset = 0
    for i in range(len(text)):
        if text[i]==10:
            i_line_offset = i + 1
            y += h*scale
        else:
            _SCREEN.blit(ts.subsurface([text[i]%16*(8*scale),text[i]%256//16*(8*scale),(8*scale),(8*scale)]),[x+((i-i_line_offset)*w)*scale,y])

# TIC-80'S KEY() FUNCTION, https://github.com/nesbox/TIC-80/wiki/key
def key(code):
    """
    Usage:
            key [code] -> pressed
    Parameters:
            code : the key code we want to check (1..65)
    Returns:
            pressed : key is currently pressed (True/False)
    Description:
            The function returns True if the key denoted by keycode is pressed.
    """
    keycodes = [[None], [pygame.K_a], [pygame.K_b], [pygame.K_c], [pygame.K_d], [pygame.K_e], [pygame.K_f], [pygame.K_g], [pygame.K_h], [pygame.K_i], [pygame.K_j], [pygame.K_k], [pygame.K_l], [pygame.K_m], [pygame.K_n], [pygame.K_o], [pygame.K_p], [pygame.K_q], [pygame.K_r], [pygame.K_s], [pygame.K_t], [pygame.K_u], [pygame.K_v], [pygame.K_w], [pygame.K_x], [pygame.K_y], [pygame.K_z], [pygame.K_0], [pygame.K_1], [pygame.K_2], [pygame.K_3], [pygame.K_4], [pygame.K_5], [pygame.K_6], [pygame.K_7], [pygame.K_8], [pygame.K_9], [pygame.K_MINUS], [pygame.K_EQUALS], [pygame.K_LEFTBRACKET], [pygame.K_RIGHTBRACKET], [pygame.K_BACKSLASH], [pygame.K_SEMICOLON], [None], [pygame.K_BACKQUOTE], [pygame.K_COMMA], [pygame.K_PERIOD], [pygame.K_SLASH], [pygame.K_SPACE], [pygame.K_TAB], [pygame.K_RETURN], [pygame.K_BACKSPACE], [pygame.K_DELETE], [pygame.K_INSERT], [pygame.K_PAGEUP], [pygame.K_PAGEDOWN], [pygame.K_HOME], [pygame.K_END], [pygame.K_UP], [pygame.K_DOWN], [pygame.K_LEFT], [pygame.K_RIGHT], [pygame.K_CAPSLOCK], [pygame.K_LCTRL, pygame.K_RCTRL], [pygame.K_LSHIFT, pygame.K_RSHIFT], [pygame.K_LALT]]
    return any(pygame.key.get_pressed()[i] for i in keycodes[code])

# TIC-80'S KEYP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/keyp
def keyp(code):
    """
    Usage:
            keyp [code [hold[NOT SUPPORTED] period[NOT SUPPORTED]] ] -> pressed
    Parameters:
            code : the key code we want to check (1..65)
            hold [NOT SUPPORTED]
            period [NOT SUPPORTED]
    Returns:
            pressed : key is pressed (True/False)
    Description:
            This function returns True if the given key is pressed but wasn't pressed in the previous frame.
    """
    global _KEY
    
    keycodes = [[None], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"], ["m"], ["n"], ["o"], ["p"], ["q"], ["r"], ["s"], ["t"], ["u"], ["v"], ["w"], ["x"], ["y"], ["z"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["-"], ["="], ["["], ["]"], ["\\"], [";"], [None], ["`"], [","], ["."], ["/"], [" "], ["tab"], ["return"], ["backspace"], ["delete"], ["insert"], ["page up"], ["page down"], ["home"], ["end"], ["up"], ["down"], ["left"], ["right"], ["caps lock"], ["left ctrl", "right ctrl"], ["left shift", "right shift"], ["left alt"]]
    
    return any(_KEY == i for i in keycodes[code])

# TIC-80'S LINE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/line
def line(x0, y0, x1, y1, color):
    """
    Usage:
            line x0 y0 x1 y1 color
    Parameters:
            x0, y0 : the coordinates of the start of the line
            x1, y1 : the coordinates of the end of the line
            color : the index of the color in the current palette
    Description:
            Draws a straight line from point (x0,y0) to point (x1,y1) in the specified color.
    """
    pygame.draw.line(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x0, y0], [x1, y1])

# TIC-80'S MAP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/map
def map(x=0, y=0, w=30, h=17, sx=0, sy=0, colorkey=-1, scale=1, remap=None):
    """
    Usage:
            map x y w h sx sy colorkey scale remap
    Parameters:
            x : The leftmost map cell to be drawn.
            y : The uppermost map cell to be drawn.
            w : The number of cells to draw horizontally.
            h : The number of cells to draw vertically.
            sx : The screen x coordinate where drawing of the map section will start.
            sy : The screen y coordinate where drawing of the map section will start.
            colorkey : index of the color that will be used as transparent color. Not setting this parameter will make the map opaque.
            scale : Map scaling.
            remap [PARTIAL] : An optional exec() function called before every tile is drawn. Using this callback function you can show or hide tiles or create tile animations during the map rendering stage: "PPU[(PPU == tile)] = tile" 
    """
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)
    sx = int(sx)
    sy = int(sy)
    colorkey = int(colorkey)
    scale = int(scale)
    
    ts = pygame.Surface([128, 128])
    ts.blit(_TIC["TILES"], [0, 0]) # [PATTERN TABLE]
    PPU = np.copy(_TIC["MAP"])
    
    if remap is not None: exec(remap)
    # if remap==None: remap=(VRAM,VRAM,VRAM)
    
    if scale != 1: ts = pygame.transform.scale(ts, [(pygame.Surface.get_size(ts)[0])*scale, (pygame.Surface.get_size(ts)[1])*scale])
    if colorkey > -1: ts.set_colorkey(_TIC["PALETTE"][colorkey%len(_TIC["PALETTE"])])
    
    # TILE BASED BACKGROUND
    for i in range(y, y+h): # ROWS
        for j in range(x, x+w): # COLUMNS
            
            _SCREEN.blit(ts.subsurface([PPU[i%PPU.shape[0]][j%PPU.shape[1]]%16*(8*scale),PPU[i%PPU.shape[0]][j%PPU.shape[1]]%256//16*(8*scale),(8*scale),(8*scale)]),[(sx+(j*(8*scale)))-(x*(8*scale)),(sy+(i*(8*scale)))-(y*(8*scale))]) #DRAW A MAP FROM A SPRITE SHEET/TILESET (FASTEST) (NEEDS 3 ARRAYS)
            # _SCREEN.blit(ts.subsurface([(np.where(*remap))[i,j]%16*8,(np.where(*remap))[i,j]%256//16*8,8,8]),[(sx+(j*8))-(x*8),sy+(i*8)]) #DRAW A MAP FROM A SPRITE SHEET/TILESET WITH NUMPY ARRAYS (FAST) (NEEDS 2 ARRAYS)
            # _SCREEN.blit(chr[m0[i][j]],[(j*16)-xm,(i*16)+ym]) #DRAW A MAP THROUGH A LIST OF INDEPENDENT IMAGES (MEDIUM)
            # spr(m0[i][j],(sx+(j*8))-(x*8),sy+(i*8),'#FFFFFF',1,0,0,1,1) #DRAW A MAP FROM A SPRITE SHEET/TILESET WITH SPR

# TIC-80'S MGET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mget
def mget(x, y):
    """
    Usage:
            mget x y -> tile_id
    Parameters:
            x, y : tilemap coordinates
    Description:
            This function returns the tile at the specified TILEMAP coordinates, the top left cell of the tilemap being (0, 0).
    """
    x = int(x)
    y = int(y)
    
    if ((x < 0) | (x >= _TIC['MAP'].shape[1]) | (y < 0) | (y >= _TIC['MAP'].shape[0])): return 0
        
    return _TIC["MAP"][y, x]

# TIC-80'S MSET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mget
def mset(x, y, tile_id):
    """
    Usage:
            mset x y tile_id
    Parameters:
            x, y : tilemap coordinates
            tile_id : The background tile (0-255) to place in map at specified coordinates.
    Description:
            This function will change the tile at the specified TILEMAP coordinates. By default, changes made are only kept while the current game is running.
    """
    x = int(x)
    y = int(y)
    tile_id = int(tile_id)

    if ((x < 0) | (x >= _TIC['MAP'].shape[1]) | (y < 0) | (y >= _TIC['MAP'].shape[0])): return
    
    _TIC["MAP"][y, x] = tile_id

# TIC-80'S MOUSE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/mouse
def mouse():
    """
    Usage:
            mouse -> x y left middle right scrollx scrolly
    Parameters:
            x y : coordinates of the mouse pointer
            left : left button is down (True/False)
            middle : middle button is down (True/False)
            right : right button is down (True/False)
            scrollx : x scroll delta since last frame (-1..1)
            scrolly : y scroll delta since last frame (-1..1)
    Description:
            This function returns the mouse coordinates and a boolean value for the state of each mouse button, with True indicating that a button is pressed.
    """
    mw_xy = 0, 0
    for event in pygame.event.get(MOUSEWHEEL):
        mw_xy = event.x, event.y
    
    return tuple((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[1],pygame.mouse.get_pressed()[2],mw_xy[0],mw_xy[1]))

# TIC-80'S MUSIC() FUNCTION, https://github.com/nesbox/TIC-80/wiki/music
def music(track=-1, frame=-1, row=-1, loop=True, sustain=False, tempo=-1, speed=-1):
    """
    Usage:
            music [track=-1] [frame=-1] [row=-1] [loop=True] [sustain=False][NOT SUPPORTED] [tempo=-1][NOT SUPPORTED] [speed=-1][NOT SUPPORTED]
            ...or to stop the music:
            music
    Parameters:
            track : the id of the track to play (0..n)
            frame : the index of the frame to play from (0..254)
            row : the index of the row to play from (0..63)
            loop : loop music (True) or play it once (False)
            sustain [NOT SUPPORTED]
            tempo : play track with the specified tempo
            speed : play track with the specified speed
    Description:
            This function starts playing a track.
    """
    import struct, io
    
    filename = os.path.join(_ASSET_PATH, 'music', f'{int(track)}.xm')
    
    if track < 0:
        pygame.mixer.music.stop()
    else:
        with open(filename, "rb") as file:
            data = bytearray(file.read())
            
            if tempo >= 32: struct.pack_into("<H", data, 0x4E, tempo)
            if speed > 0: struct.pack_into("<H", data, 0x4C, speed)
            
            T = struct.unpack_from("<H", data, 0x4E)[0]
            M = struct.unpack_from("<H", data, 0x4C)[0]
            timeperrow = 2500 / T * M
            
            pygame.mixer.music.load(io.BytesIO(data))
            pygame.mixer.music.play(loop and -1 or 0, (timeperrow * (max(0, row) + (max(0, frame) * 63))) / 1000)

# TIC-80'S PIX() FUNCTION, https://github.com/nesbox/TIC-80/wiki/pix
def pix(x, y, color=None):
    """
    Usage:
            pix x y color Draw a pixel in the specified color
            pix x y -> color Retrieve a pixel's color
    Parameters:
            x, y : coordinates of the pixel
            color : the index of the palette color to draw
    Returns:
            color : the index (0-n) of the palette color at the specified coordinates.
    Description:
            This function can read or write individual pixel color values. When called with a color argument , the pixel at the specified coordinates is set to that color. When called with only x y arguments, the color of the pixel at the specified coordinates is returned.
    """
    x = int(x)
    y = int(y)
    if type(color) != None: int(color)
    
    scn = pygame.surfarray.pixels3d(_SCREEN)
    if color == None:
        return _TIC["PALETTE"].index(scn[x, y].tolist()) #FASTER
        #return list(scn[x, y])
    elif x >= 0 and x < _SCREEN.get_size[0] and y >= 0 and y < _SCREEN.get_size[1]:
        scn[x, y] = _TIC["PALETTE"][color%len(_TIC["PALETTE"])]

# TIC-80'S PMEM() FUNCTION, https://github.com/nesbox/TIC-80/wiki/pmem
def pmem(index, val32=None):
    """
    Usage:
            pmem index -> val32 Retrieve data from persistent memory file
            pmem index val32 Save new value to persistent memory file
    Parameters:
            index : an index (0..255) into the persistent memory file.
            val32 : the 32-bit integer value you want to store. Omit this parameter to read vs write.
    Returns:
            val32 : the current value saved to the specified memory slot.
    Description:
            This function allows you to save and retrieve data in one of the 256 individual 32-bit slots available in the file's persistent memory. This is useful for saving high-scores, level advancement or achievements. Data is stored as unsigned 32-bit integer (from 0 to 4294967295).
    """
    import json
    
    if val32==None:
        try:
            with open(f"{_SAVEFILE}.sav", 'r') as file:
                data = json.load(file)
                return data["{}".format(int(index)%256)]
        except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError) as error:
            return 0
    else:
        try:
            with open(f"{_SAVEFILE}.sav", 'r') as file:
                data = json.load(file)
                prior_val32 = data["{}".format(int(index)%256)]
        except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError) as error:
            prior_val32 = 0
        
        try:
            with open(f"{_SAVEFILE}.sav", 'r') as file:
                data = json.load(file)
                data[str(int(index%256))] = int(val32)%2**32
            with open(f"{_SAVEFILE}.sav", 'w') as file:
                json.dump(data,file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as error:
            with open(f"{_SAVEFILE}.sav", 'w') as file:
                data = dict()
                data["{}".format(int(index)%256)] = int(val32)%2**32
                json.dump(data,file)
        
        return prior_val32

# TIC-80'S PRINT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/print
def print(text, x=0, y=0, color=15, fixed=False, scale=1, smallfont=False):
    """
    Usage:
            print text [x=0 y=0] [color=12] [fixed=False] [scale=1] [smallfont=False] -> text width
    Parameters:
            text : any string to be printed to the screen
            x, y : coordinates for printing the text
            color : the color to use to draw the text to the screen
            fixed : a flag indicating whether fixed width printing is required
            scale : font scaling
            smallfont : use small font if True
    Returns:
            text width : returns the width of the text in pixels.
    Description:
            This will simply print text to the screen using the font defined in assets. When set to True, the fixed width option ensures that each character will be printed in a 'box' of the same size, so the character 'i' will occupy the same width as the character 'w' for example. When fixed width is false, there will be a single space between each character.
    """
    for i in range(len(str(text).splitlines())):
        if i>0: y += 6*scale
        if fixed==False:
            if smallfont==False:
                _SCREEN.blit(pygame.transform.scale(_TIC["FONT"][0].render(str(text).splitlines()[i],False,_TIC["PALETTE"][color%len(_TIC["PALETTE"])]),np.array(pygame.font.Font.size(_TIC["FONT"][0],str(text).splitlines()[i]))*scale),[x,y]) #SYSTEM FONT
            else:
                _SCREEN.blit(pygame.transform.scale(_TIC["FONT"][1].render(str(text).splitlines()[i],False,_TIC["PALETTE"][color%len(_TIC["PALETTE"])]),np.array(pygame.font.Font.size(_TIC["FONT"][1],str(text).splitlines()[i]))*scale),[x,y]) #SYSTEM SMALLFONT
        else:
            if smallfont==False:
                _SCREEN.blit(pygame.transform.scale(_TIC["FONT"][2].render(str(text).splitlines()[i],False,_TIC["PALETTE"][color%len(_TIC["PALETTE"])]),np.array(pygame.font.Font.size(_TIC["FONT"][2],str(text).splitlines()[i]))*scale),[x,y]) #SYSTEM FONT FIXED
            else:
                _SCREEN.blit(pygame.transform.scale(_TIC["FONT"][3].render(str(text).splitlines()[i],False,_TIC["PALETTE"][color%len(_TIC["PALETTE"])]),np.array(pygame.font.Font.size(_TIC["FONT"][3],str(text).splitlines()[i]))*scale),[x,y]) #SYSTEM SMALLFONT FIXED
    
    if fixed==False:
        if smallfont==False:
            return _TIC["FONT"][0].size(max(str(text).splitlines()))[0] * scale
        else:
            return _TIC["FONT"][1].size(max(str(text).splitlines()))[0] * scale
    else:
        if smallfont==False:
            return _TIC["FONT"][2].size(max(str(text).splitlines()))[0] * scale
        else:
            return _TIC["FONT"][3].size(max(str(text).splitlines()))[0] * scale

# TIC-80'S RECT() FUNCTION, https://github.com/nesbox/TIC-80/wiki/rect
def rect(x, y, w, h, color):
    """
    Usage:
            rect x y w h color
    Parameters:
            x, y : coordinates of the top left corner of the rectangle
            w : the width the rectangle in pixels
            h : the height of the rectangle in pixels
            color : the index of the color in the palette that will be used to fill the rectangle
    Description:
            This function draws a filled rectangle of the desired size and color at the specified position.
    """
    pygame.draw.rect(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x, y, w, h])

# TIC-80'S RECTB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/rect
def rectb(x, y, w, h, color):
    """
    Usage:
            rectb x y w h color
    Parameters:
            x, y : coordinates of the top left corner of the rectangle
            w : the width the rectangle in pixels
            h : the height of the rectangle in pixels
            color : the index of the color in the palette that will be used to color the rectangle's border.
    Descripion:
            This function draws a one pixel thick rectangle border at the position requested.
    """
    pygame.draw.rect(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [x, y, w, h], 1)

# TIC-80'S RESET() FUNCTION, https://github.com/nesbox/TIC-80/wiki/reset
def reset():
    """
    Usage:
            reset
    Description:
            Resets the program.
    """
    os.execv(sys.executable, ['python3'] + sys.argv)

# TIC-80'S SFX() FUNCTION, https://github.com/nesbox/TIC-80/wiki/sfx
def sfx(id, note=None, duration=0, channel=0, volume=15, speed=0):
    """
    Usage:
            sfx id [note][NOT SUPPORTED] [duration=0] [channel=0] [volume=15] [speed=0][NOT SUPPORTED]
    Parameters:
            id : the SFX id (0..n), or -1 to stop playing
            note [NOT SUPPORTED]
            duration : the duration (number of frames) (0 by default, which plays continuously)
            channel : the audio channel to use (0..defaults to 3)
            volume : the volume (0..15) (defaults to 15)
            speed [NOT SUPPORTED]
    Description:
            This function will play the sound with id in assets/sfx filepath. Calling the function with an id of -1 will stop playing the channel.

            The duration specifies how many ticks to play the sound for; since TIC-80 runs at 60 frames per second, a value of 30 represents half a second. A value of 0 will play the sound continuously.

            The channel parameter indicates which of the channels to use. Allowed values are 0 to defaults to 3.

            Volume can be between 0 and 15.
    """
    if id != -1:
        snd = pygame.mixer.Sound(os.path.join(_ASSET_PATH, 'sfx', f'{int(id)}.wav'))
        snd.set_volume((volume%16)/15)
        pygame.mixer.Channel(channel).play(snd, 0, int(duration * (1000 / 60)))
    else:
        pg.mixer.Channel(channel).stop()

# TIC-80'S SPR() FUNCTION, https://github.com/nesbox/TIC-80/wiki/spr
def spr(id, x, y, colorkey=-1, scale=1, flip=0, rotate=0, w=1, h=1):
    """
    Usage:
            print text [x=0 y=0] [color=12] [fixed=False] [scale=1] [smallfont=False] -> text width
    Parameters:
            id : index of the sprite (0..511)
            x : x coordinate where the sprite will be drawn, starting from top left corner.
            y : y coordinate where the sprite will be drawn, starting from top left corner.
            colorkey : index of the color in the sprite that will be used as transparent color. Use -1 if you want an opaque sprite.
            scale : scale factor applied to sprite.
            flip : flip the sprite vertically or horizontally or both.
            rotate : rotate the sprite by 0, 90, 180 or 270 degrees.
            w : width of composite sprite
            h : height of composite sprite
    """
    ts = pygame.Surface([128, 256])
    ts.blit(_TIC["TILES"], [0, 0])
    ts.blit(_TIC["SPRITES"], [0, 128])
    
    if scale != 1: ts = pygame.transform.scale(ts,[(pygame.Surface.get_size(ts)[0])*scale,(pygame.Surface.get_size(ts)[1])*scale])
    
    obj = pygame.Surface([w*(8*scale), h*(8*scale)])
    
    for i in range(0,h): #ROWS
        for j in range(0,w): #COLUMNS
            obj.blit(ts.subsurface([(int(id)+((i*16)+j))%16*(8*scale),(int(id)+((i*16)+j))%512//16*(8*scale),scale*8,scale*8]),[j*(8*scale),i*(8*scale)])
            
    if flip != 0: obj = pygame.transform.flip(obj, flip >> 0 & 1, flip >> 1 & 1)
    if rotate != 0: obj = pygame.transform.rotate(obj, rotate*-90)
    if colorkey != -1: obj.set_colorkey(_TIC["PALETTE"][colorkey%len(_TIC["PALETTE"])])
    
    _SCREEN.blit(obj, [x,y])

# TIC-80'S SYNC() FUNCTION, https://github.com/nesbox/TIC-80/wiki/sync
def sync(mask=0, bank=0, tocart=False):
    """
    Usage:
            sync [mask=0] [bank=0] [tocart=False]
    Parameters:
            mask : mask of sections you want to switch:
                tiles   = 1<<0 -- 1
                sprites = 1<<1 -- 2
                map     = 1<<2 -- 4
                sfx     = 1<<3 -- 8   [NOT SUPPORTED]
                music   = 1<<4 -- 16  [NOT SUPPORTED]
                palette = 1<<5 -- 32  [NOT SUPPORTED]
                flags   = 1<<6 -- 64  [NOT SUPPORTED]
                screen  = 1<<7 -- 128 [NOT SUPPORTED]
            0 - will switch all the sections 1 | 2 | 4 - will switch only TILES, SPRITES and MAP sections, for example
            bank : memory bank (0..n)
            tocart : True - save memory from runtime to bank/cartridge, False - load data from bank/cartridge to runtime.
    """
    if mask == 0: mask = 0b111
    
    if tocart == False:
        if (0b1 & mask) == 0b1: _TIC["TILES"] = pygame.image.load(os.path.join(_ASSET_PATH, 'map', f'{bank}.png')) #TILES
        if (0b10 & mask) == 0b10: _TIC["SPRITES"] = pygame.image.load(os.path.join(_ASSET_PATH, 'spr', f'{bank}.png')) #SPRITES
        if (0b100 & mask) == 0b100: _TIC["MAP"] = np.loadtxt(os.path.join(_ASSET_PATH, 'map', f'{bank}.csv'), dtype='int', delimiter=',')
    elif tocart == True:
        if (0b1 & mask) == 0b1: pygame.image.save(_TIC["TILES"], os.path.join(_ASSET_PATH, 'map', f'{bank}.png')) #TILES
        if (0b10 & mask) == 0b10: pygame.image.save(_TIC["SPRITES"], os.path.join(_ASSET_PATH, 'spr', f'{bank}.png')) #SPRITES
        if (0b100 & mask) == 0b100: np.savetxt(os.path.join(_ASSET_PATH, 'map', f'{bank}.csv'), _TIC["MAP"], fmt='%d', delimiter=',')

# TIC-80'S TEXTRI() FUNCTION, https://github.com/nesbox/TIC-80/wiki/textri
def textri(x1, y1, x2, y2, x3, y3, u1, v1, u2, v2, u3, v3, use_map=False, trans=-1):
    """
    """
    texture = pygame.surfarray.array3d(_TIC["SPRITES"])
    
    triangle = np.array([[x1,y1],[x2,y2],[x3,y3]])
    texture_uv = np.array([[u1,v1],[u2,v2],[u3,v3]])
    
    frame = pygame.surfarray.array3d(_SCREEN)
    
    sorted_y = triangle[:,1].argsort()

    x_start, y_start = triangle[sorted_y[0]]
    x_middle, y_middle = triangle[sorted_y[1]]
    x_stop, y_stop = triangle[sorted_y[2]]

    x_slope_1 = (x_stop - x_start)/(y_stop - y_start + 1e-32)
    x_slope_2 = (x_middle - x_start)/(y_middle - y_start + 1e-32)
    x_slope_3 = (x_stop - x_middle)/(y_stop - y_middle + 1e-32)

    uv_start = texture_uv[sorted_y[0]]/128
    uv_middle = texture_uv[sorted_y[1]]/128
    uv_stop = texture_uv[sorted_y[2]]/128

    uv_slope_1 = (uv_stop - uv_start)/(y_stop - y_start + 1e-32)
    uv_slope_2 = (uv_middle - uv_start)/(y_middle - y_start + 1e-32)
    uv_slope_3 = (uv_stop - uv_middle)/(y_stop - y_middle + 1e-32)
    
    for y in range(max(y_start,0), min(y_stop,pygame.Surface.get_size(_SCREEN)[1])):

        x1 = x_start + int((y-y_start)*x_slope_1)
        uv1 = uv_start + (y-y_start)*uv_slope_1

        if y < y_middle:
            x2 = x_start + int((y-y_start)*x_slope_2)
            uv2 = uv_start + (y-y_start)*uv_slope_2
        else:
            x2 = x_middle + int((y-y_middle)*x_slope_3)
            uv2 = uv_middle + (y-y_middle)*uv_slope_3
        
        if x1 > x2:
            x1, x2 = x2, x1
            uv1, uv2 = uv2, uv1

        uv_slope = (uv2 - uv1)/(x2 - x1 + 1e-32)
        
        for x in range(max(x1,0), min(x2,pygame.Surface.get_size(_SCREEN)[0])):
            uv = uv1 + (x - x1) * uv_slope
            u = int(uv[0]*128)%128
            v = int(uv[1]*128)%128
            frame[x, y] = texture[u][v]

    surf = pygame.surfarray.make_surface(frame)
    if trans != -1: surf.set_colorkey(_TIC["PALETTE"][trans%len(_TIC["PALETTE"])])
    _SCREEN.blit(surf, (0,0))

# TIC-80'S TIME() FUNCTION, https://github.com/nesbox/TIC-80/wiki/time
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

# TIC-80'S TSTAMP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/tstamp
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

# TIC-80'S TRACE() FUNCTION, https://github.com/nesbox/TIC-80/wiki/trace
def trace(message, color=15):
    """
    Usage:
            trace message [color]
    Parameters:
            message : the message to print in the console.
            color : the index of a color in the current palette (0..n)
    Description:
            This is a service function, useful for debugging your code. It prints the message parameter to the console in the (optional) color specified.
    """
    import builtins
    
    if os.name == 'nt':
        builtins.print(str(message))
    else:
        builtins.print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(*_TIC["PALETTE"][color%len(_TIC["PALETTE"])], str(message)))

# TIC-80'S TRI() FUNCTION, https://github.com/nesbox/TIC-80/wiki/tri
def tri(x1, y1, x2, y2, x3, y3, color):
    """
    Usage:
            tri x1 y1 x2 y2 x3 y3 color
    Parameters:
            x1, y1 : the coordinates of the first triangle corner
            x2, y2 : the coordinates of the second corner
            x3, y3 : the coordinates of the third corner
            color: the index of the desired color in the current palette
    Description:
            This function draws a triangle filled with color, using the supplied vertices.
    """
    pygame.draw.polygon(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [(x1, y1), (x2, y2), (x3, y3)])

# TIC-80'S TRIB() FUNCTION, https://github.com/nesbox/TIC-80/wiki/trib
def trib(x1, y1, x2, y2, x3, y3, color):
    """
    Usage:
            trib x1 y1 x2 y2 x3 y3 color
    Parameters:
            x1, y1 : the coordinates of the first triangle corner
            x2, y2 : the coordinates of the second corner
            x3, y3 : the coordinates of the third corner
            color: the index of the desired color in the current palette
    Description:
            This function draws a triangle border with color, using the supplied vertices.
    """
    pygame.draw.polygon(_SCREEN, _TIC["PALETTE"][color%len(_TIC["PALETTE"])], [(x1, y1), (x2, y2), (x3, y3)], 1)

#####################################
try:
    
    # do you useful stuff here
    
    while True:
        _KEY = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                _KEY = pygame.key.name(event.key)
        
        _TIC["CLOCK"].tick(60)
        
        # do you TIC() stuff here

        pygame.display.flip()
except Exception:
    import traceback
    
    traceback.print_exc()
    
    pygame.quit()
    sys.exit()

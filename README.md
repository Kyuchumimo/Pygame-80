# Pygame-80

![](https://user-images.githubusercontent.com/74131798/159044855-2366e15f-3730-4eab-b7f9-bc2c800cb9f6.gif)

A set of functions from TIC-80 tiny computer 0.90.1723 platform ported to Pygame 2. Many of them are designed to work with the NumPy library to improve performance, per pixel access and CSV files access.   

Some of the highlights of using this library are:  
* TIC-80 friendly  
* Highly customizable (any screen resolution, different screen modes, any number of audio channels, custom FPS)  
* Python as the main programming language  
* Practically no memory restrictions regarding the number of assets that can be used (code size, tilesets, spritesheets, music, sfx, color palette)  
* Expandable with the use of modules and libraries  
* Support of multiple audio and image formats  

## Dependencies
```
pip install pygame==2.1.3.dev6
pip install numpy
```
## Functions
### Functions available so far:  
**btn**: use pygame.key.get_pressed & **btnp**: use pygame.event.get(pygame.KEYDOWN)  
**clip**: use pygame.Surface.set_clip  
**cls**: use pygame.Surface.fill  
**circ & circb**: use pygame.draw.circle  
**elli & ellib**: use pygame.draw.elipse  
**exit (⚠️: sys built-in module dependant)**: use sys.exit  
**font**: use pygame.Surface.subsurface and pygame.transform.scale  
**key**: use pygame.key.get_pressed & **keyp**: use pygame.event.get(pygame.KEYDOWN)  
**line**: use pygame.draw.line  
**map (⚠️: numpy library dependant)**: use pygame.Surface.subsurface and pygame.transform.scale  
**mget & mset**: VRAM 2D array indexing, read/write  
**mouse**: use pygame.mouse.get_pos, pygame.mouse.get_pressed and MOUSEWHEEL event  
**music (⚠️: sustain parameter not supported)**: use pygame.mixer.music.load, pygame.mixer.music.play and pygame.mixer.music.stop  
**pix (⚠️: numpy library dependant)**: use pygame.surfarray.pixels3d  
**pmem (⚠️: os, sys, json module dependant)**: use os.path.splitext, sys.argv, json.load and json.dump  
**print**: use pygame.font.Font  
**rect & rectb**: use pygame.draw.rect  
**reset (⚠️: os, sys module dependant)**: use os.execv  
**sfx (⚠️: note and speed parameters not supported by Pygame)**: use pygame.mixer.Sound, pygame.mixer.Channel and pygame.mixer.Sound.set_volume  
**spr**: use pygame.Surface, pygame.Surface.subsurface, pygame.transform.flip, pygame.transform.scale and pygame.transform.rotate  
**sync**: use pygame.image.load, pygame.image.save, numpy.loadtxt and numpy.savetxt  
**textri**: use pygame.surfarray.array3d, pygame.Surface.get_size, pygame.surfarray.make_surface  
**time**: use pygame.time.get_ticks  
**trace (⚠️: builtins built-in module dependant)**: use builtins.print with ANSI escape sequences for RGB color  
**tri & trib**: use pygame.draw.polygon  
**tstamp (⚠️: time built-in module dependant)**: use time.time

### Some excluded features:  
**TIC, SCN, OVR, BDR**: Callbacks  
**peek & peek4, poke & poke4, memcpy & memset**: Memory Mapping  
**fset & fget**: Sprite flags  
**Blit Segment / Low BPP graphics**: Bit depth

## Special thanks:  
This library and other projects would not have been possible without the generous help of Pygame Community Discord members, either directly or indirectly:  
**@Starbuck**  
**@Ghast**  
**@blubberquark**  
**@Matt**  
**@Axis**

# Pygame-80

![pygame80](https://user-images.githubusercontent.com/74131798/137247572-a0919aa6-76d7-4139-a688-234a28cfc4d0.gif)

A set of functions from TIC-80 tiny computer platform ported to Pygame>=2.0.1. Many of them are designed to work with the NumPy library to improve performance, per pixel access and CSV files access.  

Some of the highlights of using this library are:  
* TIC-80 friendly  
* Highly customizable (any screen resolution, different screen modes, any number of audio channels, custom FPS)  
* Python as programming language  
* Practically no memory restrictions regarding the number of assets that can be used (code size, tilesets, spritesheets, music, sfx, color palette)  
* Expandable with the use of modules and libraries  
* Support of multiple audio and image formats  

## Dependencies
```
pip install pygame
pip install numpy
```

To run the demo program, you can use Thonny IDE or GNU/Linux shell or Windows shell

- **Thonny IDE**: Open pygame80.py and press F5 or CTRL+R or CTRL+T
- **GNU/Linux shell**:~@ python3 /path/pygame80.py
- **Windows shell**: >python /path/pygame80.py

## Functions
### Functions available so far:  
**btn**: use pygame.key.get_pressed  
**cls**: use pygame.Surface.fill  
**circ & circb**: use pygame.draw.circle  
**elli & ellib**: use pygame.draw.elipse  
**exit (!: sys built-in module dependant)**: use pygame.quit and raise SystemExit  
**font**: use pygame.Surface.subsurface and pygame.transform.scale  
**key**: use pygame.key.get_pressed  
**line**: use pygame.draw.line  
**map**: use pygame.Surface.subsurface and pygame.transform.scale  
**mget & mset**: VRAM 2D array indexing, read/write  
**pix (!: numpy library dependant)**: use pygame.surfarray.pixels3d  
**print**: use pygame.font.Font  
**rect & rectb**: use pygame.draw.rect  
**sfx (!: note and speed parameters not supported by Pygame)**: use pygame.mixer.Sound, pygame.mixer.Channel and pygame.mixer.Sound.set_volume  
**spr**: use pygame.Surface, pygame.Surface.subsurface, pygame.transform.flip, pygame.transform.scale and pygame.transform.rotate  
**time**: use pygame.time.get_ticks  
**trace (!: builtins built-in module dependant)**: use builtins.print with ANSI escape sequences for RGB color  
**tstamp (!: time built-in module dependant)**: use time.time()  
**tri & trib**: use pygame.draw.polygon

### Some excluded functions:  
**TIC, SCN(n), OVR, BDR**: Callbacks  
**peek & peek4, poke & poke4, memcpy & memset**: Memory Mapping  
**fset & fget**: Sprite flags  

### To do list:  
- [ ] **btnp**: button input  
- [ ] **key & keyp**: keyboard input  
- [ ] **textri (!: pygame.gfxdraw library dependant)**: textured triangle  
- [ ] **mouse**: mouse input  
- [x] **TIC-80 smallfont**: system font variant  
- [x] **pix (!: numpy library dependant)**: per pixel read or write access  
- [ ] **sync**: function for asset management (!: important)  
- [ ] **wiki (23/26)**: for show examples and tutorials  

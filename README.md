# Pygame-80

![pygame80](https://user-images.githubusercontent.com/74131798/137247572-a0919aa6-76d7-4139-a688-234a28cfc4d0.gif)

A set of functions from TIC-80 tiny computer platform ported to Pygame 2 + Python 3.7+. Many of them are designed to work with the NumPy library to improve performance, per pixel access and CSV files access.  

**THIS LIBRARY IS STILL UNDER DEVELOPMENT, SO THE BEHAVIOR OF THE FUNCTIONS MAY CHANGE OVER TIME, WAIT UNTIL A STABLE VERSION IS RELEASED**  

Some of the highlights of using this library are:  
* TIC-80 friendly  
* Highly customizable (any screen resolution, different screen modes, any number of audio channels, custom FPS)  
* Python as the main programming language  
* Practically no memory restrictions regarding the number of assets that can be used (code size, tilesets, spritesheets, music, sfx, color palette)  
* Expandable with the use of modules and libraries  
* Support of multiple audio and image formats  

## Dependencies
```
pip install pygame
pip install numpy
```

To run the demo program, you can use a GNU/Linux shell or Windows shell

- **GNU/Linux shell**:~$ python3 pygame80.py pythondemo.py
- **Windows shell**: >python pygame80.py pythondemo.py

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
**music (⚠️: sustain, tempo and speed parameters not supported by Pygame)**: use pygame.mixer.music.load, pygame.mixer.music.play and pygame.mixer.music.stop  
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
**peek, peek4, peek1, peek2, poke, poke4, poke1, poke2, memcpy & memset, vbank**: Memory Mapping  
**fset & fget**: Sprite flags  
**Blit Segment / Low BPP graphics**: Bit depth  
**16 color palette**

### To do list:  
- [ ] **handling of Assert Statement and Try Except Statement**

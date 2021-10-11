# Pygame-80

![pygame80 cover](https://user-images.githubusercontent.com/74131798/136860145-dad00473-008c-47e4-a385-e338accfc1ef.png)

A set of functions from TIC-80 tiny computer platform ported to Pygame 2.0.1. Many of them are designed to work with the numpy library to improve performance and per pixel access.  

Some of the highligts of using this library are:
*TIC-80 friendly
*Highly customizable (any screen resolution, different screen modes, any number of audio channels)
*Python as a programming language
*Practically no memory restrictions regarding the number of assets that can be used (tilesets,spritesheets,music,sfx)
*Expandable with the use of modules and libraries
*Support of multiple audio and image formats

Functions available so far:  
btn: use pygame.key.get_pressed  
cls: use pygame.Surface.fill  
circ & circb: use pygame.draw.circle  
elli & ellib: use pygame.draw.elipse  
exit: use pygame.quit and raise SystemExit  
font: use pygame.Surface.subsurface and pygame.transform.scale  
line: use pygame.draw.line  
map: use pygame.Surface.subsurface and pygame.transform.scale  
print: use pygame.font.Font
rect & rectb: use pygame.draw.rect  
spr: use pygame.Surface, pygame.Surface.subsurface, pygame.transform.flip, pygame.transform.scale and pygame.transform.rotate
trace (builtins module dependant!): use builtins.print with ANSI escape sequences for RGB color

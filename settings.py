#import pygame
#creates the level layout 
level_map = [
'X                                                                         X',
'X                                                                         X',
'X                     CC                     C         C            CC    X',
'X           C        XXXXXX         XXXX             XXXX        XXXX     X',
'X          XXX  C              C                C                        XX',
'X       XXX   XXX             XXX              XX                   C     X',
'X                                                    XXXXXX      XXXXX    X',
'XPC         C         XXXXX          XXCXXXX         XXXXXX    XXXXXXX   XX',
'XXXX       XX        XXXXXXX         XXCXXXX         XXXXXX    XXXXXXX    X',
'XXXX      CXX    XX  XXXXXXX         XXCXXXXX       XXXXXXXX   XXXXXXXX   X',
'XXXX      XXXX   X   CXXXXXXX         CCXXXXXX  C   XXXXXXXX C XXXXXXXX   X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 32
screen_width = 600
screen_height = len(level_map) * tile_size


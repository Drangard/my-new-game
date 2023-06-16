#import pygame
#creates the level layout 
level_map = [
'X                                                                         ',
'X                                                                         ',
'X                                                                         ',
'X        XXXX            XXXX   XX   XXXX     XX     XXX XX   XXX   XXXX  ',
'X                XX    XXXX         XX        XX      XXXX    XX    XXXX  ',
'X     XX                                       XX      XXX   XXXX   XXXX  ',
'X                  XXX        XXXXX       XX       XX  XXXX  XXXX   XXXX  ',
'X P                      XX                                         XXXX  ',
'XXXXXX    XXX         XXXXX    XXX   XX    X     XX      XXX     XXXXXXX  ',
'XXXXX    XXXXX     XXXX   XXX  XXXX  XX   XXX    XXXXX   XXX    XXXXXXXX  ',
'XXX     XX   XX  XXX      XXX   XXX  XX  XXXXX   XXX X   XXX   XXXXXXXXX  ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 32
screen_width = 600
screen_height = len(level_map) * tile_size


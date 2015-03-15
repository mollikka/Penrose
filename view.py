from math import sin,atan2,sqrt,pi
import pygame

from model import HalfDart, HalfKite

def draw_model(surf,model,offx,offy,scale,draw_options):
    dart_color = draw_options["dart_color"]
    dart_texture = draw_options["dart_texture"]
    kite_color = draw_options["kite_color"]
    kite_texture = draw_options["kite_texture"]
    drawmode = draw_options["drawmode"]
    background_color = draw_options["background_color"]

    surf.fill(background_color)

    if drawmode == "texture":
        for tile in model.get_tiles():
            if tile.__class__ == HalfDart:
                draw_tile_texture(surf, tile, dart_texture, offx, offy, scale)
            if tile.__class__ == HalfKite:
                draw_tile_texture(surf, tile, kite_texture, offx, offy, scale)

    elif drawmode == "solid":
        for tile in model.get_tiles():
            if tile.__class__ == HalfDart:
                draw_tile_color(surf, tile, dart_color, offx, offy, scale)
            if tile.__class__ == HalfKite:
                draw_tile_color(surf, tile, kite_color, offx, offy, scale)

def draw_tile_color(surf, tile, color, offx, offy, scale):
    a,b,c = tile.a,tile.b,tile.c

    a = a[0]*scale + offx, a[1]*scale + offy
    b = b[0]*scale + offx, b[1]*scale + offy
    c = c[0]*scale + offx, c[1]*scale + offy

    pygame.draw.polygon(surf, color, [a,b,c])

def draw_tile_texture(surf, tile, texture, offx, offy, scale):
    a,b,c = tile.a, tile.b, tile.c

    a = a[0]*scale + offx, a[1]*scale + offy
    b = b[0]*scale + offx, b[1]*scale + offy
    c = c[0]*scale + offx, c[1]*scale + offy

    bx, by = b
    cx, cy = c
    centerx, centery = (bx+cx)/2, (by+cy)/2

    if tile.__class__ == HalfDart:
        ang = atan2(bx-cx,by-cy)*180/pi + 90
        dist = sqrt((bx-cx)**2 + (by-cy)**2) * (sin(108*pi/180) / sin(36*pi/180))
    elif tile.__class__ == HalfKite:
        ang = atan2(bx-cx,by-cy)*180/pi - 90
        dist = sqrt((bx-cx)**2 + (by-cy)**2)

    ratio = texture.get_rect().width/float(texture.get_rect().height)

    texture = pygame.transform.rotozoom(texture, ang, dist/texture.get_rect().width)

    drawx = centerx - texture.get_rect().width / 2
    drawy = centery - texture.get_rect().height / 2

    surf.blit(texture,(drawx,drawy))

def load_textures(kite_tex_file, dart_tex_file):
    kite_texture = pygame.image.load(kite_tex_file)
    dart_texture = kite_texture.copy()
    dart_texture.fill((0,0,0,0))
    dart_texture.blit(pygame.image.load(dart_tex_file),(0,0),None,)
    return kite_texture, dart_texture

def start_window(w,h):
    winflags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE
    window=pygame.display.set_mode((w,h),winflags)
    window.fill((30,30,30))
    return window

import sys
import pygame

from model import PenroseModel
from start_states import dart_star
from view import draw_model, load_textures, start_window

def interactive_mode(win_width,win_height):

    window = start_window(win_width,win_height)

    offx = win_width/2
    offy = win_height/2
    scale = min(win_width,win_height)/2

    model = PenroseModel(dart_star())
    kite_texture,dart_texture = load_textures("images/kite_tex.png","images/dart_tex.png")

    draw_options =  {}
    draw_options["dart_color"] = (0,0,128)
    draw_options["dart_texture"] = dart_texture
    draw_options["kite_color"] = (128,0,0)
    draw_options["kite_texture"] = kite_texture
    draw_options["drawmode"] = "solid"
    draw_options["background_color"] = (30,30,30)

    draw_model(window,model,offx,offy,scale,draw_options)

    while True:

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    model.split()
                    draw_model(window,model,offx,offy,scale,draw_options)
                if event.key == pygame.K_l:
                    model.desplit()
                    draw_model(window,model,offx,offy,scale,draw_options)
                if event.key == pygame.K_t:
                    draw_options["drawmode"] = "texture"
                    draw_model(window,model,offx,offy,scale,draw_options)
                if event.key == pygame.K_y:
                    draw_options["drawmode"] = "solid"
                    draw_model(window,model,offx,offy,scale,draw_options)

if __name__ == "__main__":
    interactive_mode(600,600)

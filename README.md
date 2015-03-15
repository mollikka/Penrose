# Penrose Tiling Renderer

Requires Python and Pygame to run. Tested with Python 2.7.6 and Pygame 1.9.1.

Run the program with `python interactive_mode.py`.

To create something more specific, you'll want to create your own script. Initialize with:
```python
from model import PenroseModel
from starting_states import dart_star
from view import load_textures, draw_model

#Penrose model takes initial set of tiles as the argument. Look at starting_states.py for examples.
model = PenroseModel(dart_star())

#calculate the forth iteration
for i in range(4): model.split()

kite_texture,dart_texture = load_textures("images/kite_tex.png","images/dart_tex.png")
```

After this you can call `draw_model(surf,model,offx,offy,scale,draw_options)`, where `surf` is a Pygame Surface.
offx, offy and scale specify location and scale on the surface. The exact effect of these depend on the initial state.
I recomment having model coordinates in the [-1,1] range for easy placement.

draw_options is a dict:
```python
draw_options["dart_color"] = (0,0,128)        #rgb color of darts if using solid coloring
draw_options["dart_texture"] = dart_texture   #texture of darts if in texture mode
draw_options["kite_color"] = (128,0,0)        #rgb color of kites if using solid coloring
draw_options["kite_texture"] = kite_texture   #texture of kites if in texture mode
draw_options["drawmode"] = "solid"            #"solid" or "texture"
draw_options["background_color"] = (30,30,30) #background rgb color
```

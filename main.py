import tkinter as tk
import pyperclip
from datetime import datetime

from main_screen_utils import *
from plugboard_utils import *
from logic import *
from import_export_config import *

plugboard = {}
qwerty_keys = []
qwerty_plugs = []
io_buttons = []

press_data = {
  "last_mouse_click": datetime.now(),
  "last_key_press": datetime.now(),
  "last_key":"",
  "last_output":"",
  "threshold":0.55,
  "showing_keyboard":True,
  "lonely_plug":None
}
since_last_press = lambda: (datetime.now() - press_data['last_key_press']).total_seconds()
since_last_click = lambda: (datetime.now() - press_data['last_mouse_click']).total_seconds()


# Tkinter setup
root = tk.Tk()
root.title("Enigma Machine")
root.geometry(f"{width}x{height}")
root.configure(bg=BG)
root.resizable(False, False)
canvas = tk.Canvas(root, bg=BG, width=width, height=height)


# User Interaction Functions
def key_down(e):
  # Process a key press to verify it and change a key accordingly
  if hasattr(e, 'char') and e.char.upper() in alphabet and e.char:
    if since_last_press() > press_data['threshold'] or e.char.upper() != press_data['last_key']:
      result = choose(e.char.upper(), plugboard)
      time = '{:0>5}'.format("{:.2f}".format((t if (t:= since_last_press()) < 100 else 99.99)))
      print(f"key down - {time} - {e.char.upper()}: {result}")
      
  
      if press_data['last_key'] != "":
        index = qwerty_letters.index(press_data["last_output"])
        change_brightness = press_data["last_output"] == result
        qwerty_keys[index].update(change_brightness = change_brightness)
      
      rotate(canvas)
      
      press_data["last_output"] = result
      press_data["last_key"] = e.char.upper()
      qwerty_keys[qwerty_letters.index(result)].update()
    
    press_data['last_key_press'] = datetime.now()
    
# Run program
def change_screen(e):
  # Switch between keyboard and plugboard
  main_screen = press_data["showing_keyboard"]
  if (main_screen and e.y >= height - plugboard_handle_height) or (not main_screen and e.y <= plugboard_handle_height):
    # Delete all canvas objects
    canvas.delete('all')
    press_data["showing_keyboard"] = not press_data["showing_keyboard"]
    if press_data["lonely_plug"]:
      # Clear any lonely plugs
      press_data["lonely_plug"].active = False
      press_data["lonely_plug"] = None
    main_screen = press_data["showing_keyboard"]

    if io_buttons:
      # Clear import/export buttons
      for i in range(2):
        io_buttons[0].destroy()
        io_buttons.pop(0)
      
    # Draw appropriate screen
    if main_screen:
      draw_rotors(canvas)
      draw_keyboard(canvas, qwerty_keys)
      draw_buttons(canvas, io_buttons, lambda: import_button(rotors, plugboard), lambda: export_button())
      draw_plugboard_handle(canvas)
    else:
      draw_plugboard_handle(canvas, top=True)
      draw_plugs(canvas, qwerty_plugs, plugboard)
      draw_connections(canvas, plugboard)

def plug_clicks(e):
  # Process plugboard clicks to make connections
  for plug_hole in qwerty_plugs:
    x0, y0, x1, y1 = plug_hole.hitbox
    pad = 7
    if e.x in range(x0 - pad, x1 + pad) and e.y in range(y0 - pad, y1 + pad):
      # Toggle the white circle
      plug_hole.update()

      if plug_hole.letter in plugboard:
        # Plug already connected, unplug it
        other_end = qwerty_plugs[alphabet.index(plugboard[plug_hole.letter])]
        other_end.update()
        unplug(plug_hole.letter, plugboard)
        draw_connections(canvas, plugboard)
      else:
        # No complete connection exists yet
        
        if press_data["lonely_plug"]:
          # One end of the connection is in
          if press_data["lonely_plug"].letter != plug_hole.letter:
            # Connect 2 distinct letters
            plug(press_data["lonely_plug"].letter, plug_hole.letter, plugboard)
            draw_connections(canvas, plugboard)
            
          # Either the connection has been completed or the first end of the connection has been clicked again
          press_data["lonely_plug"] = None
        else:
          # Put in the first end of the connection
          press_data["lonely_plug"] = plug_hole
          
      break
        
def rotor_clicks(e):
  start_x, start_y = (width - rotor_square_size * 6) / 2, 20
  get_x_range = lambda col: range(x:= int(start_x + col * rotor_square_size * 2.5), x+rotor_square_size)
  get_y_range = lambda row: range(y:= start_y + row * rotor_square_size, y + rotor_square_size)

  for row in [0, 2]:
    if e.y in get_y_range(row):
      # Rotating up or down
      rotate_down = row == 2
      for rot in range(3):
        if e.x in get_x_range(rot):
          # rot is the rotor clicked
          # amount = 1 -> rotating the rotor downwards
          rotate(canvas, amount= 1 if rotate_down else -1, rotor= rot)
 
def mouse_down(e):
  if since_last_click() > press_data["threshold"] * 0.2:
    # Call all functions that use mouse down events
    change_screen(e)
    if press_data["showing_keyboard"]:
      rotor_clicks(e)
    else:
      plug_clicks(e)

  press_data['last_mouse_click'] = datetime.now()

def import_button(rotors, plugboard):
  if not pyperclip.paste():
    return
  
  new_rotors, new_plugboard = import_config(pyperclip.paste())
  for i, rot in enumerate(new_rotors):
    rotors[i] = rot
  draw_rotors(canvas)

  plugboard.clear()
  plugboard.update(new_plugboard)

def export_button():
  pyperclip.copy(export_config(rotors, plugboard))
      
draw_rotors(canvas)
draw_keyboard(canvas, qwerty_keys)
draw_plugboard_handle(canvas)
draw_buttons(canvas, io_buttons, lambda: import_button(rotors, plugboard), lambda: export_button())
root.bind('<KeyPress>', key_down)
root.bind('<Button-1>', mouse_down)
canvas.pack()
root.mainloop()

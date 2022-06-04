# 000ABCDEF
# 3 digits representing 3 rotor positions
# 0-13 pairs of letters

import re
from plugboard_utils import plug
import tkinter as tk

def import_config(code):
  # Check to make sure code matches format
  if re.search("(\d{1,2},){3}([a-zA-Z]{2}){0,13}", code):
    raw_nums = re.search("(\d{1,2},){3}", code).group(0)
    rotors = [int(num) for num in raw_nums.split(",") if num]
    code = code[len(raw_nums):].upper()
    plugboard = {}
    while code:
      plug(code[0], code[1], plugboard)
      code = code[2:]
    return [rotors, plugboard]
  else:
    return [[0, 0, 0], {}]

def export_config(rotors, plugboard):
  rotor_nums = ",".join([str(num) for num in rotors]) + ","
  connections = "".join([f"{key}{plugboard[key]}" for key in list(plugboard.keys())[::2]])
  return rotor_nums + connections

def draw_buttons(canvas, io_buttons, im, ex):
  font = (f"Arial {8} bold")
  import_button = tk.Button(canvas, text="Import setup", font=font, command=im)
  export_button = tk.Button(canvas, text="Export setup",font=font, command=ex)
  io_buttons.append(import_button)
  io_buttons.append(export_button)
  import_button.place(x=20, y=20)
  export_button.place(x=20, y=60)
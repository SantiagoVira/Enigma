from string import ascii_uppercase as alphabet

# Enigma variables
rotors = [0,0,0]
rotor_wirings = [
  "DMTWSILRUYQNKFEJCAZBPGXOHV",     
  "HQZGPJTMOBLNCIFDYAWVEUSRKX", 
  "UQNTLSZFMREHDPXKIBVYGJCWOA"
]
reflector = list(rotor_wirings[-1][::-1])

# UI variables
qwerty = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
qwerty_letters = "".join(qwerty)
plugs_qwerty = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ"]
rotor_square_size = 25
plugboard_handle_height = 45

# Tkinter constants
width = 700
height = 400
BG = "#737373"
KEY_INACTIVE = "#333333"
KEY_ACTIVE = "#f0ff66"
KEY_BRIGHTER = "#faffc7"

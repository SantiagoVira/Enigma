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

# key down - 02.11 - H: X
# key down - 00.91 - E: D
# key down - 02.00 - L: O
# key down - 01.12 - L: E
# key down - 02.21 - O: I
# key down - 01.15 - W: M
# key down - 01.98 - O: E
# key down - 01.21 - R: M
# key down - 01.17 - L: S
# key down - 00.97 - D: A

# key down - 15.74 - H: X
# key down - 00.99 - E: D
# key down - 01.14 - L: U
# key down - 00.83 - L: J
# key down - 01.01 - O: I
# key down - 02.30 - W: M
# key down - 00.65 - O: E
# key down - 00.47 - R: M
# key down - 00.45 - L: D
# key down - 00.39 - D: L

# 0,23,24,ABCD
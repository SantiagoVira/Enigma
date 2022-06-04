from logic import *

class Key:
  '''
  Draws a circle on the canvas at the given coordinates to represent a key on a keyboard
  '''
  radius = 30
  font_size = 22

  def __init__(self, x, y, letter, canvas):
    # Store the variables and draw the circle for the first time
    self.x = x
    self.y = y
    self.letter = letter
    self.canvas = canvas
    self.on = False
    self.brighter = False

    self.draw()

  def draw(self):
    # Draws the circle and text
    x0 = self.x - Key.radius
    y0 = self.y - Key.radius
    x1 = self.x + Key.radius
    y1 = self.y + Key.radius

    self.clear()
    
    self.circle = self.canvas.create_oval(x0, y0, x1, y1, fill=(KEY_ACTIVE if not self.brighter else KEY_BRIGHTER) if self.on else KEY_INACTIVE, width=0)
    self.text = self.canvas.create_text(self.x, self.y, text=self.letter, fill=KEY_INACTIVE if self.on else BG, font=(f"Arial {Key.font_size} bold"))

  def clear(self):
    # Clears any previous drawing of a key
    if hasattr(self, "circle") and self.circle:
      self.canvas.delete(self.circle)
    if hasattr(self, "text") and self.text:
      self.canvas.delete(self.text)

  def update(self, change_brightness = False):
    # Update the state of a key
    self.on = not self.on

    
    if change_brightness:
      self.brighter = not self.brighter
    if not self.on and not change_brightness:
      self.brighter = False

    self.draw()

def draw_keyboard(canvas, qwerty_keys): 
  # Draw the keyboard
  for r, row in enumerate(qwerty):
    for c, letter in enumerate(row):
      # Spacing based on first row, padding based on centering rows
      spacing = (width - (20 * Key.radius)) / 11
      padding = (width - ((2 * Key.radius * len(row)) + spacing * (len(row) - 1))) / 2
      vert_start = 120
      x = padding + Key.radius + (2 * Key.radius + spacing) * c
      y = vert_start + spacing + Key.radius + (2 * Key.radius + spacing) * r
      qwerty_keys.append(Key(x, y, letter, canvas))

def draw_rotor_square(x, y, canvas, border = False):
  # Draw a square for the rotors
  return canvas.create_rectangle(x , y, x+rotor_square_size - int(border), y+rotor_square_size, width = int(border), fill=KEY_INACTIVE)

def draw_rotors(canvas):
  # Draw the rotors and their values
  
  start_x, start_y = (width - rotor_square_size * 6) / 2, 20
  for column in range(3):
    for row in range(3):
      row_val = [0, 2, 1][row]
      x, y = start_x + column * rotor_square_size * 2.5, start_y + row_val * rotor_square_size
      draw_rotor_square(x, y, canvas, border = row_val == 1)

      letter = turn(rotors[column] - row_val + 1, rotor_wirings[column])[0]
      canvas.create_text(x + rotor_square_size / 2, y + rotor_square_size / 2, text=letter, fill=BG, font=(f"Arial 12 bold"))

# Logic
def turn(amount, order, down=True): # Function to show
  # "Turn" a rotor by a certain amount to get the letter the rotor would output
  # Return the rotor list of letters
  letters = list(order)
  if amount < 0:
    down = False
    amount = abs(amount)
    
  for i in range(amount):
    if down:
      letters.insert(0, letters.pop())
    else:
      letters.append(letters.pop(0))

  return letters

def rotate(canvas, amount=1, rotor=-1):
  # "Rotate" the rotor(s) to change their future outputs
  if rotor == -1:
    # Rotating all, not setting a specific orientation
    rotors[0] += 1
    if rotors[0] % len(alphabet) == 0:
        rotors[1] += 1
        if rotors[1] % len(alphabet) == 0 and rotors[1] != 0:
          rotors[2] += 1
          rotors[1] = 0
        rotors[0] = 0
  elif rotor in range(0, 3):
    # Setting rotation
    rotors[rotor] += amount
    if rotors[rotor] % len(alphabet) == 0:
      rotors[rotor] = 0
    elif rotors[rotor] < 0:
      rotors[rotor] = len(alphabet)

  draw_rotors(canvas)
  
def choose(letter, plugboard):
  # Put a given letter through the rotors and reflectors, return the output
  if letter in alphabet:
    letter = letter.upper()
  else:
    return ""

  if letter in plugboard:
    letter = plugboard[letter]
    
  indices = [letter]
  for j in range(2):
    for i in range(3):
      # Turn a rotor to the current position it is at
      # Get the letter at the same index (Ex. turned 3 down, A -> X)
      indices.append(turn(rotors[i], rotor_wirings[i], down = j==0)[rotor_wirings[i].index(indices[-1])])
    if j == 0:
      # Same process but in a reversed version of the alphabet
      indices.append(reflector[rotor_wirings[i].index(indices[-1])])

  final = indices[-1]
  if final in plugboard:
    final = plugboard[final]
  return final


from logic import *

class Plug:
  '''
  Draws a pill shape on the canvas at the given coordinates to represent a plug for the plugboard
  '''
  radius = 17
  font = (f"Arial {15} bold")

  def __init__(self, x, y, letter, canvas, plugboard):
    # Store the variables and draw the circle for the first time
    self.x = x
    self.y = y
    self.letter = letter
    self.active = letter in plugboard
    self.canvas = canvas

    self.draw()

  def draw(self):
    # Draws the circle and text
    # Main coordinates
    x0 = self.x
    y0 = self.y
    x1 = self.x - Plug.radius
    y1 = self.y - Plug.radius
    x2 = self.x + Plug.radius
    y2 = self.y + Plug.radius
    y3 = y2 + Plug.radius

    # Smaller circle coordinates
    x0_1 = int(self.x - (1/2) * Plug.radius)
    y0_1 = int(self.y + (1/2) * Plug.radius)
    x1_1 = int(self.x + (1/2) * Plug.radius)
    y1_1 = int(self.y + (3/2) * Plug.radius)
    self.hitbox = [x0_1, y0_1, x1_1, y1_1]

    # Smallest circle coordinates
    x0_2 = self.x - (1/4) * Plug.radius - 1
    y0_2 = self.y + (3/4) * Plug.radius 
    x1_2 = self.x + (1/4) * Plug.radius - 1
    y1_2 = self.y + (5/4) * Plug.radius 

    # Settings
    settings0 = {"fill":BG, "width":0}
    settings1 = {"fill":"black", "width":0}
    self.clear()
    
    self.circle1 = self.canvas.create_oval(x1, y1, x2, y2, **settings0)
    self.circle2 = self.canvas.create_oval(x1, y0, x2, y3, **settings0)
    self.square = self.canvas.create_rectangle(x1, y0, x2, y2, **settings0)
    self.circle3 = self.canvas.create_oval(x0_1, y0_1, x1_1, y1_1, **settings1)
    if self.active:
      self.circle4 = self.canvas.create_oval(x0_2, y0_2, x1_2, y1_2, fill="white")
    self.text = self.canvas.create_text(x0, y0 - 3, text=self.letter, fill=KEY_INACTIVE, font=Plug.font)

  def clear(self, off=False):
    # Clears any previous drawing of a plug
    if off:
      # Clearing screen
      self.active = False
    try:
      for shape in [self.circle1, self.circle2, self.circle3, self.circle4, self.square, self.text]:
        self.canvas.delete(shape)
    except:
      # Not initialized yet
      pass

  def update(self):
    # Update the state of a plug
    self.active = not self.active
    self.draw()
    


def draw_plugboard_handle(canvas, top = False):
  # Draw the section to change to the plugboard view
  start = height-plugboard_handle_height if not top else 0
  canvas.create_rectangle(0, start, width, height, fill=KEY_INACTIVE, width=0)
  if top:
    canvas.create_line(0, plugboard_handle_height, width, plugboard_handle_height)
  hx, hy = width/2, (height - plugboard_handle_height / 2 + 5 if not top else plugboard_handle_height - 12.5)
  hw, hh = 30, 20
  canvas.create_arc(hx-hw, hy-hh, hx+hw, hy+hh, start=0, extent=180, fill=BG, width=0)

def draw_plugs(canvas, qwerty_plugs, plugboard):
  
  sizes = [4, 5, 6, 5, 6]
  for r, size in enumerate(sizes):
    for c in range(size):
      # Spacing based on first row, padding based on centering rows
      letter = alphabet[sum(sizes[:r]) + c]
      area = (3 * width / 4 - 5, height - 1.2 * plugboard_handle_height)
      
      spacing = (area[0] - (12 * Plug.radius)) / 7
      padding = (area[0] - ((2 * Plug.radius * size) + spacing * (size - 1))) / 2
      vert_start = plugboard_handle_height / 2 - 15
      x = padding + Plug.radius + (2 * Plug.radius + spacing) * c
      y = vert_start + spacing + Plug.radius + (Plug.radius + spacing) * r
      qwerty_plugs.append(Plug(x, y, letter, canvas, plugboard))

def draw_connections(canvas, plugboard):
  # Draw a layout of all letters with an area to represent current conections on the right
  connections = [f"{key} {'-'*10} {plugboard[key]}" for key in list(plugboard.keys())[::2]]
  connections_string = "\n".join(connections)

  rect_x, rect_y = 3*width/4 + 5, plugboard_handle_height + 10
  text_x, text_y = (rect_x + width - 10) / 2, rect_y + 12 * len(connections) + 5
  canvas.create_rectangle(rect_x, rect_y, width - 10, height - 10, fill="#fff")
  canvas.create_text(text_x, text_y, text=connections_string, fill="#000", font=Plug.font, justify="center")

  
def plug(a, b, plugboard):
  # Add a new pair of connections to the plugboard
  plugboard.update({a:b, b:a})

def unplug(a, plugboard):
  # Remove a pair of connections from the plugboard
  plugboard.pop(plugboard[a])
  plugboard.pop(a)
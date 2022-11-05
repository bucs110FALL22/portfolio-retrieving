class Rectangle: 
  def __init__(self, x, y, h, w): 
    """
    initializes rectangle
	  args: int x, int y, int h, int w
	  """
    if x < 0: 
      x = 0
    if y < 0:
      y = 0
    if h < 0: 
      h = 0
    if w < 0: 
      w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  def  __str__(self): 
    """
    provides rectangle information
	  args: none
	  return: string for x,y, width and height values
    """
    return "(x :" , self.x,  "y :", self.y,")",  "width:", self.width, "height:", self.height

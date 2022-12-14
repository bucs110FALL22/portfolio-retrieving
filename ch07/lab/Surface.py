from Rectangle import Rectangle
class Surface:
  def __init__(self, filename, x, y, h, w):
    """
    initializes surface
	  args: filename, x, y, h, w
	  """
    self.rect = Rectangle (x,y,h,w)
    self.image = filename
  def getRect(self):
    """
    provides rectangle
	  args: none
	  return: returns rectangle
    """
    return self.rect
    
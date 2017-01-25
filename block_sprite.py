import pygame as pg


class BlockType:
    UNBREAKABLE = 0
    COLOR = 1
    PAINT = 2
    DIAMOND = 3
    SKULL = 4
    KEY = 5
    LOCK = 6
    REVERSE = 7


class BlockSprite(pg.sprite.Sprite):

  def __init__(self, blocktype, color, size, loc=[0,0], group=None):
    pg.sprite.Sprite.__init__(self, group)

    # TODO: Add blocktypes and corresponding styling
    self.blocktype = blocktype
    self.color = color
    self.size = (self.width, self.height) = size
    self.loc = list(loc)

    self._init_draw()

    # These variables hold new states for the Sprite.
    # When the update method is called, if any new_attr is defined,
    # the corresponding attributes are set to the new_ values.
    self.new_type = None
    self.new_color = None
    self.new_size = None
    self.new_loc = None


  def _init_draw(self):
    """defines image (surface) and rect (location) attributes 
    for use by a pg.sprite.Group"""
    self.image = pg.Surface(self.size)
    self.image.fill(self.color)
    pg.draw.rect(self.image, (60,60,60), self.image.get_rect(), 5) # This should draw a dark grey rectangle border.
    self.image.convert()

    self.rect = pg.Rect(self.loc, self.size)


  def setNewType(self, new_type):
    self.new_type = new_type
    
  def setNewColor(self, new_color):
    self.new_color = new_color

  def setNewSize(self, new_size):
    self.new_size = new_size

  def setNewLoc(self, new_loc):
    self.new_loc = new_loc


  def update(self):
    if self.new_type:
      self.blocktype = self.new_type
      self.new_type = None
    if self.new_color:
      self.color = self.new_color
      self.new_color = None
    if self.new_size:
      self.size = self.new_size
      self.new_size = None
    if self.new_loc:
      self.loc = self.new_loc
      self.new_loc = None

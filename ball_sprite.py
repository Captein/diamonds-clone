import pygame as pg


class BallSprite(pg.sprite.Sprite):

  def __init__(self, ball, group=None):
    pg.sprite.Sprite.__init__(self, group)

    self.color = ball.getColor()
    self.r = ball.getRadius()
    self.size = (self.width, self.height) = (2*self.r, 2*self.r)
    self.loc = ball.getLocation()

    self._init_draw()

    # These variables hold new states for the Sprite.
    # When the update method is called, if any new_attr is defined,
    # the corresponding attributes are assigned to the new_ values.
    self.new_color = None
    self.new_r = None
    self.new_loc = None


  def _init_draw(self):
    """defines image (surface) and rect (location) attributes 
    for use by a pg.sprite.Group"""
    self.image = pg.Surface(self.size)
    self.image.set_colorkey((0,0,0))
    self.image.convert_alpha()

    pg.draw.circle(self.image, self.color, (self.r, self.r), self.r)
    
    self.rect = pg.Rect(self.loc, self.size)


  def setNewColor(self, new_color):
    self.new_color = new_color

  def setNewRadius(self, new_r):
    self.new_r = new_radius

  def setNewLocation(self, new_loc):
    self.new_loc = new_loc


  def update(self):
    if self.new_color:
      self.color = self.new_color
      self.new_color = None
    if self.new_r:
      self.r = self.new_r
      self.new_r = None
    if self.new_loc:
      self.loc = self.new_loc
      self.new_loc = None

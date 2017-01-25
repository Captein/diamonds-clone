class Event:
  """A generic superclass for events that are passed to EventManager."""
  def __init__(self):
    self.name = 'generic event'



class TickEvent(Event):
  def __init__(self):
    self.name = 'cpu tick event'

class QuitEvent(Event):
  def __init__(self):
    self.name = 'quit event'


class LevelBuiltEvent(Event):
  """Raised when the model has built the level"""
  def __init__(self, level):
    self.name = 'level built event'
    self.level = level

class LevelStartEvent(Event):
  """Raised when the player starts the level"""
  def __init__(self, level):
    self.name = 'level start event'
    self.level = level

class BallMoveRequest(Event):
  """Raised when the controller identifies a keypress to move the ball"""
  def __init__(self, direction):
    self.name = 'ball move request'
    self.direction = direction
    self.distance = distance

class BallPlaceRequest(Event):
  """Raised when the ball is assigned a location (usually at the start of a level)"""
  def __init__(self, location):
    self.name = 'ball place request'
    self.location = location

class BallMoveEvent(Event):
  """Raised when the model registers a ball movement"""
  def __init__(self, ball):
    self.name = 'ball move event'
    self.ball = ball

class CollisionEvent(Event):
  """Raised when the ball collides with a block"""
  def __init__(self, ball, block):
    self.name = 'collision event'
    self.ball = ball
    self.block = block

class DebugEvent(Event):
  """Raised for any kind of debugging task or notification"""
  def __init__(self):
    self.name = 'debug event'
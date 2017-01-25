import listener
import event


class Ball(listener.Listener):
  """..."""

  def __init__(self, ev_manager, radius, color, 
                      loc=[0,0], direction='down'):

    listener.Listener.__init__(self, ev_manager)

    self.r = radius
    self.color = color
    self.loc = list(loc)
    self.direction = (-1 if (direction == 'up' or direction == -1) else 1)


  def move(self, direction, distance):
    """Modifies the ball's location and generates a BallMoveEvent."""
    
    if direction == 'left':
      self.loc[0] -= distance
    elif direction == 'right':
      self.loc[0] += distance
    elif direction == 'up':
      self.loc[1] -= distance
    elif direction == 'down':
      self.loc[1] += distance
    else:
      # invalid direction specified
      return

    self.ev_manager.post(event.BallMoveEvent(self))


  def place(self, loc):
    """Reassigns the ball's location and generates a BallMoveEvent."""

    self.loc = list(loc)

    self.ev_manager.post(event.BallMoveEvent(self))


  def changeDirection(self, direction=None):
    """Sets self.direction attribute if arg is given.
    Otherwise reverses the direction attribute."""

    if direction is not None:
      self.direction = (-1 if (direction == 'up' or direction == -1) else 1)
    else:
      self.direction *= -1


  def getRadius(self):
    return self.r

  def getColor(self):
    return self.color

  def getLocation(self):
    return self.loc

  def getDirection(self):
    return self.direction


  def notify(self, ev):
    if isinstance(ev, event.LevelStartEvent):
      # NB: The LevelStartEvent happens after the LevelBuiltEvent, which
      #     is triggered when the ball is built. The Ball should already
      #     have a direction and location. This overwrites it and places
      #     the ball, which will cause the View to draw it.
      self.changeDirection(ev.level.getStartDirection())
      self.ev_manager.post(event.BallPlaceRequest(ev.level.getStartLocation()))

    elif isinstance(ev, event.BallMoveRequest):
      self.move(ev.direction, ev.distance)

    elif isinstance(ev, event.BallPlaceRequest):
      self.place(ev.location)


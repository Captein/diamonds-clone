import listener
import event
import ball
import time


class Level(listener.Listener):
  """..."""

  def __init__(self, ev_manager, fps):
    listener.Listener.__init__(self, ev_manager)
    self.timer = time.time()
    self.fps = fps
    self.frametime = 1./fps  # The period per frame (in seconds)

    self.block_array = None # Data structure to hold the block objects.
    self.ball_start_loc = [0,0] # starting coordinates of the ball
    self.ball_start_direction = 'down' # starting direction of the ball ('up' or 'down')
    self.ball_start_color = (0, 0, 255) # starting color of the ball
    self.ball_radius = 10

    self.ball = None

    


  def build(self):

    # This may be a place to import level data like block arrangements
    # Once the game is big enough to support multiple levels.
    # It will be best to find a way to encode each level and translate it here.
    
    self.ball = ball.Ball(self.ev_manager, self.ball_radius,
                          self.ball_start_color, self.ball_start_loc,
                          self.ball_start_direction)

    self.ev_manager.post(event.LevelBuiltEvent(self))


  def getBall(self):
    return self.ball

  def getStartLocation(self):
    return self.ball_start_loc

  def getStartDirection(self):
    return self.ball_start_direction

  def getStartColor(self):
    return self.ball_start_color

  def getRadius(self):
    return self.ball_radius


  def notify(self, ev):
    if isinstance(ev, event.LevelStartEvent):
       # Resets the timer when the level starts.
      self.timer = time.time()

    elif isinstance(ev, event.TickEvent):
      if (time.time() - self.timer) >= self.frametime:
        

        # Resets the timer
        self.timer = time.time()

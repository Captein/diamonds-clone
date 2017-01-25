import listener
import event
import level
import ball


class Game(listener.Listener):
  """..."""

  STATE_BUILDING = 'building'
  STATE_RUNNING = 'running'
  STATE_PAUSED = 'paused'


  def __init__(self, ev_manager, fps=60):
    listener.Listener.__init__(self, ev_manager)

    self.state = Game.STATE_BUILDING

    self.level = level.Level(ev_manager, fps)


  def getLevel(self):
    return self.level


  def start(self):
    self.level.build()

    self.state = Game.STATE_RUNNING

    self.ev_manager.post(event.LevelStartEvent(self.level))


  def notify(self, ev):
    """Starts the Game if the Game is building on a TickEvent."""
    if isinstance(ev, event.TickEvent):
      if self.state == Game.STATE_BUILDING:
        self.start()


import listener
import event


class CpuSpinnerController(listener.Listener):
  """Keeps the program running until a QuitEvent is generated."""

  def __init__(self, ev_manager):
    listener.Listener.__init__(self, ev_manager)
    
    # self.running is true while the app is running
    self.running = True

    # self.timing is true while the player is in-game
    # it spools 
    self.timing = False


  def run(self):
    # Can space it out here to not check on every single CPU tick
    while self.running:
      self.ev_manager.post(event.TickEvent())

  def notify(self, ev):
    # This quits the game loop on a QuitEvent.
    if isinstance(ev, event.QuitEvent):
      self.running = False

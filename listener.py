class Listener(object):
  """A generic listener class that registers itself with an
  event manager on instantiation and unregisters upon destruction.
  It can be any Model element, a View, or any Controller."""

  def __init__(self, ev_manager):
    self.ev_manager = ev_manager
    self.ev_manager.registerListener(self)

  def __del__(self):
    self.ev_manager.unregisterListener(self)
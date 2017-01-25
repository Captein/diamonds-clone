import event
import log


class EventManager:
  """EventManager serves as a mediator 
  between the Model, View, and Controller."""

  def __init__(self):
    # Listeners include the model elements, view, and controllers
    self.listeners = []
    self.log = log.getLogger(__name__)

    self.indent = '> '

  
  def registerListener(self, listener):
    if listener not in self.listeners:
      self.listeners.append(listener)

  def unregisterListener(self, listener):
    if listener not in self.listeners:
      self.log.error('cannot unregister: listener not found')
    else:
      self.log.debug('')
    
    idx = self.listeners.index(listener)
    self.listeners.remove(idx)


  def post(self, ev):
    """Alerts listeners for events."""
    if isinstance(ev, event.DebugEvent):
      self.log.debug('Listeners:')
      for listener in self.listeners:
        self.log.debug('  {}'.format(type(listener)))



    if not isinstance(ev, event.TickEvent):
      self.log.debug('{}Event: START {}'.format(self.indent, ev.name))
      self.indent += '| '
    
    for listener in self.listeners:
      # NB: when the weakref dies, the key is removed from
      # the dictionary automatically

      listener.notify(ev)

    if not isinstance(ev, event.TickEvent):
      self.log.debug('{}Event: END {}'.format(self.indent, ev.name))
      self.indent = self.indent[:-2]
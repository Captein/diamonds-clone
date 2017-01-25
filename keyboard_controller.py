import listener
import event
import pygame as pg


class KeyboardController(listener.Listener):
  """Sends keyboard events to the EventManager."""

  def notify(self, ev):
    
    if isinstance(ev, event.TickEvent):

      # Handles input events
      for pg_event in pg.event.get():
        new_ev = None
        if pg_event.type == pg.QUIT:
          new_ev = event.QuitEvent()
        elif pg_event.type == pg.KEYDOWN and pg_event.key == pg.K_ESCAPE:
          new_ev = event.QuitEvent()
        elif pg_event.type == pg.KEYDOWN:
          if pg_event.key == pg.K_d:
            new_ev = event.DebugEvent()
        #  if pg_event.key == pg.K_LEFT:
        #    new_ev = event.BallMoveRequest('left')
        #  elif pg_event.key == pg.K_RIGHT:
        #    new_ev = event.BallMoveRequest('right')

        # Add more events here. Check for pressed keys to generate move events?

        if new_ev:
          self.ev_manager.post(new_ev)

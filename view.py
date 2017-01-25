import listener
import event
import ball_sprite as bs
import pygame as pg


class View(listener.Listener):

  def __init__(self, ev_manager, screensize=(640, 480)):
    listener.Listener.__init__(self, ev_manager)

    self.screensize = (self.width, self.height) = screensize

    pg.init()

    self.screen = pg.display.set_mode(self.screensize)
    self.background = pg.Surface(self.screen.get_size())
    self.background.convert()
    self.drawBackground()

    # This is a rendering group for just the ball.
    self.ball_group = pg.sprite.RenderUpdates()

    # This rendering group contains the blocks.
    self.block_group = pg.sprite.RenderUpdates()



  def drawBackground(self):
    """Blits the background to the screen."""
    self.background.fill((22,22,22))
    self.screen.blit(self.background, (0,0))
    pg.display.flip()


  def drawLevel(self, level):
    """Blits the level sprites to the screen."""

    self.drawBackground()

    # Create sprites for each block in level 
    # and add them to self.block_group.



  def showBlocks(self, level):
    """Blits the blocks to the screen."""

    # The list of blocks should show up in a 2D array in the Level object.
    # This should iterate across them and blit them to the screen.
    pass


  def moveBallSprite(self, ball):
    """Sets the attrs of the BallSprite to the attrs of the ball arg.
    Creates a new BallSprite if there is none."""

    ball_sprite = self.getBallSprite()

    # If there is no BallSprite in self.ball_group, make one!
    if ball_sprite is None:
      ball_sprite = bs.BallSprite(ball, self.ball_group)

    # Otherwise, queue new attributes
    else:
      ball_sprite.setNewRadius(ball.getRadius())
      ball_sprite.setNewColor(ball.getColor())
      ball_sprite.setNewLocation(ball.getLocation())


  def getBallSprite(self):
    """Returns the BallSprite from self.ball_group if it's present."""
    for sprite in self.ball_group:
      return sprite
    return None



  def notify(self, ev):
    if isinstance(ev, event.TickEvent):
      # Draw all of the sprites on each tick
      self.ball_group.clear(self.screen, self.background)
      self.ball_group.update()
      dirty_ball_rect = self.ball_group.draw(self.screen)
      pg.display.update(dirty_ball_rect)
      

    elif isinstance(ev, event.LevelBuiltEvent):
      # Draws the background and blocks of the level.
      self.drawLevel(ev.level)

      # The BallSprite is placed when the level is started, not built.
      # It is drawn and blitted every tick event.
      

    elif isinstance(ev, event.BallMoveEvent):
      # Clears and redraws the Ball
      self.moveBallSprite(ev.ball)
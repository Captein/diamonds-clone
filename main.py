#!/usr/bin/env python

import event_manager as em
import keyboard_controller as keyctrl
import cpu_spinner_controller as cpuctrl
import view
import game


def main():
  """..."""

  ev_manager = em.EventManager()

  keyboard = keyctrl.KeyboardController(ev_manager)
  spinner = cpuctrl.CpuSpinnerController(ev_manager)
  pygame_view = view.View(ev_manager)
  diamonds_game = game.Game(ev_manager, fps=60)

  spinner.run()


if __name__ == '__main__':
  main()

#!/usr/bin/env python
# python_example.py
# Author: Ben Goodrich
#
# This is a direct port to python of the shared library example from
# ALE provided in doc/examples/sharedLibraryInterfaceExample.cpp
import sys
sys.path.insert(0, '/home/jmastr2/ECSE526-Artificial-Intelligence/A3/ale_0_5/ale_python_interface')
from random import randrange
from ale_python_interface import ALEInterface


# Inputs: 'rom_file'
if len(sys.argv) < 2:
  print('Usage:', sys.argv[0], 'rom_file')
  sys.exit()

ale = ALEInterface()

# Get & Set the desired settings
ale.setInt('random_seed', 123)
ale.setInt('frame_skip', 5)
ale.setFloat('repeat_action_probability', 0.25)


# Set USE_SDL to true to display the screen. ALE must be compilied
# with SDL enabled for this to work. On OSX, pygame init is used to
# proxy-call SDL_main.
USE_SDL = sys.argv[2];
if USE_SDL:
  ale.setBool('display_screen', True)
  if sys.platform == 'darwin':
    import pygame
    pygame.init()
    ale.setBool('sound', False) # Sound doesn't work on OSX
  elif sys.platform.startswith('linux'):
    ale.setBool('sound', True)
  

# Load the ROM file
ale.loadROM(sys.argv[1])

# Get the list of legal actions
legal_actions = ale.getLegalActionSet()
print(legal_actions)

# Play 10 episodes
for episode in xrange(1):
  total_reward = 0
  while not ale.game_over():
    a = legal_actions[randrange(len(legal_actions))]
    # Apply an action and get the resulting reward
    reward = ale.act(a);
    total_reward += reward
  print('Episode', episode, 'ended with score:', total_reward)
  ale.reset_game()

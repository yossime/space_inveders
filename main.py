#!/usr/bin/env python3
"""
Space Invaders Game
Main entry point for the game
"""

import sys
import os

# Add the game directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'game'))

# Import and run the game
from game.run_game import main

if __name__ == "__main__":
    main()
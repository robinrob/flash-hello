#!/usr/bin/python3

import sys
import argparse

import life_settings as settings
from life_config import LifeConfig
from life_grid import LifeGrid
from life_algo import LifeAlgo
from life_game import LifeGame

parser = argparse.ArgumentParser(description='Play a game of Life.')

parser.add_argument('width', metavar='width', type=int,
                    help='width of world')

parser.add_argument('height', metavar='height', type=int,
                    help='height of world')

parser.add_argument('turns', metavar='turns', type=int,
                    help='number of turns')

parser.add_argument('delay', metavar='delay', type=float,
                    help='delay between turns')

args = parser.parse_args();

grid = LifeGrid(args.width, args.height)

game = LifeGame(grid, LifeAlgo)

#config = Arrangement(args.width, args.height).center(settings.CONFIG)
config = LifeConfig(args.width, args.height).grid(15)

game.configure(config)

game.play(args.turns, args.delay)
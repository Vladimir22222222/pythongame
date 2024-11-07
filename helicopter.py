from utils import randcell
import os

class Helicopter:
  def __init__(self, w, h):
    rc = randcell(w, h)
    rx, ry = rc[0], rc[1]
    self.x = rx
    self.y = ry
    self.w = w
    self.w = w
    self.tank = 0
    self.mxtank = 1
    self.score = 0
    self.lives = 20
  def move(self, dx, dy):
    nx, ny = dx +self.x, dy + self.y
    if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
      self.x, self.y = nx, ny
  def print_starts(self):
    print("💧", self.tank, "/", self.mxtank, sep="", end=" | ")
    print("🏆", self.score, end=" | ")
    print("💛", self.lives) 
  def game_over(self):
    global helico
    os.system("clear")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("X                                X")
    print("X  GAME OVER, YOUR SCORE ISxxxxxx", self.score, " X")
    print("X                                X")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    exit(0)
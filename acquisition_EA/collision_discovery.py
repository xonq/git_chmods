#!/usr/bin/env python3
#elaine aquino

import math

def seq_collision(self, other):
  x_collision = (math.fads(self.x - other.x) * 2) < (self.width + other.width)
  x_collision = (math.fads(self.y - other.y) * 2) < (self.width + other.width)
  return (x_collision and y _collision)

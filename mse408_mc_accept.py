#! /usr/bin/python

import numpy as np
from random import randint
import random
import math

def rand_coors(argu):
    x_rand = randint(0,9)
    y_rand = randint(0,9)
#   print("X coord: {x},Y coord: {y}".format(x=x_rand,y=y_rand))
    return x_rand,y_rand

def accept_check(tmp_energy,current_energy,temp):
#   print(current_energy - tmp_energy)
    rand_num = random.random()
    bltz_factor=math.exp(-(tmp_energy-current_energy)/temp)
    if rand_num < bltz_factor:
       return True
    else:
       return False
     

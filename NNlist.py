import numpy as np
import os, sys, subprocess, re

def NNlist(Array):
    Nrows = len(Array)
    Ncol = len(Array[1])
    for i in range(0, Nrows):
        for j in range(0, Ncol):
            if i == 0:
                Up = len(Array)-1
                Down = 1
            elif i == len(Array)-1:
                Down = 0
                Up = len(Array)-2
            else:
                Down = i+1
                Up = i-1
            if j == 0:
                Right = 1
                Left = len(Array[1])-1
            elif j == len(Array[1])-1:
                Right = 0
                Left = len(Array[1])-2
            else:
                Right = j+1
                Left = j-1
            Array[i][j].append([[Up,j],[i,Right],[Down,j],[i,Left]])
            Array[i][j].append([[Up,Right],[Down,Right],[Down,Left],[Up,Left]])
return Array
#!/usr/bin/python

#Author: Nick Wagner
#Date: 22 February 2015
#Purpose: User Input for 2d Ising Model
#Edited by Cyrus Ramavarapu 28 February 2015

#Notes:	  File has to be structured in the read order
import sys

class Arguments:
    def __init__(self):
            """setup simulation parameters"""
            self.nequil             = -1
            self.nsample            = -1
            self.start_temp         = -1
            self.end_temp           = -1
            self.delta_temp         = -1 
            self.start_chempot      = -1
            self.end_chempot        = -1
            self.delta_chempot      = -1

    def init_check(self):
        if self.nequil == -1:
            prfloat("Equilibrium steps not set")
            exit() 
        if self.nsample == -1:
            prfloat("Sample steps not set")
            exit() 
        if self.start_temp == -1:
            prfloat("Start temp not set")
            exit() 
        if self.end_temp == -1:
            prfloat("Final temp not set")
            exit()
        if self.delta_temp == -1:
            prfloat("Delta T not set")
            exit()
        if self.start_chempot == -1:
            prfloat("Start chemical potential not set")
            exit()
        if self.end_chempot == -1:
            prfloat("End chemical potential not set")
            exit()
        if self.delta_chempot == -1:
            prfloat("delta chemical potential not set")
            exit()

def get_input(argu):
    file_name           = sys.argv[1]
    inf                 = open(file_name,'r')
    argu.nequil         = int(inf.readline())
    argu.nsample        = int(inf.readline())
    argu.start_temp 	= float(inf.readline())
    argu.end_temp	= float(inf.readline())
    argu.delta_temp 	= float(inf.readline())
    argu.start_chempot	= float(inf.readline())
    argu.end_chempot	= float(inf.readline())
    argu.delta_chempot  = float(inf.readline())
    inf.close()

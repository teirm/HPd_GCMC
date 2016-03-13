#!/usr/bin/python

#Author: Johnathan Pfluger
#Date:   22 February 2015
#Purpose: Implement PBC, Tabulate Energies, and Caculate Hamiltonian 
#Edited by Cyrus Ramavarapu 28 February 2015
#Edited by Cyrus Ramavarapu 1 March 2015
#Edited by Cyrus Ramavarapu 2 March 2015 - Simplified Hamiltonian Calculation

import math

#Energy Table
EnergyTable = []

V1= -1
V2 = 0
for i in range(0,2):
    EnergyTable.append([])
    for j in range(0,5):
        EnergyTable[i].append(math.pow(-1,i)*(j-2))
#    for j in range(0,5):
#        EnergyTable[i].append([])
#        for k in range(0,2):
#            EnergyTable[i][j].append(0.5*V1*((2*k)-1)*(2*i-4)+0.5*V2*((2*k)-1)*(2*j-4))

def init_lattice(argu):
    rows = 10 
    columns = rows
    lattice = []
    for i in range(rows):
            lattice.append([])
            for j in range(columns):
                    lattice[i].append([1])
    
    lattice = init_pbc(lattice) 
    
    return lattice

def init_pbc(Array):
    Nrows = len(Array)
    Ncol = len(Array[1])

#Calculate the NN and NNN indices and modify the lattice array
#so that each element is of the form [spin, array of NN indices 
#in a top/right/bottom/left pattern, array of NNN indices in a top-right clockwise manner
#i scans the rows and j scans the columns
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

def spin_sums(Array,i,j):
    
    Spin = Array[i][j][0]
    Spin1 = Array[Array[i][j][1][0][0]][Array[i][j][1][0][1]][0]
    Spin2 = Array[Array[i][j][1][1][0]][Array[i][j][1][1][1]][0]
    Spin3 = Array[Array[i][j][1][2][0]][Array[i][j][1][2][1]][0]
    Spin4 = Array[Array[i][j][1][3][0]][Array[i][j][1][3][1]][0]
    NNspin = Spin1+Spin2+Spin3+Spin4
    Spin5 = Array[Array[i][j][2][0][0]][Array[i][j][2][0][1]][0]
    Spin6 = Array[Array[i][j][2][1][0]][Array[i][j][2][1][1]][0]
    Spin7 = Array[Array[i][j][2][2][0]][Array[i][j][2][2][1]][0]
    Spin8 = Array[Array[i][j][2][3][0]][Array[i][j][2][3][1]][0] 
    NNNspin = Spin5+Spin6+Spin7+Spin8

    return Spin,NNspin,NNNspin

def get_energy(Array,mu):
#   Energy = EnergyTable[NNspin][NNNspin][Spin]
#   print(EnergyTable) 
#   print(Spin)
#   print(NNspin)

    Energy = 0
    
    for i in range(len(Array)):
        for j in range(len(Array)):
            Spin,NNspin,NNNspin = spin_sums(Array,i,j)
            Energy += EnergyTable[Spin][NNspin]    
    
#    print(Energy) 
    field = field_calc(Array,mu)

    Energy -= field
    return Energy

##############BUG#######################
#0 in field sum is wrong should have -1#
#Corrected 28 February 2015            #
########################################
def field_calc(Array,mu):
    Sum = 0
    for i in range(len(Array)):
        for j in range(len(Array[1])):
            if Array[i][j][0] == 1:
                Sum += 1
            else:
                Sum -= 1
    
    Field = mu*Sum
#    print(Field)
    return Field

def get_coverage(Array,argu):
    size = 10 
    total = 0
    for i in range(0,size):
        for j in range(0,size):
            if Array[i][j][0] == 1:
                total += 1
            else:
                total -= 1

    return total/(size*size)

def flip_spin(lattice,x,y):
    if  lattice[x][y][0] == 0:
        return 1 
    else:
        return 0 

def get_site_energy(lattice,x,y):
   
    spin,nnspin,nnnspin = spin_sums(lattice,x,y)

    return EnergyTable[spin][nnspin]

def update_energy(current_energy,new_site_energy,old_site_energy):
    
    energy = current_energy - old_site_energy + 3*new_site_energy     

    return energy

#Initialize the array of spins
rows = 70
columns = rows
lattice = []
for i in range(rows):
	lattice.append([])
	for j in range(columns):
		lattice[i].append(1)

#Array = [[[1],[0],[1],[0]],[[0],[1],[0],[1]],[[1],[0],[1],[0]],[[0],[1],[0],[1]]]

#Calculate the size of the spin array
Nrows = len(lattice)
Ncol = len(lattice[1])

#Calculate the NN and NNN indices and modify the lattice array
#so that each element is of the form [spin, array of NN indices 
#in a top/right/bottom/left pattern, array of NNN indices in a top-right clockwise manner
#i scans the rows and j scans the columns
for i in range(0, Nrows):
    for j in range(0, Ncol):
        if i == 0:
            Up = len(lattice)-1
            Down = 1
        elif i == len(lattice)-1:
            Down = 0
            Up = len(lattice)-2
        else:
            Down = i+1
            Up = i-1
        if j == 0:
            Right = 1
            Left = len(lattice[1])-1
        elif j == len(lattice[1])-1:
            Right = 0
            Left = len(lattice[1])-2
        else:
            Right = j+1
            Left = j-1
        lattice[i][j].append([[Up,j],[i,Right],[Down,j],[i,Left]])
        lattice[i][j].append([[Up,Right],[Down,Right],[Down,Left],[Up,Left]])
        
#Given a lattice index position, we will calculate the sum of NN and NNN spins
#i and j are the indices for the spin to be flipped
#Spin is the new value of the spin flip
i = 0
j = 0
Spin = lattice[i][j][0]
Spin1 = lattice[lattice[i][j][1][0][0]][lattice[i][j][1][0][1]][0]
Spin2 = lattice[lattice[i][j][1][1][0]][lattice[i][j][1][1][1]][0]
Spin3 = lattice[lattice[i][j][1][2][0]][lattice[i][j][1][2][1]][0]
Spin4 = lattice[lattice[i][j][1][3][0]][lattice[i][j][1][3][1]][0]
NNspin = Spin1+Spin2+Spin3+Spin4
Spin5 = lattice[lattice[i][j][2][0][0]][lattice[i][j][2][0][1]][0]
Spin6 = lattice[lattice[i][j][2][1][0]][lattice[i][j][2][1][1]][0]
Spin7 = lattice[lattice[i][j][2][2][0]][lattice[i][j][2][2][1]][0]
Spin8 = lattice[lattice[i][j][2][3][0]][lattice[i][j][2][3][1]][0] 
NNNspin = Spin5+Spin6+Spin7+Spin8

#This is the tabulation of all of the energy possibilities for the NN/NNN terms
#in the format (value of NN spin sum, value of NNN spin sum, value of flipped spin)
EnergyTable = []
for i in range(0,5):
    EnergyTable.append([])
    for j in range(0,5):
        EnergyTable[i].append([])
        for k in range(0,2):
            EnergyTable[i][j].append(0.5*V1*((2*k)-1)*(2*i-4)+0.5*V2*((2*k)-1)*(2*j-4))
#This references the table and extracts the proper value of the NN/NNN terms
Energy = EnergyTable[NNspin][NNNspin][Spin]

#Calculation of the field term
Sum = 0
for i in range(len(lattice)):
    for j in range(len(lattice[1])):
        Sum = Sum + lattice[i][j][0]
Field = mu*Sum

#Calculation of the total Energy term (defined as NN+NNN-Field)
TotalEnergy = Energy-Field

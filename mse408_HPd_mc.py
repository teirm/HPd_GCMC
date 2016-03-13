#!/usr/bin/python

#Author: Cyrus Ramavarapu 
#Date:   28 February 2015
#Purpose: Organize Code, Implement MMC algorithm, Debug 
#Edited by Cyrus Ramavarapu 1 March 2015
#Edited by Cyrus Ramavarapu 2 March 2015 - Can reproduce Onsager's result

import numpy as np
from mse408_mc_userIO import *
from mse408_mc_accept import *
from mse408_mc_lattice import *

argu = Arguments()
get_input(argu)
argu.init_check()

temperatures    = list(np.arange(argu.start_temp,argu.end_temp,argu.delta_temp))
chemical_pots   = list(np.arange(argu.start_chempot,argu.end_chempot,argu.delta_chempot)) 

lattice = init_lattice(argu)

#print(EnergyTable)

for mu in chemical_pots:
    current_energy = get_energy(lattice,mu)
    for temp in temperatures:
        file_name = """test_HPd_GCMC_temp{temp}_mu{mu}""".format(temp = temp, mu = mu)
        f_data = open(file_name,"w")
        f_data.write("""#T\t\tmu\t\tenergy\t\tenergy^2\t\tcoverage\n""")
        for i in range(0,argu.nequil):
#            print(current_energy) 
#            print(EnergyTable) 
            x,y = rand_coors(argu)
            old_site_energy = get_site_energy(lattice,x,y) 
            lattice[x][y][0] = flip_spin(lattice,x,y) 
            new_site_energy = get_site_energy(lattice,x,y) 
            tmp_energy = update_energy(current_energy,new_site_energy,old_site_energy)
#            print(tmp_energy) 
#            input("press Enter to step forward")
            if tmp_energy <= current_energy:
                current_energy = tmp_energy
            else:
                if accept_check(tmp_energy,current_energy,temp):
                    current_energy = tmp_energy
                else:
                    lattice[x][y][0] = flip_spin(lattice,x,y)

#            print(get_coverage(lattice,argu))

        print("""Now sampling T:{temp} with mu:{mu}""".format(temp=temp,mu=mu))

        for i in range(0,argu.nsample):
            x,y = rand_coors(argu)
            old_site_energy = get_site_energy(lattice,x,y) 
            lattice[x][y][0] = flip_spin(lattice,x,y) 
            new_site_energy = get_site_energy(lattice,x,y) 
            tmp_energy = update_energy(current_energy,new_site_energy,old_site_energy)        
#            tmp_energy = update_energy(current_energy,mu,lattice,x,y)
            if tmp_energy <= current_energy:
                current_energy = tmp_energy
            else:
                if accept_check(tmp_energy,current_energy,temp):
                    current_energy = tmp_energy
                else:
                    lattice[x][y][0] = flip_spin(lattice,x,y)
            
            coverage = get_coverage(lattice,argu)

            if i%500 == 0:
               f_data.write("""{temp}\t\t{mu}\t\t{E}\t\t{EE}\t\t{coverage}\n""".format(temp=temp,\
                        mu=mu,E=current_energy,EE=current_energy*current_energy,\
                        coverage=coverage))

        f_data.close()
        lattice = init_lattice(argu)
        print("""Sample at T:{temp} with mu:{mu} COMPLETE""".format(temp=temp,mu=mu))

# -*- coding: utf-8 -*-
"""
ABM for "Is the cultural evolution of technology combinatorial or cumulative?".

@author: James Winters
"""

import editdistance
from problemspace import *
from procedures import *
from ag_init import *

def simulation(run=0,n=100,generations=2000,TS=10,modify=True,combine=True,loss=0.5):
	prob,agents,positions,memory = init(n=n,difficulty=2)
	for gen in range(0,generations):
		for ts in range(0,TS):
			random.shuffle(agents)
			if gen > 0 and ts == 0:
				#Inheritance process
				for agent in agents:
					lost = np.random.choice([True,False],1,p=[loss,1-loss])
					if lost == True:
						sol_len = random.choice([2,3,4])
						sol_space = generate_binary(sol_len)
						sol_choice = [random.choice(sol_space),random.choice(sol_space),random.choice(sol_space),random.choice(sol_space)]
						memory.update({agent:sol_choice})
			for agent in agents:
				problem = positions[agent]
				current = sorted(memory[agent],key=lambda x: editdistance.eval(x,problem))[0]
				#Combination and Modification
				if combine == True and modify == True:
					ag_loc = local(sol=current,prob=problem)
					ag_com = combination(agent=agent,memory=memory,problem=problem)
					sol_pool = [current,ag_loc,ag_com]
					ag_sols = sorted(sol_pool, key=lambda x: editdistance.eval(x,problem))
				#Modification
				elif combine == False and modify == True:
					ag_loc = local(sol=current,prob=problem)
					sol_pool = [current,ag_loc]
					ag_sols = sorted(sol_pool, key=lambda x: editdistance.eval(x,problem))
				#Combination
				elif combine == True and modify == False:
					ag_com = combination(agent=agent,memory=memory,problem=problem)
					sol_pool = [current,ag_com]
					ag_sols = sorted(sol_pool, key=lambda x: editdistance.eval(x,problem))
				#Inheritance only
				else:
					sol_pool = [current]
					ag_sols = sorted(sol_pool, key=lambda x: editdistance.eval(x,problem))

				if ag_sols[0] not in memory[agent]:
					sol_list = sorted(memory[agent],key=lambda x: editdistance.eval(x,problem))
					del sol_list[-1]
					sol_list.append(ag_sols[0])	
					memory.update({agent:sol_list})
				
				#Exploration
				if ts == 9:
					ag_current = sorted(memory[agent],key=lambda x: editdistance.eval(x,problem))[0]
					loc = positions[agent]
					while len(ag_current) >= len(loc):
						new_loc = movement(prob=prob,loc=loc,pr=[1/3,1/3,1/3])
						positions.update({agent:new_loc})
						if new_loc not in prob:
							prob.update({new_loc:['*','+','-']})
						loc = positions[agent]

			prob_list = [len(positions[ag]) for ag in agents]
			complexity_ave = sum(prob_list) / len(prob_list)
			complex_min = min(prob_list)
			complex_max = max(prob_list)

			print('Run: {}, Loss: {}, Gen: {}, TS: {}, Problem Complexity: {}'.format(run,loss,gen,ts,complex_max))

			#Writing to file
			import os
			dir_path = os.path.dirname(os.path.realpath(__file__))
			if combine == True and modify == True:
				soc = 'combo_local'
			elif combine == False and modify == True:
				soc = 'local'
			elif combine == True and modify == False:
				soc = 'combo'
			else:
				soc = 'inherit'
			with open(dir_path+'\\output\\{}_loss{}_gens{}.csv'.format(soc,loss,generations),'a') as output:
				output.write(str(run)+';'+str(gen)+';'+str(ts)+';'+str(loss)+';'+str(modify)+';'+str(combine)+';'+str(complex_max)+'\n')

# run=0
# n=25
# generations=2000
# TS=10
# modify=True
# combine=True
# loss=0.9

# for r in range(1,10):
# 	simulation(run=r,n=n,generations=generations,TS=TS,modify=modify,combine=combine,loss=loss)

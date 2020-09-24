import random
import numpy as np
import editdistance
from itertools import permutations

def modification(sol):
	st_locs = [i for i in range(len(sol))]
	val_loc = random.choice(st_locs)
	value = sol[val_loc]
	if value == '0':
		new_sol = sol[:val_loc] + '1' + sol[val_loc+1:]
	elif value == '1':
		new_sol = sol[:val_loc] + '0' + sol[val_loc+1:]
	return new_sol

def insertion(sol):
	st_locs = [i for i in range(len(sol)+1)]
	val_loc = random.choice(st_locs)
	try:
		value = sol[val_loc]
		if value == '0':
			new_sol = sol[:val_loc] + '1' + sol[val_loc:]
		elif value == '1':
			new_sol = sol[:val_loc] + '0' + sol[val_loc:]
	except IndexError:
		place = random.choice([0,1])
		if place == 0:
			new_sol = random.choice(['0','1']) + sol
		elif place == 1:
			new_sol = sol + random.choice(['0','1'])
	return new_sol

def deletion(sol):
	if len(sol) > 2:
		st_locs = [i for i in range(len(sol))]
		val_loc = random.choice(st_locs)
		value = sol[val_loc]
		new_sol = sol[:val_loc] + sol[val_loc+1:]
	else:
		new_sol = sol
	return new_sol

def local(sol,prob):
	ag_mod = modification(sol=sol)
	ag_ins = insertion(sol=sol)
	ag_del = deletion(sol=sol)
	sol_pool = [ag_mod,ag_ins,ag_del]
	ag_sols = sorted(sol_pool, key=lambda x: editdistance.eval(x,prob))[0]
	return ag_sols

def combination(agent,memory,problem):
	permute_space = list(permutations(memory[agent],2))
	combo_space = sorted([''.join(i) for i in permute_space],key=lambda x: editdistance.eval(x,problem))
	new_sol = combo_space[0]
	return new_sol
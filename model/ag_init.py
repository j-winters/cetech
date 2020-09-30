import random
from problemspace import generate_binary,local_space

def agent_generator(agents,memory):
	for ag in agents:
		sol_len = random.choice([2,3,4])
		sol_space = generate_binary(sol_len)
		solution = [random.choice(sol_space),random.choice(sol_space),random.choice(sol_space),random.choice(sol_space)]
		memory.update({ag:solution})
	return memory

def init(n,difficulty=2):
	prob = {'00':['*','+'],'01':['*','+'],'10':['*','+'],'11':['*','+']}
	agents = [i for i in range(n)]
	p_initial = generate_binary(difficulty)
	positions = local_space(p_initial,agents)
	memory = agent_generator(agents,dict())
	return prob,agents,positions,memory



# Running the genetic algorithm
for i in range(iterations):
	nextPop = []
	# Each one of this iteration will generate two descendants individuals. Therefore, to guarantee same population size, this will iterate half population size times
	for j in range(int(len(pop) / 2)):
		# Selecting randomly 4 individuals to select 2 parents by a binary tournament
		parentIds = set()
		while len(parentIds) < 4:
			parentIds |= {random.randint(0, len(pop) - 1)}
		parentIds = list(parentIds)
		# Selecting 2 parents with the binary tournament
		parent1 = pop[parentIds[0]] if fitness(pop[parentIds[0]]) < fitness(pop[parentIds[1]]) else pop[parentIds[1]]
		parent2 = pop[parentIds[2]] if fitness(pop[parentIds[2]]) < fitness(pop[parentIds[3]]) else pop[parentIds[3]]
		# Selecting two random cutting points for crossover, with the same points (indexes) for both parents, based on the shortest parent
		cutIdx1, cutIdx2 = random.randint(1, min(len(parent1), len(parent2)) - 1), random.randint(1, min(len(parent1), len(parent2)) - 1)
		cutIdx1, cutIdx2 = min(cutIdx1, cutIdx2), max(cutIdx1, cutIdx2)
		# Doing crossover and generating two children
		child1 = parent1[:cutIdx1] + parent2[cutIdx1:cutIdx2] + parent1[cutIdx2:]
		child2 = parent2[:cutIdx1] + parent1[cutIdx1:cutIdx2] + parent2[cutIdx2:]
		nextPop += [child1, child2]
	# Doing mutation: swapping two positions in one of the individuals, with 1:15 probability
	if random.randint(1, 15) == 1:
		ptomutate = nextPop[random.randint(0, len(nextPop) - 1)]
		i1 = random.randint(0, len(ptomutate) - 1)
		i2 = random.randint(0, len(ptomutate) - 1)
		ptomutate[i1], ptomutate[i2] = ptomutate[i2], ptomutate[i1]
	# Adjusting individuals
	for p in nextPop:
		adjust(p)
	# Updating population generation
	pop = nextPop

# Selecting the best individual, which is the final solution
better = None
bf = float('inf')
for p in pop:
	f = fitness(p)
	if f < bf:
		bf = f
		better = p


## After processing the algorithm, now outputting it ##


# Printing the solution
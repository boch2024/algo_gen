import random

UNITS = [
    {"id": 1, "capacity": 20, "valid_codes": ["1100", "0110", "0011"]},
    {"id": 2, "capacity": 15, "valid_codes": ["1100", "0110", "0011"]},
    {"id": 3, "capacity": 35, "valid_codes": ["1000", "0100", "0010", "0001"]},
    {"id": 4, "capacity": 40, "valid_codes": ["1000", "0100", "0010", "0001"]},
    {"id": 5, "capacity": 15, "valid_codes": ["1000", "0100", "0010", "0001"]},
    {"id": 6, "capacity": 15, "valid_codes": ["1000", "0100", "0010", "0001"]},
    {"id": 7, "capacity": 10, "valid_codes": ["1000", "0100", "0010", "0001"]}
]

DEMANDS = [80, 90, 65, 70]
TOTAL_CAPACITY = 150


def generate_individual():
    return [random.choice(unit["valid_codes"]) for unit in UNITS]


def evaluate(chromosome):
    reserves = []
    for t in range(4):
        p_perdue = 0
        for i, block in enumerate(chromosome):
            if block[t] == '1':
                p_perdue += UNITS[i]["capacity"]
        reserve = TOTAL_CAPACITY - p_perdue - DEMANDS[t]
        reserves.append(reserve)

    min_reserve = min(reserves)
    return max(0.0, float(min_reserve))


def selection_roulette(population, fitnesses):
    total_fit = sum(fitnesses)
    if total_fit == 0:
        return random.choice(population)

    pick = random.uniform(0, total_fit)
    current = 0
    for ind, fit in zip(population, fitnesses):
        current += fit
        if current >= pick:
            return ind
    return population[-1]


def crossover(parent1, parent2):
    if random.random() < 0.8:
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1.copy(), parent2.copy()


def mutation_inversion(chromosome, mutation_rate=0.15):
    mutated = list(chromosome)
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            inverted_block = mutated[i][::-1]
            if inverted_block in UNITS[i]["valid_codes"]:
                mutated[i] = inverted_block
            else:
                mutated[i] = random.choice(UNITS[i]["valid_codes"])
    return mutated


def genetic_algorithm(pop_size=50, generations=100):
    population = [generate_individual() for _ in range(pop_size)]

    best_solution = None
    best_fitness = -1.0

    for gen in range(generations):
        fitnesses = [evaluate(ind) for ind in population]

        max_fit = max(fitnesses)
        if max_fit > best_fitness:
            best_fitness = max_fit
            best_solution = population[fitnesses.index(max_fit)]

        new_population = []
        while len(new_population) < pop_size:
            p1 = selection_roulette(population, fitnesses)
            p2 = selection_roulette(population, fitnesses)

            c1, c2 = crossover(p1, p2)
            c1 = mutation_inversion(c1)
            c2 = mutation_inversion(c2)

            new_population.extend([c1, c2])

        population = new_population[:pop_size]

    return best_solution, best_fitness


if __name__ == "__main__":
    best_ind, best_fit = genetic_algorithm()
    print("Meilleur planning trouvé (par unité de 1 à 7) :", best_ind)
    print("Réserve minimale garantie (Fitness) :", best_fit, "MW")

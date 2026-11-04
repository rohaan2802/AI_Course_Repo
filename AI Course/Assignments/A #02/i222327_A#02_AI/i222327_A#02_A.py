import random

# Products data
products = [
    {"name": "P1 - Glass Bottles", "weight": 20, "category": "Beverage", "fragile": True, "hazardous": False, "temp": False, "demand": "Medium"},
    {"name": "P2 - Frozen Meat", "weight": 30, "category": "Food", "fragile": False, "hazardous": False, "temp": True, "demand": "High"},
    {"name": "P3 - Cleaning Acid", "weight": 10, "category": "Chemical", "fragile": False, "hazardous": True, "temp": False, "demand": "Low"},
    {"name": "P4 - Rice Bags", "weight": 50, "category": "Grocery", "fragile": False, "hazardous": False, "temp": False, "demand": "High"},
    {"name": "P5 - Ceramic Plates", "weight": 15, "category": "Kitchenware", "fragile": True, "hazardous": False, "temp": False, "demand": "Medium"},
    {"name": "P6 - Ice Cream", "weight": 25, "category": "Food", "fragile": False, "hazardous": False, "temp": True, "demand": "High"},
    {"name": "P7 - Detergent", "weight": 12, "category": "Chemical", "fragile": False, "hazardous": True, "temp": False, "demand": "Medium"},
    {"name": "P8 - Chips Carton", "weight": 8, "category": "Snacks", "fragile": False, "hazardous": False, "temp": False, "demand": "High"},
    {"name": "P9 - Olive Oil Bottles", "weight": 18, "category": "Grocery", "fragile": True, "hazardous": False, "temp": False, "demand": "Medium"},
    {"name": "P10 - Industrial Bleach", "weight": 22, "category": "Chemical", "fragile": False, "hazardous": True, "temp": False, "demand": "Low"},
    {"name": "P11 - Yogurt Cartons", "weight": 14, "category": "Food", "fragile": False, "hazardous": False, "temp": True, "demand": "High"},
    {"name": "P12 - Flour Bags", "weight": 45, "category": "Grocery", "fragile": False, "hazardous": False, "temp": False, "demand": "High"},
    {"name": "P13 - Wine Bottles", "weight": 16, "category": "Beverage", "fragile": True, "hazardous": False, "temp": False, "demand": "Medium"},
    {"name": "P14 - Paint Cans", "weight": 28, "category": "Chemical", "fragile": False, "hazardous": True, "temp": False, "demand": "Low"},
    {"name": "P15 - Biscuit Boxes", "weight": 6, "category": "Snacks", "fragile": False, "hazardous": False, "temp": False, "demand": "High"},
    {"name": "P16 - Motor Oil", "weight": 35, "category": "Chemical", "fragile": False, "hazardous": True, "temp": False, "demand": "Low"},
    {"name": "P17 - Frozen Fish", "weight": 20, "category": "Food", "fragile": False, "hazardous": False, "temp": True, "demand": "High"},
    {"name": "P18 - Bubble Wrap Rolls", "weight": 10, "category": "Packaging", "fragile": True, "hazardous": False, "temp": False, "demand": "Medium"},
    {"name": "P19 - Wheat Sacks", "weight": 40, "category": "Grocery", "fragile": False, "hazardous": False, "temp": False, "demand": "High"},
    {"name": "P20 - Hand Sanitizer", "weight": 8, "category": "Chemical", "fragile": True, "hazardous": False, "temp": False, "demand": "Medium"}
]

# Zone capacities
zones = {
    1: 120,  # Z1
    2: 80,   # Z2
    3: 80,   # Z3
    4: 80,   # Z4
    5: 80,   # Z5
    6: 60,   # Z6
    7: 150,  # Z7
    8: 100   # Z8
}

fragile_products = {
    "P1 - Glass Bottles",
    "P5 - Ceramic Plates",
    "P9 - Olive Oil Bottles",
    "P13 - Wine Bottles",
    "P18 - Bubble Wrap Rolls",
    "P20 - Hand Sanitizer"
}

hazardous_products = {
    "P3 - Cleaning Acid",
    "P7 - Detergent",
    "P10 - Industrial Bleach",
    "P14 - Paint Cans",
    "P16 - Motor Oil"
}

temp_products = {
    "P2 - Frozen Meat",
    "P6 - Ice Cream",
    "P11 - Yogurt Cartons",
    "P17 - Frozen Fish"
}

high_demand_products = {
    "P2 - Frozen Meat",
    "P4 - Rice Bags",
    "P8 - Chips Carton",
    "P11 - Yogurt Cartons",
    "P12 - Flour Bags",
    "P15 - Biscuit Boxes",
    "P17 - Frozen Fish",
    "P19 - Wheat Sacks"
}

heavy_products = {
    "P4 - Rice Bags",
    "P12 - Flour Bags"
}

food_products = {
    "P2 - Frozen Meat",
    "P6 - Ice Cream",
    "P11 - Yogurt Cartons",
    "P17 - Frozen Fish"
}

chemical_products = {
    "P3 - Cleaning Acid",
    "P7 - Detergent",
    "P10 - Industrial Bleach",
    "P14 - Paint Cans",
    "P16 - Motor Oil",
    "P20 - Hand Sanitizer"
}

eligible_z8_products = {
    "P2 - Frozen Meat",
    "P11 - Yogurt Cartons",
    "P17 - Frozen Fish"
}


def fitness(chromosome):
    total_penalty = 0
    violations = []

    # -----------------------------
    # 1. Zone weight capacity check
    # -----------------------------
    zone_weights = {zone: 0 for zone in zones}

    for i in range(len(chromosome)):
        zone = chromosome[i]
        weight = products[i]["weight"]
        zone_weights[zone] += weight

    for zone in zone_weights:
        if zone_weights[zone] > zones[zone]:
            excess = zone_weights[zone] - zones[zone]
            penalty = excess * 2
            total_penalty += penalty
            violations.append(f"Z{zone} exceeds capacity by {excess} kg -> +{penalty}")

    # ----------------------------------
    # 2. Product-based individual checks
    # ----------------------------------
    for i in range(len(chromosome)):
        product = products[i]
        name = product["name"]
        zone = chromosome[i]

        # Fragile must be in Z3
        if name in fragile_products and zone != 3:
            total_penalty += 8
            violations.append(f"{name} is fragile but not in Z3 -> +8")

        # Hazardous must be in Z5
        if name in hazardous_products and zone != 5:
            total_penalty += 10
            violations.append(f"{name} is hazardous but not in Z5 -> +10")

        # Temperature controlled must be in Z4 or Z8
        if name in temp_products and zone not in [4, 8]:
            total_penalty += 9
            violations.append(f"{name} needs temperature control but not in Z4/Z8 -> +9")

        # High demand should be in Z6
        if name in high_demand_products and zone != 6:
            total_penalty += 5
            violations.append(f"{name} is high demand but not in Z6 -> +5")

        # Heavy items > 40 kg must be in Z1
        if name in heavy_products and zone != 1:
            total_penalty += 4
            violations.append(f"{name} is heavy but not in Z1 -> +4")

        # Z8 restriction
        if zone == 8 and name not in eligible_z8_products:
            total_penalty += 12
            violations.append(f"{name} is not allowed in Z8 -> +12")

    # ----------------------------------------
    # 3. Same category in different zones
    # ----------------------------------------
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            if products[i]["category"] == products[j]["category"]:
                if chromosome[i] != chromosome[j]:
                    total_penalty += 3
                    violations.append(
                        f"{products[i]['name']} and {products[j]['name']} same category but different zones -> +3"
                    )

    # ----------------------------------------
    # 4. Food and chemical in same zone
    # ----------------------------------------
        # ----------------------------------------
    # 4. Food and chemical in same zone
    # ----------------------------------------
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            name1 = products[i]["name"]
            name2 = products[j]["name"]

            cond1 = name1 in food_products and name2 in chemical_products
            cond2 = name2 in food_products and name1 in chemical_products

            if cond1 or cond2:
                if chromosome[i] == chromosome[j]:
                    total_penalty += 15
                    violations.append(
                        f"{name1} and {name2} stored together in same zone -> +15"
                    )

    return total_penalty, violations

def create_chromosome():
    chromosome = []
    for i in range(len(products)):
        zone = random.randint(1, 8)
        chromosome.append(zone)
    return chromosome

def create_population(population_size):
    population = []
    for i in range(population_size):
        chromosome = create_chromosome()
        population.append(chromosome)
    return population

def tournament_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)

    best_chromosome = tournament[0]
    best_fitness = fitness(best_chromosome)[0]

    for chromosome in tournament[1:]:
        current_fitness = fitness(chromosome)[0]
        if current_fitness < best_fitness:
            best_chromosome = chromosome
            best_fitness = current_fitness

    return best_chromosome


def two_point_crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)

    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1, child2


def mutate(chromosome, mutation_rate=0.1):
    new_chromosome = chromosome.copy()

    for i in range(len(new_chromosome)):
        if random.random() < mutation_rate:
            new_chromosome[i] = random.randint(1, 8)

    return new_chromosome



def genetic_algorithm(population_size=100, generations=200, mutation_rate=0.1):
    population = create_population(population_size)

    best_chromosome = None
    best_fitness = float("inf")
    best_violations = []
    generation_reached = 0

    for generation in range(generations):
        # Sort population by fitness
        population.sort(key=lambda chromosome: fitness(chromosome)[0])

        current_best = population[0]
        current_best_score, current_best_violations = fitness(current_best)

        if current_best_score < best_fitness:
            best_fitness = current_best_score
            best_chromosome = current_best.copy()
            best_violations = current_best_violations[:]

        generation_reached = generation + 1

        print("Generation", generation + 1, "Best Fitness =", best_fitness)

        if best_fitness == 0:
            break

        new_population = []

        # Elitism: keep best chromosome
        new_population.append(population[0].copy())
        new_population.append(population[1].copy())

        while len(new_population) < population_size:
            parent1 = tournament_selection(population, tournament_size=5)
            parent2 = tournament_selection(population, tournament_size=5)

            child1, child2 = two_point_crossover(parent1, parent2)

            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)


            new_population.append(child1)

            if len(new_population) < population_size:
                new_population.append(child2)

        population = new_population

    return best_chromosome, best_fitness, best_violations, generation_reached


def print_storage_plan(chromosome):
    zone_products = {i: [] for i in range(1, 9)}
    zone_total_weight = {i: 0 for i in range(1, 9)}

    for i in range(len(chromosome)):
        zone = chromosome[i]
        product_name = products[i]["name"]
        product_weight = products[i]["weight"]

        zone_products[zone].append(product_name)
        zone_total_weight[zone] += product_weight

    print("\n===== Optimal Storage Plan =====")
    for zone in range(1, 9):
        print(f"\nZ{zone}:")
        if len(zone_products[zone]) == 0:
            print("  (empty)")
        else:
            for item in zone_products[zone]:
                print("  -", item)

        print(f"  Total Weight: {zone_total_weight[zone]} kg / {zones[zone]} kg")


def print_product_assignments(chromosome):
    print("\n===== Product Assignments =====")
    for i in range(len(chromosome)):
        print(products[i]["name"], "-> Z" + str(chromosome[i]))


best_chromosome, best_fitness, best_violations, generations_run = genetic_algorithm(
    population_size=150,
    generations=900,
    mutation_rate=0.08
)

if best_chromosome is not None:
    print_storage_plan(best_chromosome)
    print_product_assignments(best_chromosome)

    print("\n===== Final Result =====")
    print("Best Fitness Score:", best_fitness)
    print("Number of Generations Run:", generations_run)

    print("\n===== Remaining Violations =====")
    if len(best_violations) == 0:
        print("No violations. Perfect solution found.")
    else:
        for i, v in enumerate(best_violations, 1):
            print(f"{i}. {v}")


else:
    print("No solution found.")
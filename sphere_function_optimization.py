import random
import math


# Definition of the function of the Sphere
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_point = [random.uniform(lower, upper) for lower, upper in bounds]
    current_value = func(current_point)

    for _ in range(iterations):
        neighbor_point = [current_point[i] + random.uniform(-0.1, 0.1) for i in range(len(bounds))]
        neighbor_point = [max(bounds[i][0], min(bounds[i][1], neighbor_point[i])) for i in range(len(bounds))]
        neighbor_value = func(neighbor_point)

        if abs(current_value - neighbor_value) < epsilon:
            break

        if neighbor_value < current_value:
            current_point, current_value = neighbor_point, neighbor_value

    return current_point, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    current_point = [random.uniform(lower, upper) for lower, upper in bounds]
    current_value = func(current_point)

    for _ in range(iterations):
        neighbor_point = [random.uniform(lower, upper) for lower, upper in bounds]
        neighbor_value = func(neighbor_point)

        if abs(current_value - neighbor_value) < epsilon:
            break

        if neighbor_value < current_value:
            current_point, current_value = neighbor_point, neighbor_value

    return current_point, current_value


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_point = [random.uniform(lower, upper) for lower, upper in bounds]
    current_value = func(current_point)

    for _ in range(iterations):
        neighbor_point = [random.uniform(lower, upper) for lower, upper in bounds]
        neighbor_value = func(neighbor_point)

        if abs(current_value - neighbor_value) < epsilon:
            break

        if neighbor_value < current_value:
            current_point = neighbor_point
            current_value = neighbor_value
        else:
            delta = neighbor_value - current_value
            probability = math.exp(-delta / temp)
            if random.random() < probability:
                current_point = neighbor_point
                current_value = neighbor_value

        temp *= cooling_rate

    return current_point, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "Value:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Solution:", rls_solution, "Value:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Solution:", sa_solution, "Value:", sa_value)

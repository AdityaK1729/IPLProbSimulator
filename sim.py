import numpy as np

# Define the distributions
distribution_1 = {0: 612, 1: 694, 4: 229, 2: 108, 6: 165, 3: 3}
distribution_2 = {1: 79, 0: 1732}
distribution_3 = {1: 99, 0: 1712}

# Create a random variable function for each distribution
def create_random_variable(distribution):
    values = list(distribution.keys())
    probabilities = np.array(list(distribution.values()), dtype=float)
    probabilities /= probabilities.sum()  # Normalize to sum to 1
    return lambda: np.random.choice(values, p=probabilities)

# Instantiate random variables
rv1 = create_random_variable(distribution_1)
rv2 = create_random_variable(distribution_2)
rv3 = create_random_variable(distribution_3)


runs=0
wickets=0
balls=0
while balls<120 and wickets<10:
    extras=rv2()
    if extras==1:
        continue
    balls+=1
    run = rv1()
    runs+=run
    wickets+=rv3()
print(runs,wickets,balls)
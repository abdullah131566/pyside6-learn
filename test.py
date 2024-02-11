import numpy as np

# Probabilities for each outcome (1, 2, 3, 4)
p_dice = np.array([0.5, 0.1, 0.2, 0.2])  

# Number of simulations
n_simulations = 1000000

# Simulate dice rolls
dice_rolls = np.random.choice([1, 2, 3, 4], size=n_simulations, p=p_dice)

# Check each pair of outcomes
for i in range(4):
    for j in range(i + 1, 4):
        # Calculate empirical probabilities
        prob_event1 = np.mean(dice_rolls == i+1)
        prob_event2 = np.mean(dice_rolls == j+1)
        joint_prob = np.mean((dice_rolls == i+1) & (dice_rolls == j+1))

        # Check if independence condition holds
        if np.allclose(joint_prob, prob_event1 * prob_event2):
            print(f"Events: ({i+1}, {j+1}) are independent.")
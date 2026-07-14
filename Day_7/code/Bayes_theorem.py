# Bayes' Theorem Example

P_A = 0.01      # Prior Probability
P_B_given_A = 0.95
P_B = 0.06

P_A_given_B = (P_B_given_A * P_A) / P_B

print("Posterior Probability:", P_A_given_B)
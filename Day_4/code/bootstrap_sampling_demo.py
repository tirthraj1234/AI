import random

employees = [1, 2, 3, 4, 5]

bootstrap_sample = random.choices(employees, k=5)

print("Original Dataset:", employees)
print("Bootstrap Sample:", bootstrap_sample)
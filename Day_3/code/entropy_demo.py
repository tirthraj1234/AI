import math

p_yes = 0.5
p_no = 0.5

entropy = -(p_yes * math.log2(p_yes) + p_no * math.log2(p_no))

print("Entropy:", entropy)
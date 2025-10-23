P = 10000
R = 5
T = 3

SI = (P * R * T) / 100

print(f"Simple Interest: ₹{SI}")

P = 10000
R = 5
T = 3

SI = (P * R * T) / 100
CI = P * ((1 + R / 100) ** T) - P

print(f"Simple Interest: ₹{SI}")
print(f"Compound Interest: ₹{round(CI, 2)}")
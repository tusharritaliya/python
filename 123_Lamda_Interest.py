p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time (years): "))

ci = lambda p, r, t: p * (1 + r / 100) ** t - p

print("Compound Interest =", ci(p, r, t))

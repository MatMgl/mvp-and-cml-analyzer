# Portfolio Theory Project
import matplotlib.pyplot as plt
import numpy as np

# Data input
print('########## DATA INPUT ###############')
print('## (use decimal notation, e.g.: 0.1) ##')

salary = float(input("Available budget: "))
s1 = float(input("Price of risky asset 1: "))
s2 = float(input("Price of risky asset 2: "))

while True:
    mi1 = float(input('\u03BC\u2081 (expected return of asset 1): '))
    mi2 = float(input('\u03BC\u2082 (expected return of asset 2): '))

    sigma1 = float(input('\u03C3\u2081 (standard deviation of asset 1): '))
    sigma2 = float(input('\u03C3\u2082 (standard deviation of asset 2): '))

    # Covariance input – will keep asking if the value is invalid
    while True:
        sigma12 = float(input('\u03C3\u2081\u2082 (covariance between assets): '))

        ro = sigma12 / (sigma1 * sigma2)
        ro = round(ro, 2)

        if ro >= 1 or ro <= -1:
            print(f"\u03C1 = {ro}, please correct the covariance!")
        else:
            break

    r = float(input('R (risk-free rate): '))

    # Calculations
    # Minimum Variance Portfolio (MVP)
    w_mvp = (sigma2**2 - sigma12) / (sigma1**2 + sigma2**2 - 2 * sigma12)

    mi_mvp = w_mvp * mi1 + (1 - w_mvp) * mi2
    var_mvp = w_mvp**2 * sigma1**2 + (1 - w_mvp)**2 * sigma2**2 + 2 * w_mvp * (1 - w_mvp) * sigma12
    sigma_mvp = var_mvp**0.5

    if mi_mvp < r:
        print("\u03BCmp < R, please revise your data!")
    else:
        break

print('\n### Minimum Variance Portfolio (MVP) ###')
print(f"Expected return: {round(mi_mvp, 4)}")
print(f"Risk (std dev): {round(sigma_mvp, 4)}")

# Market Portfolio (MP)
c = sigma2**2 * (mi1 - r) - sigma12 * (mi2 - r)
d = sigma1**2 * (mi2 - r) - sigma12 * (mi1 - r)
w_mp = c / (c + d)

mi_mp = w_mp * mi1 + (1 - w_mp) * mi2
var_mp = w_mp**2 * sigma1**2 + (1 - w_mp)**2 * sigma2**2 + 2 * w_mp * (1 - w_mp) * sigma12
sigma_mp = var_mp**0.5

s1_mp = (w_mp * salary) / s1
s2_mp = ((1 - w_mp) * salary) / s2

print('\n### Market Portfolio (MP) ###')
print(f"Expected return: {round(mi_mp, 4)}")
print(f"Risk (std dev): {round(sigma_mp, 4)}")

print('\nInvestment plan for the market portfolio:')
if s1_mp >= 0:
    print(f"- Buy {round(s1_mp, 2)} units of risky asset 1")
else:
    print(f"- Short {round(-s1_mp, 2)} units of risky asset 1")
if s2_mp >= 0:
    print(f"- Buy {round(s2_mp, 2)} units of risky asset 2")
else:
    print(f"- Short {round(-s2_mp, 2)} units of risky asset 2")

### Charts
fig, ax = plt.subplots(figsize=(7, 5), dpi=128)
ogrs = max(sigma1, sigma2, sigma_mp)  # range for CML plot
ogrm = max(abs(mi_mvp - mi1), abs(mi_mvp - mi2), abs(mi_mvp - mi_mp))  # range for hyperbola

# Points
ax.scatter(0, r, c='brown', label='risk-free asset')
ax.scatter(sigma_mvp, mi_mvp, c='purple', label='MVP')
ax.scatter(sigma_mp, mi_mp, c='green', label='MP')
ax.scatter(sigma1, mi1, c='orange', label='risky asset 1')
ax.scatter(sigma2, mi2, c='red', label='risky asset 2')

# Capital Market Line (CML)
x = np.arange(0, ogrs + 0.2, 0.001)
y = r + x * ((mi_mp - r) / sigma_mp)

# Efficient Frontier (Hyperbola)
u = np.arange(mi_mvp, mi_mvp + ogrm + 0.15, 0.0001)

A = (mi1 - mi2)**2
B = (u - mi2)**2 * sigma1**2
C = (mi1 - u)**2 * sigma2**2
D = 2 * (u - mi2) * (mi1 - u) * sigma12

z = (1 / A) * (B + C + D)
v = z**0.5
q = u - 2 * (u - mi_mvp)

plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Expected Return')
plt.axhline(y=0, color="#cccccc")
plt.axvline(x=0, color="#cccccc")
plt.title('Portfolio Theory Project')

plt.plot(x, y, c='grey')     # CML
plt.plot(v, u, c='blue')     # Efficient frontier
plt.plot(v, q, c='blue')     # Lower branch (non-optimal)

ax.set_xlim(-0.1, ogrs + 0.1)
ax.legend(loc="upper left")

input("\nPress Enter to display the chart")
plt.show()

#################################################
input("\nPress Enter to finish the program")

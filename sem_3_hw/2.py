from numpy import random
import matplotlib.pyplot as plt
from math import sqrt

fig = plt.figure(figsize=(15, 5))


# 1
x = 0
L = [0]

for i in range(1000):
    shag = random.normal(0, 1)

    if shag > 0:
        x += 1
    else:
        x -= 1

    L.append(x)

N = [i for i in range(1001)]

ax1 = fig.add_subplot(131)
ax1.plot(N, L)
ax1.set_xlabel('N')
ax1.set_ylabel('x')
ax1.grid()


# -------------------------------------
# 2 и 3
particles = [0 for i in range(1000)]
L_2 = []

for i in range(1000):
    for j in range(1000):

        shag = random.normal(0, 1)

        if shag > 0:
            particles[j] += 1
        else:
            particles[j] -= 1

    summa = 0
    for k in range(1000):
        summa += (particles[k] ** 2)

    L_2.append(sqrt(summa / 1000))


ax2 = fig.add_subplot(132)
ax2.hist(particles, bins=30)
ax2.set_xlabel('x')
ax2.set_ylabel('Количество частиц')
ax2.grid()


N = [i for i in range(1000)]

ax3 = fig.add_subplot(133)
ax3.plot(N, L_2)
ax3.set_xlabel('N')
ax3.set_ylabel('Среднеквадратичное x')
ax3.grid()


plt.savefig('HM_sem3_2.png', dpi=300)
plt.show()


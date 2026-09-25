import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize=(16, 9), dpi=100)

# 1
x = df['SepalLengthCm']
y = df['SepalWidthCm']

args = np.polyfit(x, y, 1)
func = np.poly1d(args)

ax1 = fig.add_subplot(231)
ax1.scatter(x, y)

x_line = [min(x), max(x)]
ax1.plot(x_line, func(x_line), 'r')

ax1.set_xlabel('SepalLengthCm')
ax1.set_ylabel('SepalWidthCm')
ax1.grid()

print('SepalLengthCm - SepalWidthCm:', args)


# 2
x = df['SepalLengthCm']
y = df['PetalLengthCm']

args = np.polyfit(x, y, 1)
func = np.poly1d(args)

ax2 = fig.add_subplot(232)
ax2.scatter(x, y)

x_line = [min(x), max(x)]
ax2.plot(x_line, func(x_line), 'r')

ax2.set_xlabel('SepalLengthCm')
ax2.set_ylabel('PetalLengthCm')
ax2.grid()

print('SepalLengthCm - PetalLengthCm:', args)


# 3
x = df['SepalLengthCm']
y = df['PetalWidthCm']

args = np.polyfit(x, y, 1)
func = np.poly1d(args)

ax3 = fig.add_subplot(233)
ax3.scatter(x, y)

x_line = [min(x), max(x)]
ax3.plot(x_line, func(x_line), 'r')

ax3.set_xlabel('SepalLengthCm')
ax3.set_ylabel('PetalWidthCm')
ax3.grid()

print('SepalLengthCm - PetalWidthCm:', args)


# 4
x = df['SepalWidthCm']
y = df['PetalLengthCm']

args = np.polyfit(x, y, 1)
func = np.poly1d(args)

ax4 = fig.add_subplot(234)
ax4.scatter(x, y)

x_line = [min(x), max(x)]
ax4.plot(x_line, func(x_line), 'r')

ax4.set_xlabel('SepalWidthCm')
ax4.set_ylabel('PetalLengthCm')
ax4.grid()

print('SepalWidthCm - PetalLengthCm:', args)


# 5
x = df['SepalWidthCm']
y = df['PetalWidthCm']

args = np.polyfit(x, y, 1)
func = np.poly1d(args)

ax5 = fig.add_subplot(235)
ax5.scatter(x, y)

x_line = [min(x), max(x)]
ax5.plot(x_line, func(x_line), 'r')

ax5.set_xlabel('SepalWidthCm')
ax5.set_ylabel('PetalWidthCm')
ax5.grid()

print('SepalWidthCm - PetalWidthCm:', args)


# 6
x = df['PetalLengthCm']
y = df['PetalWidthCm']

args = np.polyfit(x, y, 1)
func = np.poly1d(args)

ax6 = fig.add_subplot(236)
ax6.scatter(x, y)

x_line = [min(x), max(x)]
ax6.plot(x_line, func(x_line), 'r')

ax6.set_xlabel('PetalLengthCm')
ax6.set_ylabel('PetalWidthCm')
ax6.grid()

print('PetalLengthCm - PetalWidthCm:', args)


plt.savefig('HM_sem3_1.png', dpi=300)
plt.show()

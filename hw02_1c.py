# Visualize the answer of the above 2 questions

import matplotlib.pyplot as plt

x, y = [], []
f1, f2 = open('hw02_1a.txt', 'r'), open('hw02_1b.txt', 'r')

for i in range(1000):
    x.append(float(f1.readline()))
    y.append(float(f2.readline()))

plt.plot(x, y)
plt.savefig('hw02_1c.png')
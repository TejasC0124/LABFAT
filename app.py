import matplotlib.pyplot as plt
import random
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
prices = []
for i in range(12):
    a=random.randint(7000,16000)
    prices.append(a)
plt.figure(figsize=(8, 4))
plt.plot(months, prices, marker='o', color='#D4AF37')
plt.title('Gold Rate Statistics')
plt.grid(True)
plt.show()


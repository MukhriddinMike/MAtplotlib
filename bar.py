import matplotlib.pyplot as plt

x = [2,5,6,8,9]
y = [3, 7, 4, 3, 2]

x2 = [1,3,7,4,10]
y2 = [2, 1, 5, 2, 8]

plt.bar(x,y, label = 'bar1', color ='pink')
plt.bar(x2,y2, label = 'bar2', color = 'salmon')

plt.xlabel('x')
plt.ylabel('y')
plt.title("MikePlusPlus\nBar")
plt.legend()
plt.show()
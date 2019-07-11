import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8,9,11,12,13,15,12,3]
y = [2,45,4,3,7,8,5,34,5,7,8,9,3,3,4]
x2 = [21,22,23,24,25,26]
y2 = [10,16,17,18,19,20]

plt.scatter(x,y, label='skat', color='salmon', marker='*',s=80)
plt.scatter(x2,y2, label='skar', color='b', marker='.',s=80)

plt.xlabel('x')
plt.ylabel('y')
plt.title('MikePlusPlus\nAbr')
plt.legend()
plt.show()

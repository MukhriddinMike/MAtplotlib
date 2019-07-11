import matplotlib.pyplot as plt

population_ages = [22,44,32,23,44,5,5,66,77,23,44,55,34,34,23,33,44,7,2,27,80,22,18,16,15,7,99]
# id_s = [x for x in range(len(population_ages))]
bins = [10,20,30,40,50,60,70,80,90,100]
plt.hist(population_ages, bins,  histtype='bar', rwidth=0.6)

# plt.bar(id_s, population_ages)
plt.xlabel('x')
plt.ylabel('y')
plt.title('MikePlusPlus\nAbr')
plt.legend()
plt.show()

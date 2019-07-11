import matplotlib.pyplot as plt

days = [1,2,3,4,5]

# sleep = [8,7,9,6,9]
# eat = [1,2,3,1,2]
 # work =[ 10,12, 13,15,11]
# study = [ 1,3,5,4,2]

slices = [7, 2,2,13]
activities = ['sleep','eat','work','study']
cols = ['c','m','r','k']

plt.pie(slices, labels=activities, colors=cols)

plt.show()
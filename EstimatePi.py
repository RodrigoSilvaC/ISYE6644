
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

class EstimatePi(object):
    def __init__(self):
        # First, we need to create the unit square and circle of radius 1/2 inside
        self.fig, self.ax = plt.subplots() #create axis and figure objects
        self.ax.set(xlim = (0,1), ylim= (0,1)) #create unit square
        self.ax.add_patch(mpl.patches.Circle((0.5,0.5), radius= 0.5, fill= False, edgecolor= 'black', linewidth = 2)) #add circle to the axis

    def simulate_darts(self, N):
        # we need to create an array with random uniform numbers for x and y coordinates
        x = np.random.uniform(0,1,N)
        y = np.random.uniform(0,1,N)
        #create category 'cat' list
        cat = []
        for i in range(N):
            # using the circle's formula, if the sum of the distances is less than radius^2 then its inside the circle
            cond = (0.5-x[i])**2 + (0.5-y[i])**2
            if cond <= 0.25:
                cat.append(1)
            else:
                cat.append(0)
        df = pd.DataFrame(dict(x = x, y = y, cat = cat))
        groups = df.groupby('cat')
        for name, group in groups:
            self.ax.scatter(group['x'], group['y'], s=3) #make scatterplot of darts grouped by category
        # pi is approximately equal to the proportion of darts inside the circle times 4
        ratio = len(df[df['cat'] == 1])/len(x)*4
        print('The estimated value for pi is: ', ratio)
        return plt.show()



a = EstimatePi()
a.simulate_darts(10000)


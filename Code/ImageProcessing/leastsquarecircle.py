import numpy as np
import matplotlib.pyplot as plt

def mls(coordinates):
    #
    # Modified least squares method
    # From "A Few Methods for Fitting Circles to Data" by Dale Umbach and Kerry N. Jones
    #

    x = []
    y = []
    Al = Bl = Cl = Dl = El = 0
    n = len(coordinates)
    for i in range(n):
        x.append(coordinates[i][0])
        y.append(coordinates[i][1])
    x2 = [i**2 for i in x]
    y2 = [i**2 for i in y]



    # Defining A
    Al = n*(n-1) * np.var(x, ddof=1) # ddof=1 sets the var function to use sample variance instead of population variance
    # print("varx: ", np.var(x))
    # print("--A: ", Al)
    # Defining B
    Bl = n*(n-1) * np.cov(np.stack((x,y), axis=0))[0][1]
    # print(n*(n-1))
    # print("covar(x,y): ", np.cov(np.stack((x,y)))[0][1] )
    # print("--B: ", Bl)
    # Defining C
    Cl = n*(n-1) * np.var(y, ddof=1)
    # print("--C: ", Cl)
    # Defining D
    Dl = 0.5*n*(n-1) * (np.cov(np.stack((x, y2), axis=0))[0][1] + np.cov(np.stack((x, x2), axis=0))[0][1])
    # print("--D: ", Dl)
    # Defining E
    El = 0.5*n*(n-1) * (np.cov(np.stack((y, x2), axis=0))[0][1] + np.cov(np.stack((y, y2), axis=0))[0][1])
    # print("--E: ", El)


    #Definitions for a and b
    a = ( (Dl * Cl) - (Bl * El) ) / ( (Al * Cl) - Bl**2 ) 
    b = ( (Al * El) - (Bl * Dl) ) / ( (Al * Cl) - Bl**2 )

    r = 0
    for i in range(n):
        r += ( np.sqrt( (x[i] - a)**2 + (y[i] - b)**2 )  / n )

    # print(a),
    # print(b)
    # print(r)

    # fig, ax = plt.subplots()
    # ax.scatter(x,y)
    # ax.add_patch(plt.Circle((a, b), r, color='black', fill=False))
    # plt.show()

    return (a, b, r)


lst = [[0,1], [2,1], [1,0], [1,2], [0.03,1.1]]
# print(len(lst))
mls(lst)
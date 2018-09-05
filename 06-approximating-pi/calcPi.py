import numpy as np

def calc_Pi(numberOfPoints):
	n = numberOfPoints
	randX = np.random.random(n)
	randY = np.random.random(n)
	
	valsIn = np.sqrt(randX**2+randY**2)<=1
	valsOut = np.sqrt(randX**2+randY**2)>1
	
	outX = randX[valsOut]
	outY = randY[valsOut]
	
	inX = randX[valsIn]
	inY = randY[valsIn]
	
	
	return (4*np.sum(np.sqrt(randX**2+randY**2)<1)/n, outX, outY, inX, inY)
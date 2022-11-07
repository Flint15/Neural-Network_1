"""import numpy as np
weights = np.array([0.5,0.48,-0.7])
alpha = 0.1
streetlights = np.array([[1,0,1],
			    		 [0,1,1],
						 [0,0,1],
						 [1,1,1],
						 [0,1,1],
						 [1,0,1]])
walk_vs_stop = np.array([0,1,0,1,1,0])
for i in range(40):	
	error_for_all_lights = 0
	for i in range(len(walk_vs_stop)):
		input = streetlights[i]
		goal_prediction = walk_vs_stop[i]
		pred = input.dot(weights)
		error = (pred - goal_prediction) ** 2
		error_for_all_lights += error
		delta = pred - goal_prediction
		weights -= alpha * (input * delta)
		print("pred:" + str(pred),weights)
	print(i,"error:" + str(error_for_all_lights) + "\n")"""
import numpy as np
weights = np.array([0.5,0.48,-0.7])
alpha = 0.1
streetLights = np.array([[1,0,1],
						 [0,1,1],
						 [0,0,1],
						 [1,1,1],
						 [0,1,1],
						 [1,0,1]])
walk_vs_stop = np.array([0,1,0,1,1,0])
for i in range(40):	
	error_for_all_lights = 0
	for i in range(len(walk_vs_stop)):
		input = streetLights[i]
		goal_prediction = walk_vs_stop[i]
		pred = input.dot(weights)
		error = (pred - goal_prediction) ** 2
		error_for_all_lights += error
		delta = pred - goal_prediction
		weights -= alpha * (input * delta)
		print("pred:" + str(pred),weights)
	print("error:" + str(error_for_all_lights) + "\n")
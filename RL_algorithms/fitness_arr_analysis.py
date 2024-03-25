import numpy as np
path = '../Results/DDQN/D2sparse/1025/fitness_0.npy'
arr = np.load(path)

cnt = 100
sum(arr[-cnt:])/cnt
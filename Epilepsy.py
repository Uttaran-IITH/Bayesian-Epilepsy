import numpy as np
y = np.array([[5,3,3,3],[3,5,3,3],[2,4,0,5],[4,4,1,4],[7,18,9,21],[5,2,8,7],[6,4,0,2],[40,20,21,12],[5,6,6,5],
   [14,13,6,0],[26,12,6,22],[12,6,8,4],[4,4,6,2],[7,9,12,14],[16,24,10,9],[11,0,0,5],[0,0,3,3],[37,29,28,29],
   [3,5,2,5],[3,0,6,7],[3,4,3,4],[3,4,3,4],[2,3,3,5],[8,12,2,8],[18,24,76,25],[2,1,2,1],[3,1,4,2],
   [13,15,13,12],[11,14,9,8],[8,7,9,4],[0,4,3,0],[3,6,1,3],[2,6,7,4],[4,3,1,3],[22,17,19,16],
   [5,4,7,4],[2,4,0,4],[3,7,7,7],[4,18,2,5],[2,1,1,0],[0,2,4,0],[5,4,0,3],[11,14,25,15],[10,5,3,8],
   [19,7,6,7],[1,1,2,3],[6,10,8,8],[2,1,0,0],[102,65,72,63],[4,3,2,4],[8,6,5,7],[1,3,1,5],[18,11,28,13],
   [6,3,4,0],[3,5,4,3],[1,23,19,8],[2,3,0,1],[0,0,0,0],[1,4,3,2]])

Trt = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0,0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1])

Base = np.array([11, 11, 6, 8, 66, 27, 12, 52, 23, 10, 52, 33, 18, 42, 87, 50, 18, 111,
        18, 20, 12, 9, 17, 28, 55, 9, 10, 47, 76, 38, 19, 10, 19, 24, 31, 14,
        11, 67, 41, 7, 22, 13, 46, 36, 38, 7, 36, 11, 151, 22, 41, 32, 56, 24,
        16, 22, 25, 13, 12])

Age = np.array([31, 30, 25, 36, 22, 29, 31, 42, 37, 28, 36, 24, 23,36, 26, 26, 28, 31,
        32, 21, 29, 21, 32, 25, 30, 40, 19, 22, 18, 32, 20, 30, 18, 24, 30, 35,
        27, 20, 22, 28, 23, 40, 33, 21, 35, 25, 26, 25, 22, 32, 25, 35, 21, 41,
        32, 26, 21, 36, 37])

V4 = np.array([0, 0, 0, 1])

print('Y shape: ',y.shape)
print('Trt shape: ',Trt.shape)
print('Base shape', Base.shape)
print('Age shape: ',Age.shape)
print('V4 shape: ',V4.shape)

dataset = {}
dataset['y'] = y
dataset['Trt'] = Trt
dataset['Base'] = Base
dataset['Age'] = Age

import numpy as np
A=np.array([[1,-1],[1,1]])
B=np.array([4,10])
c=np.linalg.det(A)
if(c==0):
    print("no")
else:
    x=np.linalg.solve(A,B)
    print(x)

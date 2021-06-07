import numpy as np
l=list(map(int,input().split()))
n=np.array(l)
unique, frequency = np.unique(n,return_counts = True) 
  
# convert both into one numpy array
count = np.asarray((unique, frequency ))
print(count)

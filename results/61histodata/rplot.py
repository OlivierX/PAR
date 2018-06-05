import numpy as np
import matplotlib.pyplot as plt

def searchdata(path,target_start,target_end):
    data = list()
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("End of epoch"):
                continue
            line = line.split(target_start)[1]
            line = line.split(target_end)[0]
            line = float(line)
            data.append(line)
    print(len(data))
    return(data)
    
if __name__ == "__main__":
    errG = searchdata('code.txt','Err_G:','Err_D:')
    errD = searchdata('code.txt','Err_D:','ErrL1:')
    errL1 = searchdata('code.txt','ErrL1:','\n')
    errG20 = []
    errD20 = []
    errL120 = []
    for i in range(4000):
        if i%20 == 0 :
            errG20.append(errG[i])
            errD20.append(errD[i])
            errL120.append(errL1[i])
    plt.figure(1)
    x = np.linspace(0,200,200)
    plt.figure(1)
    plt.plot(x,errG20,color='green',label='Err_G')
    plt.plot(x,errD20,color='blue',label='Err_D')
    plt.plot(x,errL120,color='red',label='ErrL1')
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.show()
    

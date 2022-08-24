import matplotlib.pyplot as plt
import random
import numpy as np

class Node:
    def __init__(self, num, transmitStatus = False, numOfPackets = 1):
        self.num = num
        self.transmitStatus = transmitStatus
        self.numOfPackets = numOfPackets

def RandomStatus(n):
    if random.randint(1,n) == 1:
        return True
    return False

efficiency = []
numOfNodes = 50
AveragingNum = 50

for i in range(1, numOfNodes):
    countSuccess=0
    countCollision=0
    countEmpty=0
    listOfNodes = []
    AveragingEff = 0
    for j in range(AveragingNum):
        for j in range(i):
            listOfNodes.append( Node(j+1))
        NumOfSlots = 100000
        for k in range(NumOfSlots):
            NumTrue = 0
            for node in listOfNodes:
                if(node.numOfPackets!=0):
                    node.transmitStatus = RandomStatus(i)
                # print(node.num, node.transmitStatus, node.numOfPackets)
                if(node.transmitStatus==True):
                    NumTrue+=1
            if(NumTrue==0):
                # print("Empty")
                countEmpty+=1
            elif(NumTrue==1):
                for node in listOfNodes:
                    if(node.transmitStatus==True):
                        node.numOfPackets-=1
                        node.transmitStatus=False
                # print("Success")
                countSuccess+=1
            else:
                # print("Collision")
                countCollision+=1
            if(countSuccess == len(listOfNodes)):
                # print(len(listOfNodes))
                NumOfSlots=countSuccess+countEmpty+countCollision
                # print(i)
                break
        AveragingEff += (countSuccess/NumOfSlots)
    print(i)
    # plt.plot(i,countSuccess/NumOfSlots)
    # print("Success:",countSuccess, "Collision",countCollision, "Empty", countEmpty)
    # print("Efficiency", countSuccess/NumOfSlots)
    efficiency.append(AveragingEff/AveragingNum)


sum = 0
for s in efficiency:
    sum+=s

print(sum/len(efficiency))


# x axis values
x = np.arange(1,numOfNodes)
print(x)
# corresponding y axis values
y = [2,4,1]
  
# plotting the points 
plt.plot(x, efficiency)  
# naming the x axis
plt.xlabel('Node - axis')
# naming the y axis
plt.ylabel('Efficiency - axis')
plt.axis([1, numOfNodes, 0, 1])
plt.grid(linestyle='--') 
# function to show the plot
plt.show()
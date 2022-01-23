from math import exp, log

#dataset is a 3d list in the form [[[inputs],[outputs]],[[inputs],[outputs]]...]
#thetas is a 1d list of values for weights starting from all the weights to the top left node, and iterating down the layers, layer by layer
#shape specifies the shape of the neural network. For a network with 2 inputs, a hidden layer with 5, and 2 outputs, shape would be [2,5,2]
#shape does not take into account the 1.0's in each layer
#lamb specifies the weight of regularisation

def getcost(dataset,thetas,shape,lamb): #returns a cost value to be minimised
    weights = inflate(thetas,shape)
    cost = 0
    for data in dataset:
        ev = neteval(data[0],weights)  #computing cost in output
        for x in range(1,len(ev[-1])):
            cost += data[1][x-1] * log(ev[-1][x]) + (1 - data[1][x-1]) * log(1 - ev[-1][x])
    cost /= (-1 * len(dataset))
    
    weightsum = 0    #computing cost in regularisation
    weightnum = 0
    for a in weights:
        for b in a:   
            for c in b[1:]:
                weightsum += c**2
                weightnum += 1
    cost += weightsum * (lamb / (2 * weightnum))
    
    return cost

def getcostderivs(dataset,thetas,shape,lamb): #returns the gradients for a list of thetas, in a list
    weights = inflate(thetas,shape)
    derivs = []
    nodes = []
    for a in weights:      #creating a list of 0's for each node, and a list of 0 for each gradient
        derivs.append([])
        nodes.append([0])
        for b in a:
            derivs[-1].append([])
            nodes[-1].append(0)
            for c in b:
                derivs[-1][-1].append(0)
    
    for data in dataset:
        for row in nodes:      # setting node list back to 0
            for node in row:
                node = 0
        
        fwdprop = neteval(data[0],weights)
        
        for x in range(1,len(nodes[-1])):    #computing backprop for final layer of nodes
            nodes[-1][x] = fwdprop[-1][x] - data[1][x-1]
            
        for x in range(len(nodes)-2,-1,-1):    #computing backprop for other node layers (not computed for first layer)
            for y in range(len(nodes[x])):
                for z in range(1,len(nodes[x+1])):
                    nodes[x][y] += nodes[x+1][z] * weights[x+1][z-1][y] * fwdprop[x+1][y] * (1 - fwdprop[x+1][y])
                    
        for x in range(len(derivs)):   #adding to weight gradients
            for y in range(len(derivs[x])):
                for z in range(len(derivs[x][y])):
                    derivs[x][y][z] += fwdprop[x][z] * nodes[x][y+1]
                    
    for x in range(len(derivs)):    #adding normalisation and taking average
        for y in range(len(derivs[x])):
            for z in range(len(derivs[x][y])):
                if z != 0:
                    derivs[x][y][z] += lamb * weights[x][y][z]
                derivs[x][y][z] /= len(dataset)
                
    return deflate(derivs)

def neteval(inputs,weights): #returns the value at each node after foreward propagagation. 2d list returned has 1.0 at the beginning of every row, including the final row
    fwdprop = [[1.0]]
    fwdprop[0].extend(inputs)
    
    for a in range(len(weights)):
        fwdprop.append([1.0])
        for b in range(len(weights[a])):
            fwdprop[-1].append(0)
            for c in range(len(weights[a][b])):
                fwdprop[-1][-1] += weights[a][b][c] * fwdprop[a][c]
            fwdprop[-1][-1] = sig(fwdprop[-1][-1])
            
    return fwdprop

def sig(x): # applies the sigmoid function
    return (1 / (1 + exp(x * -1)))
    
def inflate(thetas,shape): # using the specified shape of the neural net, takes a 1d list of thetas and returns a 3d list of these
    weights = []
    counter = 0
    for x in range(1,len(shape)):
        weights.append([])
        for y in range(shape[x]):
            weights[-1].append([])
            for z in range(shape[x-1]+1):
                weights[-1][-1].append(thetas[counter])
                counter += 1
    
    return(weights)

def deflate(weights): #takes a 3d list of gradients and compresses to 1d
    thetas = []
    for a in weights:
        for b in a:
            for c in b:
                thetas.append(c)
                
    return thetas
    
if __name__ == '__main__': #test using a simple neural net shape with one hidden layer

    thetas = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
    shape = [2,2,2]
    inputs = [2.0,3.0]
    dataset = [[[2.0,3.0],[0.0,1.0]],[[4.0,4.0],[1.0,1.0]]]
    lamb = 0
    
    print(inflate(thetas,shape))
    print(deflate(inflate(thetas,shape)))
    print(sig(6))
    print(neteval(inputs,inflate(thetas,shape)))
    print(getcost(dataset,thetas,shape,lamb))
    print(getcostderivs(dataset,thetas,shape,lamb))

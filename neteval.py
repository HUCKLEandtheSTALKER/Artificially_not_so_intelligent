from math import exp, log

#inputs is an array of values
#weights is a 3d array of values

def getcost(dataset,thetas,shape,lamb):
    weights = inflate(thetas,shape)
    cost = 0
    for data in dataset:
        ev = neteval(data[0],weights)
        for x in range(len(ev[-1])):
            cost += data[1][x] * log(ev[-1][x]) + (1 - data[1][x]) * log(1 - ev[-1][x])
        cost /= (-1 * len(dataset))
    
    weightsum = 0
    weightnum = 0
    for a in weights:
        for b in a:
            for c in b[1:]:
                weightsum += c**2
                weightnum += 1
    cost += weightsum * (lamb / (2 * weightnum))

def getcostderivs(dataset,thetas,shape,lamb):
    weights = inflate(thetas,shape)
    derivs = []
    nodes = []
    for a in weights:
        derivs.append([])
        nodes.append([0])
        for b in a:
            derivs[-1].append([])
            nodes[-1].append(0)
            for c in b:
                derivs[-1][-1].append(0)
                
    for data in dataset:
        for row in nodes:
            for node in row:
                node = 0
        
        fwdprop = neteval(data[0],weights)
        
        for x in range(1,len(nodes[-1])):
            nodes[-1][x] = fwdprop[-1][x-1] - data[1][x-1]
            
        for x in range(len(nodes)-2,-1,-1):
            for y in range(len(nodes[x])):
                for z in range(1,len(nodes[x+1])):
                    nodes[x][y] += nodes[x+1][z] * weights[x+1][z][y] * fwdprop[x][y] * (1 - fwdprop[x][y])
                    
        for x in range(len(derivs)):
            for y in range(len(derivs[x])):
                for z in range(len(derivs[x][y])):
                    derivs[x][y][z] += fwdprop[x][z] * nodes[x][y+1]
                    
    for x in range(len(derivs)):
        for y in range(len(derivs[x])):
            for z in range(len(derivs[x][y])):
                if z != 0:
                    derivs[x][y][z] += lamb * weights[x][y][z]
                derivs[x][y][z] /= len(dataset)
                
    return deflate(weights)

def neteval(inputs,weights):
    finalvals = [[1.0]]
    finalvals[0].extend(inputs)
    retvals = [1.0]
    retvals.extend(inputs)
    newvals = [1.0]
    for layer in weights:
        for node in layer:
            newval = 0
            for x in range(len(retvals)):
                newval += retvals[x] * node[x]
            newvals.append(sig(newval))
        retvals.clear()
        retvals.extend(newvals)
        finalvals.append(retvals)
        newvals.clear()
        newvals.append(1.0)
    finalvals[-1].pop(0)
    return finalvals

def sig(x):
    return (1 / (1 + exp(x * -1)))
    
def inflate(thetas,shape):
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

def deflate(weights):
    thetas = []
    for a in weights:
        for b in a:
            for c in b:
                thetas.append(c)
                
    return thetas
    
if __name__ == '__main__': #test using the nor function

    weights = [[[10.0,-20.0,-20.0]]]
    print(neteval([0,0],weights))

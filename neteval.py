from math import exp

#inputs is an array of values
#weights is a 3d array of values

def neteval(inputs,weights):
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
        newvals.clear()
        newvals.append(1.0)
    return retvals[1:]

def sig(x):
        return (1 / (1 + exp(x * -1)))
    
if __name__ == '__main__': #test using the nor function

    weights = [[[10.0,-20.0,-20.0]]]
    print(round(neteval([0,0],weights)[0]))
    print(round(neteval([0,1],weights)[0]))
    print(round(neteval([1,0],weights)[0]))
    print(round(neteval([1,1],weights)[0]))

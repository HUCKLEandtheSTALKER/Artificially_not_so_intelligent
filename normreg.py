f = open(input('file name: '),'r')
points = []
for line in f:
    points.append([])
    for item in line.split():
        points[-1].append(float(item))

m = len(points)        
avgx = sum([i[0] for i in points]) / m
avgy = sum([i[1] for i in points]) / m
avgxsq = sum([i[0]**2 for i in points]) / m
avgxy = sum([i[0]*i[1] for i in points]) / m

theta0 = avgy - (avgx * (avgxy - avgx * avgy)) / (avgxsq - avgx**2)
theta1 = (avgxy - avgx * avgy) / (avgxsq - avgx**2)

print(theta0,theta1)

import matplotlib.pyplot as plt

def sheep(f, y0, n): #ODE function to calculate growth
    results = [y0]
    while len(results) < n:
        results.append(f(results[-1]))
    return results

sheepgrowth = lambda nsheep: nsheep + nsheep // 2 #Function that calculates number of sheeps after reproduction starting with numSheeps number of sheeps
initialSheeps = 2#Number of initial sheeps on reproduction
iterations = 10 #Number of iterations of reproduction

values = sheep(sheepgrowth, initialSheeps, iterations) #Results from reproduction of sheeps
ROC = [0] + [values[i] - values[i-1] for i in range(1, len(values))] #Rate of change of sheep growth
even = []
odd = []
for i in range(0,iterations-1):
    if values[i] % 2 == 0:
        even.append(ROC[i+1])
    else:
        odd.append(ROC[i+1])

plt.plot(range(iterations), values, label="Population of sheeps")
plt.plot(range(iterations), ROC, label="Rate of Change")
plt.plot(range(len(even)), even, label="even rate of Change")
plt.plot(range(len(odd)), odd, label="odd ate of Change")
plt.xlabel('number of iteration')
plt.ylabel('number of sheeps')
plt.legend()
plt.show()

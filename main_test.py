from random import randint
import math
global Bitcount,PoolSize
Bitcount = 5
PoolSize = 10
class Chromosome:

    def __init__(self,Value):# runs on intitiaion
        self.Fitness = 0 # directly proportional to the ideality of the chromosome
        self.Genes = Value 
        
        # Genes[0] = 1 if positive number or 0 if negative
        # Genes[1:5] if the number in binary format             
    def Value(self):
        #The Value of genes
        if self.Genes != 'Null':
            decimal = 0
            for i in range(-1,-Bitcount-1,-1):
                decimal += self.Genes[1:][i]*(2**(abs(i)-1))
            decimal *= (-1)*((-1)**self.Genes[0])
            return decimal
        else:
            return 'Null'

    def __add__(self, other):#single point crossover
        cross_over_point = randint(1,Bitcount)

        child1 = self.Genes[:cross_over_point]
        for i in other.Genes[cross_over_point:]:
            child1.append(i)
        child2 = other.Genes[:cross_over_point]
        for i in self.Genes[cross_over_point:]:
            child2.append(i)


        #MUTATION
        mutation = randint(0,100)
        if mutation > 40:

            flip_Bit = randint(0,Bitcount)
            child1[flip_Bit] = 1-child1[flip_Bit]
            flip_Bit = randint(0,Bitcount)
            child2[flip_Bit] = 1-child2[flip_Bit]
        return (Chromosome(child1),Chromosome(child2))
                
def Population():


    raw_pool = ([[randint(0,1) for x in range(Bitcount+1)] for i in range(10)])
    res = []
    for i in raw_pool:

        if i not in res:
            res.append(i)
    

    while len(res) != len(raw_pool):
        x = [randint(0,1) for x in range(Bitcount+1)]
        if x not in res:
            res.append(x)
            

    pool = []


    for i in res:
        x = []
        for j in i:
            x.append(int(j))
        pool.append(Chromosome(x))
    return pool
    
                
def Fitness_Function(chromosome):
    x = chromosome.Value()

    #here the function is F = x^3-220x^2+1600x-480000
    #find maximum Value of it
    chromosome.Fitness = x**3-(220*(x**2))+(1600*x)-480000

def Selection(Pool):
    
    arr = []
    for i in Pool:
        Fitness_Function(i)
        arr.append(i.Fitness)

        
    #sort using insertion sort

    for i in range(1, len(arr)):
  
        key = arr[i]
        keyl= Pool[i]
        j = i-1
        while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                Pool[j+1] = Pool[j]
                j -= 1
        arr[j+1] = key
        Pool[j+1] = keyl

    return Pool[:PoolSize//2+2]
        
   
Pool = Population()

selection = Selection(Pool)
for i in selection:
    print(i.Genes,'___________',i.Value(),'__________',i.Fitness)
print('-----------------------------------------')
End_Pool = []
generations = 0
while True:
    
    Pool = []
    Values = []
    for i in selection:
        for j in selection:
            if i != j:
                z = i+j
                for k in z:
                    if k.Value() not in Values:
                        Pool.append(k)
                        Values.append(k.Value())

    selection = Selection(Pool)
    generations+=1
    fitness = set()
    for i in selection:
        fitness.add(i.Fitness)
    End_Pool.append(fitness)
    if len(End_Pool) == 3:
        if End_Pool[0] == End_Pool[1] and End_Pool[0] == End_Pool[2]:
            break
        else:
            End_Pool = []
for i in selection:
    print('Maximum at dependent variable :',i.Value(),' with function value: ',i.Fitness)
    break   
print("Generations taken: ",generations)




    



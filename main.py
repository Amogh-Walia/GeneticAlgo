from random import randint
import math
global Bitcount,PoolSize,DecimalPoint,DecimalBin
DecimalBin = 10
DecimalPoint =3
Bitcount = 5
PoolSize = 10
string = "here the function is F = x^3-220x^2+1600x-480000"

class Chromosome:
    '''
    Self.Genes = [[WholeNumberPart],[DecimalPart]]

    '''
    def __init__(self,Value):# runs on intitiaion
        self.Fitness = 0 # directly proportional to the ideality of the chromosome
        self.Genes = Value
        
        # Genes[0] = 1 if positive number or 0 if negative
        # Genes[1:5] if the number in binary format             
    def Value(self):
        #The Value of genes
        if self.Genes[0] != 'Null':
            decimal = 0
            fraction = 0

            for i in range(-1,-Bitcount-1,-1):#computing the whole part
                
                decimal += self.Genes[0][1:][i]*(2**(abs(i)-1))

            for i in range(-1,-DecimalBin-1,-1):#computing the Fraction part

                fraction += (self.Genes[1][1:][i]*(2**(abs(i)-1)))
            decimal+=fraction/(10**DecimalPoint)#Adding them together
            decimal *= (-1)*((-1)**self.Genes[0][0])#Taking care of the sign
            decimal = float("{:.3f}".format((decimal)))#Clipping to required decimal places
            return decimal
        else:
            return 'Null'

    def __add__(self, other):#single point crossover
        #Crossover for the whole part and fraction part thru loop
        cross_over_point = [randint(1,Bitcount),randint(1,DecimalBin)]
        child1 = []
        child2 = []

        for k in (0,1):
            child1.append(self.Genes[k][:cross_over_point[k]])
            for i in other.Genes[k][cross_over_point[k]:]:
                child1[k].append(i)

            child2.append(other.Genes[k][:cross_over_point[k]])

            for i in self.Genes[k][cross_over_point[k]:]:
                child2[k].append(i)


        #print(child2)
        #MUTATION
        mutation = randint(0,100)
        if mutation > 40:
            flip_Bit = [randint(1,Bitcount),randint(1,DecimalBin)]
            for k in (0,1):
                

                child1[k][flip_Bit[k]] = 1-(child1[k][flip_Bit[k]])
                child2[k][flip_Bit[k]] = 1-(child2[k][flip_Bit[k]])
        
        return (Chromosome(child1),Chromosome(child2))
                
def Population():


    raw_poolW = ([[randint(0,1) for x in range(Bitcount+1)] for i in range(10)])
    x = randint(0,999)
    
    raw_poolD =  ([[randint(0,1) for x in range(DecimalBin+1)] for i in range(10)])

    raw_pool = []

    for i in range(0,len(raw_poolW)):
        raw_pool.append([raw_poolW[i],raw_poolD[i]])

    res = []


    for i in raw_pool:
        
        if i not in res:
            res.append(i)
    

    while len(res) != len(raw_pool):
        raw_poolW = ([[randint(0,1) for x in range(Bitcount+1)]])
        #raw_poolD = ([int(i) for i in bin(randint(0,int('9'*DecimalPoint)))[2:]])
        raw_poolD = ([[randint(0,1) for x in range(DecimalBin+1)]])
        x = [[raw_poolW[i],raw_poolD[i]]]
        if x not in res:
            res.append(x)
            


    pool = []


    for x in res:
        pool.append(Chromosome(x))
    return pool
    
                
def Fitness_Function(chromosome):
    x = chromosome.Value()

    
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
#------------------------------PRETTY PRINT-----------------------------------
data1 = [['WHOLE No CHROMOSOME'],['FRACTION CHROMOSOME'],['VALUE'],['FITNESS']]
columns = []
data = []
for i in selection:
    data.append([i.Genes[0],i.Genes[1],i.Value(),i.Fitness])
for i in data1:
    columns.append(i[0])
width = [0,0,0,0]
data.insert(0,tuple(columns))

for row in data:
    t = 0
    for column in row:
        if width[t] < len(str(column)):
            width[t] = len(str(column))
        t+=1
        
for row in data:
    t=0
    
    for column in row:
        x = width[t]
        
        for i in str(column):
            print (i,end = '')
            x-=1
            
        while x != 0:
           print(' ',end = '')
           x-=1
        t+=1
        print(' | ',end ='')
    print()
        
print()
print()

#----------------------------------DRIVER CODE-----------------------------------
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
    print(string)
    print('Maximum at dependent variable :',i.Value(),' with function value: ',i.Fitness)
    break   
print("Generations taken: ",generations)




    



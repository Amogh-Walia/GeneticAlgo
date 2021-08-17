from random import randint
import math
global Bitcount,PoolSize,DecimalPoint,DecimalBin,Variables
Variables = 2
DecimalBin = 10
DecimalPoint =3
Bitcount = 5
PoolSize = 10
class Chromosome:
    '''
    Self.Genes[KEY] = [[WholeNumberPart],[DecimalPart]]
    KEY = 0,1,2,3,4,5......

    '''
    def __init__(self,Values):# runs on intitiaion
        #Values = [[[WholeNumberPart],[DecimalPart]],[[WholeNumberPart],[DecimalPart]]]
        self.Fitness = 0# directly proportional to the ideality of the chromosome
        self.Genes = {}
        for i in range(0,len(Values)):
            self.Genes[i] = Values[i]
        
        # Genes[0] = 1 if positive number or 0 if negative
        # Genes[1:5] if the number in binary format             
    def Value(self):
        #The Value of genes
        decimal_Dictionary = {}
        for it in self.Genes:
            Genes = self.Genes[it]
            #print(Genes)

            decimal = 0
            fraction = 0

            for i in range(-1,-Bitcount-1,-1):#computing the whole part
                decimal += Genes[0][1:][i]*(2**(abs(i)-1))

            for i in range(-1,-DecimalBin-1,-1):#computing the Fraction part

                fraction += (Genes[1][1:][i]*(2**(abs(i)-1)))

            decimal+=fraction/(10**DecimalPoint)#Adding them together
            decimal *= (-1)*((-1)**Genes[0][0])#Taking care of the sign
            decimal = float("{:.3f}".format((decimal)))#Clipping to required decimal places
            decimal_Dictionary[it] = decimal
        return decimal_Dictionary


    def CrossOver(self,Chromo1,Chromo2):#single point crossover
        #Crossover for the whole part and fraction part thru loop
        cross_over_point = [randint(1,Bitcount),randint(1,DecimalBin)]
        child1 = []
        child2 = []

        for k in (0,1):
            child1.append(Chromo1[k][:cross_over_point[k]])
            for i in Chromo2[k][cross_over_point[k]:]:
                child1[k].append(i)

            child2.append(Chromo2[k][:cross_over_point[k]])

            for i in Chromo1[k][cross_over_point[k]:]:
                child2[k].append(i)





        #MUTATION
        mutation = randint(0,100)
        if mutation > 40:
            flip_Bit = [randint(1,Bitcount),randint(1,DecimalBin)]
            for k in (0,1):
                

                child1[k][flip_Bit[k]] = 1-(child1[k][flip_Bit[k]])
                child2[k][flip_Bit[k]] = 1-(child2[k][flip_Bit[k]])

        return (child1,child2)

    def __add__(self,other):
        children = {}
        '''
        children = { 0: (child1X,child2X);
                     1: (child1Y,child2Y)}
        '''
        for i in self.Genes:
            children[i] = self.CrossOver(self.Genes[i],other.Genes[i])
        Child1 = []
        Child2 = []
        
        for i in children:
            Child1.append(children[i][0])
            Child2.append(children[i][1])
        
        return (Chromosome(Child1),Chromosome(Child2))
            
        
def Population():
    pool = []
    res = {}
    for it in range(0,Variables):
        res[it] = []
        raw_poolW = ([[randint(0,1) for x in range(Bitcount+1)] for i in range(10)])
        x = randint(0,999)
        
        raw_poolD =  ([[randint(0,1) for x in range(DecimalBin+1)] for i in range(10)])

        raw_pool = []

        for i in range(0,len(raw_poolW)):
            raw_pool.append([raw_poolW[i],raw_poolD[i]])

        
    

        for i in raw_pool:
            
            if i not in res[it]:
                res[it].append(i)
        

        while len(res[it]) != len(raw_pool):
            raw_poolW = ([[randint(0,1) for x in range(Bitcount+1)]])
            #raw_poolD = ([int(i) for i in bin(randint(0,int('9'*DecimalPoint)))[2:]])
            raw_poolD = ([[randint(0,1) for x in range(DecimalBin+1)]])
            x = [[raw_poolW[i],raw_poolD[i]]]
            if x not in res[it]:
                res[it].append(x)
                

        

    for i in range(0,len(res[0])):
        #pool.append(Chromosome())
        temp_array = []
        for j in res:
            temp_array.append(res[j][i])

        pool.append(Chromosome(temp_array))


    return pool
    
                
def Fitness_Function(chromosome):
    var = chromosome.Value()
    x = var[0]
    y = var[1]
    #here the function is F = f(x, y) = -(x**2)-(y**2)+6
    #find maximum Value of it
    chromosome.Fitness = -(x**2)-(y**2)+6


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


#-----------------------------XTRA FUNMCTIONS--------------------------
def List_to_String(array):
    string = ''
    for i in array:
        string+=str(i)
    return string

#------------------------------PRETTY PRINT-----------------------------------

data1 = [['VAR1 CHROMOSOME'],['VAR2 CHROMOSOME'],['VALUES'],['FITNESS']]
columns = []
data = []
for i in selection:
    VALUES = []
    CHROM1 = ''
    CHROM2 = ''
    kk = i.Value()
    for j in kk:
        
        VALUES.append(kk[j])
    CHROM1 = [List_to_String(i.Genes[0][0]),List_to_String(i.Genes[0][1])]
    CHROM2 = [List_to_String(i.Genes[1][0]),List_to_String(i.Genes[1][1])]
    data.append([CHROM1,CHROM2,VALUES,i.Fitness])
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
generations = [0,0,0,0]
Times = 0
Final = []
while Times !=4:
    
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
    generations[Times]+=1

    fitness = set()
    for i in selection:
        fitness.add(i.Fitness)
    End_Pool.append(fitness)
    if len(End_Pool) == 3:
        if End_Pool[0] == End_Pool[1] and End_Pool[0] == End_Pool[2]:
            Times+=1
            Final.append(selection[0])
            End_Pool = []
            
        else:
            End_Pool = []






data1 = [['X'],['Y'],['VALUE']]
columns = []
data = []
for i in Final:

    data.append([i.Value()[0],i.Value()[1],i.Fitness])
for i in data1:
    columns.append(i[0])
width = [0,0,0]
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
  
print("Generations taken: ",generations)



    



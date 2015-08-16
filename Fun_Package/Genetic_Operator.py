__author__ = 'Jessie'
import random

def Crossover_Operator(Parent1, Parent2):
    Crossover_Probability = 85
    Random_Num = random.randint(0,100)
    if Random_Num <= Crossover_Probability:
        Length = len(Parent1)
        Cross_Point = random.randint(2,Length-1)
        Child1 = Parent1[0:Cross_Point] + Parent2[Cross_Point:Length]
        Child2 = Parent2[0:Cross_Point] + Parent1[Cross_Point:Length]
    else:
        Child1 = Parent1
        Child2 = Parent2
    return {'Child1':Child1,'Child2':Child2}

def Mutation_Operator(Individual):
    Length = len(Individual)
    Mutated_Indidual = []
    for ele in list(Individual):
        #Mutation_Probability = int(100/Length)
        Mutation_Probability = 20
        Rand_Num = random.randint(0,100)
        if Rand_Num < Mutation_Probability:
            if ele =='1':
                Mutated_Indidual.append('0')
            else:
                Mutated_Indidual.append('1')
        else:
            Mutated_Indidual.append(ele)
    return ''.join(Mutated_Indidual)

def Selection_Operator(Population_Quality):
    Elites = {}
    Good_Individual = {}
    Ranged_Population_Quality = sorted(Population_Quality.items(), key=lambda x:x[1])
    for e in range(0,200):
        if e < 20:
            Elites[Ranged_Population_Quality[e][0]] = Ranged_Population_Quality[e][1]
        else:
            Good_Individual[Ranged_Population_Quality[e][0]] = Ranged_Population_Quality[e][1]

    return {'Good_Individual':Good_Individual,'Elites':Elites}


__author__ = 'Jessie'
import random
from Fitness_Function import *
from Genetic_Operator import *
def Genetic_Algorithm(EM,EMB,Results,N,M,Mean_Square_Residue_Threshold):
    Whole_Ind = len(EMB)
    Population_Index = [random.randint(0,Whole_Ind-1) for i in range(0,200)]
    First_Generation = [EMB[ele] for ele in Population_Index]
    Elites = []
    Generation_Num = 100
    for Generation in range(0,Generation_Num):
        # offspring compete with the old individuals for a place in the next generation
        if Generation == Generation_Num/4:
            print '25% generation has been done...'
        elif Generation == Generation_Num/2:
            print '50% generation has been done...'
        elif Generation == Generation_Num *3/4:
            print '75% generation has been done...'
        else:
            None
        Next_Generation = []
        for i in range(0, len(First_Generation)/2):
            First_Generation_Cp = First_Generation[:]
            P1 = random.choice(First_Generation_Cp)
            First_Generation_Cp.remove(P1)
            P2 = random.choice(First_Generation_Cp)
            First_Generation_Cp.remove(P2)
            Children = Crossover_Operator(P1, P2)
            Mutated_Child1 = Mutation_Operator(Children['Child1'])
            Mutated_Child2 = Mutation_Operator(Children['Child2'])
            Next_Generation.append(Mutated_Child1)
            Next_Generation.append(Mutated_Child2)
        Next_Generation.extend(First_Generation)
        Next_Generation.extend(Elites)

        Population = Next_Generation[:]
        # evaluate the population
        Population_Quality = {}
        x = 0
        for Individual in Population:
            # evaluate individual
            Individual_M = Decode_Binary(Individual,EM,N,M)

            Individual_Matrix = Individual_M['Matrix']
            Individual_Matrix_Index = Individual_M['Matrix_Index']
            Row_Variance = Row_Var(Individual_Matrix)
            if Row_Variance ==0:
                Fit_Ness = 'Bad'
            else:
                Penalty = Penalty_Cal(Individual_Matrix_Index,Results)
                Mean_Squared_Residue = Mean_Squared(Individual_Matrix)
                W_D = Mean_Square_Residue_Threshold/float(len(Individual_Matrix)) + 10*Mean_Square_Residue_Threshold/float(len(Individual_Matrix[0]))
                Fit_Ness = Mean_Squared_Residue/Mean_Square_Residue_Threshold + 1/Row_Variance + Penalty + W_D
            Population_Quality[Individual] = Fit_Ness
            x+=1
        Selected_Population = Selection_Operator(Population_Quality)
        First_Generation = Selected_Population['Good_Individual'].keys()
        Elites = Selected_Population['Elites'].keys()

    Best_Individual_Index = min(Selected_Population['Elites'].values())
    Best_Individual = Selected_Population['Elites'].keys()[Selected_Population['Elites'].values().index(Best_Individual_Index)]

    return (Best_Individual,Best_Individual_Index)





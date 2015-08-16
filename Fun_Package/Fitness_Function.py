__author__ = 'Jessie'
import math

def Mean_Squared(Matrix):
    Mean_Squared_Residue = float(0)
    I = float(len(Matrix))
    if I ==0:
        None
    else:
        J = float(len(Matrix[0]))
        if J ==0:
            None
        else:
            J = float(len(Matrix[0]))
            E_i_J = [sum(ele)/J for ele in Matrix]
            E_I_j = []
            for j in range(0,int(J)):
                eIj = sum([ele[j] for ele in Matrix])
                E_I_j.append(eIj/I)
            E_I_J = sum([sum(ele) for ele in Matrix])/(I*J)
            for i in range(0,int(I)):
                for j in range(0,int(J)):
                    Mean_Squared_Residue += (Matrix[i][j] - E_i_J[i] - E_I_j[j] + E_I_J)**2
            Mean_Squared_Residue = Mean_Squared_Residue/(I*J)
    return Mean_Squared_Residue
Matrix = [[1,1,3],[2,1,1],[1,2,3]]
#print Mean_Squared(Matrix)

def Row_Var(Matrix):
    Row_Variance = float(0)
    I = float(len(Matrix))
    if I ==0:
        None
    else:
        J = float(len(Matrix[0]))
        if J ==0:
            None
        else:
            E_i_J = [sum(ele)/J for ele in Matrix]
            for i in range(0,int(I)):
                for j in range(0,int(J)):
                    Row_Variance += (Matrix[i][j] - E_i_J[i])**2
            Row_Variance = Row_Variance/(I*J)
    return Row_Variance


def Decode_Binary(Individual,EM,N,M):
    Index = [i for i, ltr in enumerate(Individual) if ltr == '1']
    I = [i for i in Index if i < N]
    J = [j-N for j in Index if j > N]
    Matrix = []
    Matrix_Index = []
    for i in I:
        row = []
        for j in J:
            row.append(EM[i][j])
            Matrix_Index.append((i,j))
        Matrix.append(row)

    return {'Matrix':Matrix,'Matrix_Index':Matrix_Index}

def Penalty_Cal(Individual_Matrix_Index,Results):
    Penalty = float(0)
    Penalty_Numerator = math.exp(-sum([len(ele) for ele in Results]))
    for ele in Individual_Matrix_Index:
        n = 0
        Cov_eij = sum([n+1 for R in Results if ele in R])
        if Cov_eij > 0:
            Penalty_Denominator = math.exp(-Cov_eij)
            Weight = Penalty_Numerator/Penalty_Denominator
        else:
            Weight = float(0)
        Penalty += Weight
    return Penalty



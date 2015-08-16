__author__ = 'Jessie'
import os
from random import randint
def Load_Data() :
    print 'Please choose the matrix file (give index number):'
    print '1. yeast.matrix;'
    print '2. lymphoma.matrix;'
    print '3. yeast_test.matrix;'
    while True:
        try:
            DataFile = raw_input()
            File_Dic = {'1':'yeast.matrix','2':'lymphoma.matrix','3':'yeast_test.matrix'}
            if DataFile in File_Dic.keys():
                print 'You choose the file ' + File_Dic[DataFile]
                break
            else:
                print 'File can not be found, please give the name of the file again:'
        except:
            print 'File can not be found, please give the name of the file again:'

    return File_Dic[DataFile]

def Preprocess_Data(Data_File,G,C):
    Expression_Matrix = []
    Expression_Matrix_Binary = []
    File = open(Data_File,'r')
    Gi = 0
    while True:
        Line = File.readline()
        if len(Line) ==0:
            break
        else:
            Gene_Num = []
            Gene_Str = Line.split()
            Ci = 0
            for ele in Gene_Str:
                ELE_Binary = ['0']*(G + C)
                ELE_Binary[Gi] = '1'
                ELE_Binary[G+Ci] = '1'
                Expression_Matrix_Binary.append(''.join(ELE_Binary))
                Ci +=1
                if ele =='-1' or ele == '-999':
                    Gene_Num.append(randint(0,600))
                else:
                    Gene_Num.append(int(ele))
            Expression_Matrix.append(Gene_Num)
            Gi +=1
    return {'EM':Expression_Matrix,'EMB':Expression_Matrix_Binary}

#print Preprocess_Data('yeast.matrix',50,17)
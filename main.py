__author__ = 'TEST'
from Fun_Package.Data_Load_Encode import *
from Fun_Package.GA import *

# load the Expression Matrix EM
Data_File = Load_Data()
#print Data_File

# parameter setting
if Data_File =='lymphoma.matrix':
    Mean_Square_Residue_Threshold = 1200
    N = 4026
    M = 96
elif Data_File =='yeast.matrix':
    Mean_Square_Residue_Threshold = 300
    N = 2884
    M = 17
else:
    Mean_Square_Residue_Threshold = 300
    N = 50
    M = 17


# store results
Results = []

# encode the biclusters
Processed_Data = Preprocess_Data(Data_File,N,M)
Result_File = open('Result_File.txt','w')
Result_File.write('No.' + '\t' + 'Rows' + '\t' + 'Columns' + '\t' + 'Mean Squared Residue' + '\t' + 'Row Variance' + '\n')
Max_Iteration = 10
for i in range(0,Max_Iteration):
    print 'No.' + str(i+1) + ' is running...'
    Bicluster_String = Genetic_Algorithm(Processed_Data['EM'],Processed_Data['EMB'],Results,N,M,Mean_Square_Residue_Threshold)

    Bicluster = Decode_Binary(Bicluster_String[0],Processed_Data['EM'],N,M)

    Row_Variance = Row_Var(Bicluster['Matrix'])
    Mean_Square_Residue = Mean_Squared(Bicluster['Matrix'])
    Rows = len(Bicluster['Matrix'])
    Columns = len(Bicluster['Matrix'][0])
    Results.append(Bicluster['Matrix_Index'])
    #print Row_Variance
    #print Mean_Square_Residue
    #print Rows
    #print Columns
    Result_File.write(str(i) + '\t' + str(Rows) + '\t' + str(Columns) + '\t' + str(Mean_Square_Residue) + '\t' + str(Row_Variance) + '\n')
Result_File.close()

print 'Algorithm Done.'


